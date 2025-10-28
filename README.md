# Certificate Automation Project

## Description
This project automates the generation and emailing of personalized certificates using Python.  
It creates custom certificates from a template image, fills in recipient details (name, course, and date), saves them as PNG and PDF files, and optionally sends them via email.

---

## Technologies Used
- **Python 3.10** or higher  
- **Pillow** – for image editing and text placement  
- **Pandas** – for reading CSV data  
- **smtplib** – for sending emails  
- **email.message** – for creating email messages with attachments  
- **os** – for file and environment handling  

---

## Project Structure

cert-automation/
│
├── template.png # Certificate template image
├── font.ttf # Font file used for writing text
├── recipients.csv # Recipient information list
├── output/ # Folder where generated certificates are saved
├── generate_certificates.py # Script that generates certificates
├── send_emails.py # Script that sends certificates through email
└── README.md # Documentation file (this one)


---

## Required Files

**template.png**  
The image background of your certificate. Leave blank spaces where text (name, course, date) will appear.

**font.ttf**  
The font file to be used for the certificate text.

**recipients.csv**  
A list of recipients with the following headers:  
`name,course,date,email`

**Example:**


Juan Dela Cruz,Python Basics,October 28 2025,juan@gmail.com

Maria Santos,Data Science 101,October 28 2025,maria@gmail.com


---

## Installation
1. Install Python 3.10 or later.
2. Open a terminal or PowerShell inside your project folder.
3. Install dependencies:


pip install pillow pandas


---

## Step 1: Generate Certificates
Run the certificate generator script:


python generate_certificates.py


This will:
- Read recipient information from `recipients.csv`
- Write their name, course, and date onto the certificate template
- Save each certificate as both PNG and PDF in the `output` folder

---

## Step 2: Set Up Gmail App Password
If you are using Gmail, you must use an App Password for secure email sending.

1. Go to your Google Account  
2. Navigate to **Security > 2-Step Verification > App Passwords**  
3. Generate a new app password for "Mail" and "Windows Computer"  
4. Copy the 16-character app password (use this instead of your real Gmail password)

---

## Step 3: Set Email Variables
Before running the email sender, set your credentials in PowerShell:


$env:SENDER_EMAIL = "youremail@gmail.com
"
$env:SENDER_PASSWORD = "your_app_password"


**Example:**


$env:SENDER_EMAIL = "g11.arnadoc@gmail.com
"
$env:SENDER_PASSWORD = "tznz nwzc xdqb heue"


---

## Step 4: Send Emails
Run the email sender script:


python send_emails.py


This will:
- Read `recipients.csv`
- Match each recipient name to their corresponding certificate file
- Send the email with the certificate attached

The program logs each step (who it sends to, what file, and if it succeeded).

---

## Step 5: Dry Run Mode
You can test the program without actually sending emails.  
In `send_emails.py`, change:


main(dry_run=False)

to


main(dry_run=True)


---

## Step 6: GitHub Setup
1. Initialize a git repository:


git init


2. Add all project files:


git add .


3. Commit your changes:


git commit -m "Initial commit - certificate automation project"


4. Add your remote GitHub repository:


git branch -M main
git remote add origin https://github.com/your-username/cert-automation.git


5. Push to GitHub:


git push -u origin main


---

## Troubleshooting

**Error:** `Template not found`  
→ Check that `template.png` is in the same folder.

**Error:** `Font file not found`  
→ Verify that your `font.ttf` path is correct.

**Error:** `ERROR: SENDER_EMAIL and SENDER_PASSWORD must be set`  
→ Re-enter the PowerShell environment variables.

**Error:** Email not sending  
→ Ensure you are using an App Password (not your normal Gmail password).

---

## Output Examples
- Certificate files:


output/Juan_Dela_Cruz.pdf
output/Juan_Dela_Cruz.png


- Console output:


Template loaded (2000 x 1414)
Saved certificate for Juan Dela Cruz
Sent email to juan@gmail.com


---

## Author
Developed by **Catherine Arnad**  
Davao City, Philippines  
Python Version: 3.13
