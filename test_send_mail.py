import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

api_key = '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'
sg = SendGridAPIClient(api_key)

def send_test_email(subject, html_content, sender_email, recipient_email):
    message = Mail(
        from_email=sender_email,
        to_emails=recipient_email,
        subject=subject,
        html_content=html_content
    )
    try:
        response = sg.send(message)
        print("Test email sent successfully to", recipient_email)
    except Exception as e:
        print("Failed to send test email:", e)

def read_html_content_from_file(html_file):
    with open(html_file, 'r') as file:
        html_content = file.read()
    return html_content

subject = "RHHS Women's Way - March Issue"
html_file = "womens-way-WD/content.html"
sender_email = "rhhswomensway@gmail.com"
recipient_email = "cozyat@gmail.com"

html_content = read_html_content_from_file(html_file)

send_test_email(subject, html_content, sender_email, recipient_email)
