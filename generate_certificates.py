import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Paths
TEMPLATE_PATH = r"C:\Users\Terryl Jean\Downloads\cert-automation\certificate.png"
FONT_PATH = r"C:\Users\Terryl Jean\Downloads\cert-automation\font.ttf"
CSV_PATH = r"C:\Users\Terryl Jean\Downloads\cert-automation\recipients.csv"
OUTPUT_DIR = r"C:\Users\Terryl Jean\Downloads\cert-automation\output"

# Coordinates for name placement
NAME_X = 1020   # horizontal center (from your provided position)
NAME_Y = 760    # vertical position in the blank area

# Font settings
NAME_FONT_SIZE = 100
TEXT_COLOR = (0, 0, 0)

def draw_centered_text(draw, text, font, center_x, y, color):
    try:
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
    except AttributeError:
        text_width, _ = draw.textsize(text, font=font)
    x = center_x - text_width / 2  # center horizontally around center_x
    draw.text((x, y), text, font=font, fill=color)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df = pd.read_csv(CSV_PATH, dtype=str).fillna("")

    try:
        template = Image.open(TEMPLATE_PATH).convert("RGB")
    except FileNotFoundError:
        print(f"❌ Template not found at: {TEMPLATE_PATH}")
        return

    try:
        font_name = ImageFont.truetype(FONT_PATH, NAME_FONT_SIZE)
    except OSError:
        print(f"❌ Font file not found or invalid: {FONT_PATH}")
        return

    width, height = template.size
    print(f"✅ Template loaded ({width} x {height})")

    for _, row in df.iterrows():
        name = row.get("name", "").strip()
        if not name:
            print("⚠️ Skipping empty name row.")
            continue

        cert = template.copy()
        draw = ImageDraw.Draw(cert)

        draw_centered_text(draw, name, font_name, NAME_X, NAME_Y, TEXT_COLOR)

        safe_name = name.replace(" ", "_").replace("/", "-")
        out_png = os.path.join(OUTPUT_DIR, f"{safe_name}.png")
        out_pdf = os.path.join(OUTPUT_DIR, f"{safe_name}.pdf")

        cert.save(out_png, "PNG")
        cert.save(out_pdf, "PDF", resolution=300.0)

        print(f"✅ Saved certificate for {name}")

    print("\nAll certificates generated successfully!")

if __name__ == "__main__":
    main()
