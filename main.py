from flask import Flask, request, jsonify
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.json
        gmail_user = os.environ.get('GMAIL_USER')
        gmail_password = os.environ.get('GMAIL_PASSWORD')

        if not gmail_user or not gmail_password:
            raise ValueError("GMAIL_USER or GMAIL_PASSWORD environment variables are not set")

        sent_from = gmail_user
        to = ['app.melinas@gmail.com']
        subject = data.get('subject')
        body = data.get('message')

        if not subject or not body:
            raise ValueError("Subject or body of email is missing")
        
        msg = MIMEMultipart()
        msg['From'] = sent_from
        msg['To'] = ", ".join(to)
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        text = msg.as_string()
        server.sendmail(sent_from, to, text)
        server.close()

        return jsonify({'status': 'success', 'message': 'Email sent successfully!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

def entry_point(request):
    return app
