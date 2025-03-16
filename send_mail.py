from sendgrid.helpers.mail import Mail, Email, To, Bcc
from sendgrid import SendGridAPIClient
import datetime
import sys
import csv

api_key = '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'
sg = SendGridAPIClient(api_key)

def send_newsletter(subject, html_content, sender_email, recipient_emails):
    recipient_emails_filtered = []
    for email in recipient_emails:
        if email.lower() != sender_email.lower():
            recipient_emails_filtered.append(email)
    recipient_emails = recipient_emails_filtered
    message = Mail(
        from_email=Email(sender_email),
        to_emails=[To(sender_email)],
        subject=subject,
        html_content=html_content
    )
    for email in recipient_emails:
        message.add_bcc(Bcc(email))
    try:
        response = sg.send(message)
        print(f"Email sent successfully to {len(recipient_emails)} recipients! Status Code: {response.status_code}")
        print(f"SendGrid Response: {response.body}")
    except Exception as e:
        print("Failed to send newsletter:", e)
        if hasattr(e, 'body'):
            print("SendGrid Error Details:", e.body)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("womens-way-WD/error_log.txt", "a") as error_file:
            error_file.write(f"NEWSLETTER - [{current_time}] {str(e)}\n")

def read_recipient_emails_from_csv(csv_file):
    recipient_emails = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            recipient_emails.append(row[0])
    return recipient_emails

def read_html_content_from_file(html_file):
    with open(html_file, 'r') as file:
        return file.read()

subject = "RHHS Women's Way - March Issue"
html_file = "womens-way-WD/content.html"
sender_email = "rhhswomensway@gmail.com"
csv_file = "womens-way-WD/signups.csv"

html_content = read_html_content_from_file(html_file)
recipient_emails = read_recipient_emails_from_csv(csv_file)
send_newsletter(subject, html_content, sender_email, recipient_emails)

sys.exit()