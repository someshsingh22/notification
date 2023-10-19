import os
import yagmail
import logging


def send_email(subject, body, recipient_email):
    sender_email = os.environ.get("EMAIL_USERNAME")
    sender_password = os.environ.get("EMAIL_PASSWORD")
    yag = yagmail.SMTP(sender_email, sender_password)
    logging.info("SMTP connection established.")
    yag.send(to=recipient_email, subject=subject, contents=body)
    yag.close()
    logging.info("Email sent successfully!")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Send an email using yagmail.")
    parser.add_argument("subject", type=str, help="Subject of the email", required=True)
    parser.add_argument("body", type=str, help="Body of the email", required=True)
    parser.add_argument("recipient_email", type=str, help="Recipient email address")
    args = parser.parse_args()
    if args.recipient_email is None:
        logging.info(
            "No recipient email provided. Using sender email as recipient email."
        )
        send_email(args.subject, args.body, os.environ.get("EMAIL_USERNAME"))
    else:
        send_email(args.subject, args.body, args.recipient_email)


if __name__ == "__main__":
    main()
