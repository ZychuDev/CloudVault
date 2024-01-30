from google.cloud import storage

import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

def convert_epub_to_mobi(event, context):
    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

    file_name = event['name']
    bucket_name = event['bucket']

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    local_file_path = f"/tmp/{file_name}"
    blob.download_to_filename(local_file_path)


    file_path = local_file_path
    with open(file_path, 'rb') as file:
        file_data = file.read()
        file_data = base64.b64encode(file_data).decode('utf-8')

    message = Mail(
        from_email='wzychowicz@student.agh.edu.pl',
        to_emails='wzychowicz@student.agh.edu.pl',
        subject='Ebook delivery',
        html_content= 'Hello, in an attachment you can find your ebook.'
    )

    attachment = Attachment(
        FileContent(file_data),
        FileName(file_name),
        FileType('application/epub+zip'),
        Disposition('attachment')
    )
    message.attachment = attachment

    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)

