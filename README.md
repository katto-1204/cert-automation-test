CERTIFICATE AUTOMATION PROJECT
DESCRIPTION

This project automates the generation and emailing of personalized certificates using Python.
It creates custom certificates from a template image, fills in recipient details (name, course, and date), saves them as PNG and PDF files, and optionally sends them via email.

TECHNOLOGIES USED

Python 3.10 or higher

Pillow – for image editing and text placement

Pandas – for reading CSV data

smtplib – for sending emails

email.message – for creating email messages with attachments

os – for file and environment handling

PROJECT STRUCTURE

cert-automation/
│
├── template.png Certificate template image
├── font.ttf Font file used for writing text
├── recipients.csv Recipient information list
├── output/ Folder where generated certificates are saved
├── generate_certificates.py Script that generates certificates
├── send_emails.py Script that sends certificates through email
└── README.md Documentation file (this one)

REQUIRED FILES

template.png
The image background of your certificate. Leave blank spaces where text (name, course, date) will appear.

font.ttf
The font file to be used for the certificate text.

recipients.csv
A list of recipients with the following headers:
name,course,date,email

Example:
Juan Dela Cruz,Python Basics,October 28 2025,juan@gmail.com

Maria Santos,Data Science 101,October 28 2025,maria@gmail.com

INSTALLATION

Install Python 3.10 or later.

Open a terminal or PowerShell inside your project folder.

Install required packages:

pip install pillow pandas

STEP 1: GENERATE CERTIFICATES

Run the certificate generator script:

python generate_certificates.py

This will:

Read recipient information from recipients.csv

Write their name, course, and date onto the certificate template

Save each certificate as both PNG and PDF in the output folder

STEP 2: SET UP GMAIL APP PASSWORD

If using Gmail, you must use an App Password to send emails securely.

Go to your Google Account

Navigate to Security > 2-Step Verification > App Passwords

Generate a new app password for "Mail" and "Windows Computer"

Copy the 16-character app password (use this instead of your real Gmail password)

STEP 3: SET EMAIL VARIABLES

Before running the email sender, set your credentials in PowerShell:

$env:SENDER_EMAIL = "youremail@gmail.com
"
$env:SENDER_PASSWORD = "your_app_password"

Example:

$env:SENDER_EMAIL = "g11.arnadoc@gmail.com
"
$env:SENDER_PASSWORD = "tznz nwzc xdqb heue"

STEP 4: SEND EMAILS

Run the email sender script:

python send_emails.py

This will:

Read the recipients.csv file

Match each name to its corresponding certificate file

Send the email with the certificate attached

The program logs each step (who it sends to, what file, and if it succeeded).

STEP 5: DRY RUN MODE

You can test the program without actually sending emails.
To do this, open send_emails.py and change:

main(dry_run=False)

to

main(dry_run=True)

STEP 6: GITHUB SETUP

Initialize a git repository:

git init

Add all project files:

git add .

Commit your changes:

git commit -m "Initial commit - certificate automation project"

Add your remote GitHub repository:

git branch -M main
git remote add origin https://github.com/your-username/cert-automation.git

Push to GitHub:

git push -u origin main

TROUBLESHOOTING

If you get "Template not found" – Check that template.png is in the same folder.

If "Font file not found" – Verify your font.ttf path is correct.

If "ERROR: SENDER_EMAIL and SENDER_PASSWORD must be set" – Re-enter the PowerShell environment variables.

If email fails – Ensure Less Secure Apps is disabled and you are using an App Password.

OUTPUT EXAMPLES

Certificate files: output/Juan_Dela_Cruz.pdf, output/Juan_Dela_Cruz.png

Console log examples:
Template loaded (2000 x 1414)
Saved certificate for Juan Dela Cruz
Sent email to juan@gmail.com