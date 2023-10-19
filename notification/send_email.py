import os
import yagmail


def send_email(subject, body, recipient_email):
    # Load email and password from environment variables
    sender_email = os.environ.get("EMAIL_USERNAME")
    sender_password = os.environ.get("EMAIL_PASSWORD")

    # Check if email credentials are provided
    if sender_email is None or sender_password is None:
        print("Error: Email credentials not provided.")
        exit(1)

    # Set a default recipient email address if not provided
    if recipient_email is None:
        recipient_email = "someshs@gmail.com"

    # Create the yagmail SMTP client
    yag = yagmail.SMTP(sender_email, sender_password)

    # Send the email
    yag.send(to=recipient_email, subject=subject, contents=body)

    # Close the SMTP connection
    yag.close()

    print("Email sent successfully.")


def main():
    import argparse

    # Initialize argparse
    parser = argparse.ArgumentParser(description="Send an email using yagmail.")

    # Add command-line arguments
    parser.add_argument("subject", type=str, help="Subject of the email")
    parser.add_argument("body", type=str, help="Body of the email")
    parser.add_argument("--recipient_email", type=str, help="Recipient email address")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Extract arguments and call the send_email function
    send_email(args.subject, args.body, args.recipient_email)


if __name__ == "__main__":
    main()
