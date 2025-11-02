import os
import pandas as pd
import smtplib
from email.message import EmailMessage

# --- File paths ---
OUTPUT_DIR = r"C:\Users\Terryl Jean\Downloads\cert-automation\output"
CSV_PATH = r"C:\Users\Terryl Jean\Downloads\cert-automation\recipients.csv"

# --- Email settings ---
SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")

SUBJECT_TEMPLATE = "hello nara oh {course}"
BODY_TEMPLATE = """yo {name},

Congratulations on completing {course} on {date}!

Attached is your certificate.

Best regards,  
Your Team
"""

# --- Helper functions ---
def safe_filename(name):
    return name.replace(" ", "_").replace("/", "-")

def send_email_with_attachment(smtp, to_email, subject, body, attachment_path):
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    with open(attachment_path, "rb") as f:
        data = f.read()
    filename = os.path.basename(attachment_path)
    msg.add_attachment(data, maintype="application", subtype="pdf", filename=filename)

    smtp.send_message(msg)

# --- Main ---
def main(dry_run=True):
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        print("ERROR: SENDER_EMAIL and SENDER_PASSWORD must be set as environment variables.")
        return

    df = pd.read_csv(CSV_PATH, dtype=str).fillna("")
    if "email" not in df.columns or "name" not in df.columns:
        print("ERROR: CSV must include 'name' and 'email' columns.")
        return

    df = df[df["email"].str.strip().astype(bool)]
    if df.empty:
        print("No recipients with email found in CSV.")
        return

    print(f"✅ Found {len(df)} recipients with emails.")
    print("📦 Mode:", "DRY RUN (no emails sent)" if dry_run else "SENDING ACTUAL EMAILS")
    print()

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
            smtp.ehlo()
            if SMTP_PORT == 587:
                smtp.starttls()
                smtp.ehlo()
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)

            for _, row in df.iterrows():
                name = row.get("name", "").strip()
                email = row.get("email", "").strip()
                course = row.get("course", "the course").strip()
                date = row.get("date", "").strip()

                safe_name = safe_filename(name)
                pdf_path = os.path.join(OUTPUT_DIR, f"{safe_name}.pdf")
                png_path = os.path.join(OUTPUT_DIR, f"{safe_name}.png")

                attachment_path = pdf_path if os.path.exists(pdf_path) else (
                    png_path if os.path.exists(png_path) else None
                )

                if not attachment_path:
                    print(f"⚠️ Skipping {name}: no certificate found.")
                    continue

                subject = SUBJECT_TEMPLATE.format(course=course)
                body = BODY_TEMPLATE.format(name=name, course=course, date=date)

                print(f"{'Would send' if dry_run else 'Sending'} to {name} <{email}>")
                print(f"  ↳ Attachment: {os.path.basename(attachment_path)}")

                if not dry_run:
                    try:
                        send_email_with_attachment(smtp, email, subject, body, attachment_path)
                        print("  ✅ Sent successfully.\n")
                    except Exception as e:
                        print(f"  ❌ ERROR sending: {e}\n")
                else:
                    print("  (Dry-run only, not sent)\n")

    except Exception as e:
        print("❌ SMTP connection/login failed:", e)

# --- Run ---
if __name__ == "__main__":
    # Change to False when you’re ready to really send
    main(dry_run=False)
