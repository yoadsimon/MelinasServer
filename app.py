from flask import Flask, request, jsonify
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    message = Mail(
        from_email='app.melinas@gmail.com',
        to_emails='app.melinas@gmail.com',
        subject=data.get('subject'),
        plain_text_content=data.get('message'),
    )

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        return jsonify({'status': 'success', 'message': 'Email sent successfully!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run()

def entry_point(request):
    return app(request)
