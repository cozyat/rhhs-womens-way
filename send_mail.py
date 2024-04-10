import os
import csv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

api_key = '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'
sg = SendGridAPIClient(api_key)

def send_newsletter(subject, html_content, sender_email, recipient_emails):
    message = Mail(
        from_email=sender_email,
        subject=subject,
        html_content=html_content
    )
    for email in recipient_emails:
        message.add_bcc(email)
    try:
        response = sg.send(message)
        print("Newsletter sent successfully to", len(recipient_emails), "recipients")
    except Exception as e:
        print("Failed to send newsletter:", e)
        # debug if print as e

def read_recipient_emails_from_csv(csv_file):
    recipient_emails = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            recipient_emails.append(row[2]) # CSV file must have a 2nd row
    return recipient_emails

def read_html_content_from_file(html_file):
    with open(html_file, 'r') as file:
        html_content = file.read()
    return html_content # update html before sending

subject = "RHHS Women's Way - March Issue" # change this title
html_file = "womens-way-WD/content.html"
sender_email = "rhhswomensway@gmail.com"
csv_file = "womens-way-WD/signups.csv"

html_content = read_html_content_from_file(html_file)
recipient_emails = read_recipient_emails_from_csv(csv_file)

send_newsletter(subject, html_content, sender_email, recipient_emails)

# review any outdated elements, refactor if needed
