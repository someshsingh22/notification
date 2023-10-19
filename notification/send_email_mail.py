import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, body, recipient_email):
    # Load email and password from environment variables
    sender_email = os.environ.get("EMAIL_USERNAME")
    sender_password = os.environ.get("EMAIL_PASSWORD")

    # Check if email credentials are provided
    if sender_email is None or sender_password is None:
        print("Error: Email credentials not provided.")
        exit(1)

    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, "plain"))

    # Connect to the Gmail SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        # Login to your email account
        server.login(sender_email, sender_password)

        # Convert the message to a string
        text = message.as_string()

        # Send the email
        server.sendmail(sender_email, recipient_email, text)

    print("Email sent successfully.")

def main():
    import argparse

    # Initialize argparse
    parser = argparse.ArgumentParser(description="Send an email using Gmail SMTP.")

    # Add command-line arguments
    parser.add_argument("subject", type=str, help="Subject of the email")
    parser.add_argument("body", type=str, help="Body of the email")
    parser.add_argument("--recipient_email", type=str, help="Recipient email address")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Extract arguments and call the send_email function
    
    # Check if recipient email is provided
    if args.recipient_email is None:
        print("Warning: Recipient email address not provided. Using default email address.")
        target = "singhksomesh@gmail.com"
    else:
        target = args.recipient_email    
    send_email(args.subject, args.body, target)

if __name__ == "__main__":
    main()
