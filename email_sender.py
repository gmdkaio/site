import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email_with_attachment(pdf_content, user_info):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'gmdkaio@gmail.com'
    sender_password = 'gtskhgztskdkwmvb'
    receiver_email = 'teste.enviaremails@gmail.com'  

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Solicitação'

    # Construct the email content
    email_content = (
        f"Nome do cliente: {user_info['nome']}\n"
        f"Celular do cliente: {user_info['celular']}\n"
        f"Email do cliente: {user_info['email']}\n"
        f"Nome da empresa: {user_info['empresa']}\n"
    )

    msg.attach(MIMEText(email_content, 'plain'))

    # Attach the generated PDF
    pdf_attachment = MIMEApplication(pdf_content)
    pdf_attachment.add_header('Content-Disposition', 'attachment', filename='solicitacao.pdf')
    msg.attach(pdf_attachment)

    # Connect to SMTP server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", str(e))

def send_email_to_user(pdf_content, user_info, user):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'gmdkaio@gmail.com'
    sender_password = 'gtskhgztskdkwmvb'
    receiver_email = user 

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Solicitação'

    # Construct the email content
    email_content = (
        f"{user_info['nome']}, obrigado por usar o site, entraremos em contato em breve."
    )

    msg.attach(MIMEText(email_content, 'plain'))

    # Attach the generated PDF
    pdf_attachment = MIMEApplication(pdf_content)
    pdf_attachment.add_header('Content-Disposition', 'attachment', filename='solicitacao.pdf')
    msg.attach(pdf_attachment)

    # Connect to SMTP server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", str(e))


def send_email_with_feedback(feedback_content, user_info):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'gmdkaio@gmail.com'
    sender_password = 'gtskhgztskdkwmvb'
    receiver_email = 'teste.enviaremails@gmail.com'  

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Feedback Submission'

    email_content = (
        f"Nome do cliente: {user_info['nome']}\n"
        f"Email do cliente: {user_info['email']}\n"
        f"Feedback do site:\n{feedback_content}\n"
    )

    msg.attach(MIMEText(email_content, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Feedback email sent successfully!")
    except Exception as e:
        print("Error sending feedback email:", str(e))