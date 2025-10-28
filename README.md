Certificate Automation – Full Documentation Guide

OVERVIEW
This project automates the generation and emailing of certificates using Python.
It uses Pillow for image processing, Pandas for data handling, and smtplib for email automation.

FOLDER STRUCTURE
cert-automation/
│
├── output/ - Generated certificates (PNG & PDF)
│ ├── Juan_Dela_Cruz.pdf
│ ├── Juan_Dela_Cruz.png
│
├── font.ttf - Font used in certificate
├── template.png - Certificate background image
├── recipients.csv - Recipient list (name, course, date, email)
├── generate_certificates.py - Script to generate certificates
├── send_emails.py - Script to email certificates
└── README.txt - This documentation

INSTALLATION

Install Dependencies
Run in PowerShell or terminal:
pip install pillow pandas

PREPARING FILES

template.png
Your certificate background image. It should have blank spaces for the name, course, and date.

font.ttf
The font used to write the text on the certificate.

recipients.csv
Create a CSV file with the following columns:
name,course,date,email
Juan Dela Cruz,Python Workshop,Oct 28 2025,juan@gmail.com

Maria Santos,Python Workshop,Oct 28 2025,maria@gmail.com

CERTIFICATE GENERATION
Run this command:
python generate_certificates.py

This will:

Read recipients.csv

Write the name, course, and date on template.png

Save each as PNG and PDF in the output folder

Example output:
Template loaded (2000 x 1414)
Saved certificate for Juan Dela Cruz
Saved certificate for Maria Santos
All certificates generated successfully!

GMAIL SETUP FOR SENDING CERTIFICATES

Create a Gmail App Password
Go to https://myaccount.google.com/apppasswords

Select “Mail” then “Windows Computer”.
Copy the 16-character app password (example: abcd efgh ijkl mnop).

Set Environment Variables (PowerShell)
Before running the email sender, set your Gmail credentials:

$env:SENDER_EMAIL = "youremail@gmail.com
"
$env:SENDER_PASSWORD = "your_app_password"

SENDING CERTIFICATES VIA EMAIL
Run this command:
python send_emails.py

This will send an email with each participant’s certificate attached.

Example output:
Found 2 recipients with emails.
Mode: SENDING ACTUAL EMAILS

Sending to Juan Dela Cruz juan@gmail.com

Attachment: Juan_Dela_Cruz.pdf
Sent successfully.

Sending to Maria Santos maria@gmail.com

Attachment: Maria_Santos.pdf
Sent successfully.

DRY RUN MODE (TEST WITHOUT SENDING)
If you only want to simulate sending without actually emailing, set:
main(dry_run=True)

This will print what would be sent but not actually connect to Gmail.

LIBRARIES USED

Pillow (PIL) - Opens the certificate template, writes text, saves images and PDFs
Pandas - Reads and manages CSV recipient data
smtplib - Connects to Gmail’s SMTP server
EmailMessage - Builds and attaches PDF to the email
os - Handles file paths and environment variables

STEP-BY-STEP SUMMARY

Install dependencies: pip install pillow pandas

Prepare your files: template, font, and CSV

Generate certificates: python generate_certificates.py

Set Gmail environment variables: $env:SENDER_EMAIL="..."

Send emails: python send_emails.py

OPTIONAL: GIT SETUP

Initialize and push this project to GitHub:

git init
git add .
git commit -m "Initial commit - certificate automation project"
git branch -M main
git remote add origin https://github.com/your-username/cert-automation.git

git push -u origin main

Optional .gitignore file to exclude unnecessary items:

output/
pycache/
*.env
*.pyc

