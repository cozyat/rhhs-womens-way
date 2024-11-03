from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import datetime
import sys
import csv

api_key = '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'
sg = SendGridAPIClient(api_key)

def send_newsletter(subject, html_content, sender_email, recipient_emails):
    message = Mail(from_email=sender_email, to_emails=recipient_emails, subject=subject, html_content=html_content)
    try:
        response = sg.send(message)
        print("Newsletter sent successfully to", len(recipient_emails), "recipients")
    except Exception as e:
        print("Failed to send newsletter:", e)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("womens-way-WD/error_log.txt", "a") as error_file:
            error_file.wirte(f"TEST EMAIL - [{current_time}] {str(e)}\n")

def read_recipient_emails_from_csv(csv_file):
    recipient_emails = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            recipient_emails.append(row[0])
    return recipient_emails

def read_html_content_from_file(html_file):
    with open(html_file, 'r') as file:
        html_content = file.read()
    return html_content

# params & args
subject = "RHHS Women's Way - October Issue"
html_file = "womens-way-WD/content.html"
sender_email = "rhhswomensway@gmail.com"
csv_file = "womens-way-WD/signups.csv"

# run all funcs
html_content = read_html_content_from_file(html_file)
recipient_emails = read_recipient_emails_from_csv(csv_file)
send_newsletter(subject, html_content, sender_email, recipient_emails)
sys.exit()