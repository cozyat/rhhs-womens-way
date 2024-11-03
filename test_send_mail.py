import sys
import datetime
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
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("womens-way-WD/error_log.txt", "a") as error_file:
            error_file.write(f"TEST EMAIL - [{current_time}] {str(e)}\n")

def read_html_content_from_file(html_file):
    with open(html_file, 'r') as file:
        html_content = file.read()
    return html_content

subject = "RHHS Women's Way - October Issue"
html_file = "womens-way-WD/content.html"
sender_email = "rhhswomensway@gmail.com"
recipient_email = "cozyat@gmail.com"

html_content = read_html_content_from_file(html_file)

send_test_email(subject, html_content, sender_email, recipient_email)
sys.exit()