# Notification-Sender
Simple Email App to send me notifications

# Email Sender Script

This Python script uses the yagmail library to send emails.

## Usage

1. Install the required packages:

```bash
pip install -r requirements.txt
export EMAIL_USERNAME=your_email@gmail.com
export EMAIL_PASSWORD=your_email_password
```

## Usage

```bash
python send_email.py "Test Subject" "Hello, this is the email body." "recipient@example.com"
```


## Notes:

1. **Environment Variables:** Before running the script, make sure to set up your email credentials as environment variables.

2. **Usage:** The `README.md` file provides instructions on how to install the required packages and run the script.

3. **Security Note:** Be cautious with storing and sharing email credentials. It's recommended to use secure methods to store and retrieve your credentials.
