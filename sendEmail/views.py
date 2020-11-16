from django.shortcuts import render
from django.http.response import HttpResponse

def send(receiverEmail, verifyCode):
    try:
        content = {'verifyCode':verifyCode}
        msg_html = render_to_string('sendEmail/email_format.html',content)
        msg = EmailMessage(subject='인증 코드 발송 메일',
                            body=msg_html,
                            from_email='lhs4859@naver.com',
                            bcc=[receiverEmail])
        msg.content_subtype='html'
        msg.send()
        return True
    except:
        return False