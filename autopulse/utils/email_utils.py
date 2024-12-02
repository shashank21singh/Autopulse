import smtplib
from email.mime.text import MIMEText
from getpass import getpass  # Securely takes password input

def send_bulk_emails(email_list, subject, message):
    # Prompt user for sender email and password
    sender_email = input("Enter your email address: ")
    password = getpass("Enter your email password (input hidden): ")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            print("Login successful!")

            for email in email_list:
                msg = MIMEText(message)
                msg["Subject"] = subject
                msg["From"] = sender_email
                msg["To"] = email

                server.sendmail(sender_email, email, msg.as_string())
                print(f"Email sent to {email}")

    except smtplib.SMTPAuthenticationError:
        print("Failed to login. Please check your email or password.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    email_list = ["example1@example.com", "example2@example.com"]
    subject = "Test Email"
    message = "This is a test email sent via Python."
    send_bulk_emails(email_list, subject, message)
