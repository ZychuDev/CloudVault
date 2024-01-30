# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

SENDGRID_API_KEY = "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"
message = Mail(
    from_email='wzychowicz@student.agh.edu.pl',
    to_emails='wzychowicz@student.agh.edu.pl',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>'
)

file_path = "../../assets/Romeo_and_Juliet.epub"
with open(file_path, 'rb') as file:
    file_data = file.read()
    file_data = base64.b64encode(file_data).decode('utf-8')

attachment = Attachment(
    FileContent(file_data),
    FileName("test.epub"),
    FileType('application/epub+zip'),
    Disposition('attachment')
)
message.attachment = attachment

sg = SendGridAPIClient(SENDGRID_API_KEY )
response = sg.send(message)
print(response.status_code)
print(response.body)
print(response.headers)
