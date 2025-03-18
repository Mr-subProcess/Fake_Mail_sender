# Fake_Mail_sender

Python Email Sender with File Attachment
This project demonstrates how to send an email using Python and attach a file. It uses SMTP (Simple Mail Transfer Protocol) to send the email and can also send files as attachments.

Features
Send email using SMTP (Gmail's SMTP server).
Send plain text messages.
Attach files to emails.
Requirements
Python 3 or higher.
Installation
Make sure you have Python 3 installed. You can download it from python.org.

The required libraries (smtplib, email.mime) are part of the Python standard library, so no additional installations are necessary.

Setup
Update Email Information:
Edit the following variables in the script:

sender = "your_email@gmail.com"
receiver = "receiver_email@gmail.com"
subject = "Email Subject"
message = "Your email message text goes here"
password = "your_app_password"  # Use Gmail App Password


Attach a File (Optional):
If you want to attach a file, update the file_path:

file_path = "path/to/your/file.pdf"  # Path to the file you want to attach
If you don’t want to send a file, leave file_path empty.

Run the Script:
Execute the script to send the email.

python send_email.py
Using Gmail
If you're using Gmail, you must generate an App Password (due to Google blocking less secure apps). To create an App Password:

Go to Google Account.
Enable 2-Step Verification.
Generate an App Password and use it as the password in the script.
SMTP Connection
The script uses Gmail's SMTP server (smtp.gmail.com) with port 587. If you're using a different email provider, make sure to update the SMTP settings accordingly.

Example Output
Successful Email:
Mail has been sent

Error:
If there's an issue, you'll see an error message:
Error: [error message]
