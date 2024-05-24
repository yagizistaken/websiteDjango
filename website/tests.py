from django.core.mail import send_mail


def test_email_sending():
    subject = 'Test Email'
    message = 'This is a test email to check email sending functionality.'
    from_email = 'smtp.gmail.com'  # Gönderici e-posta adresi
    to_email = ['yagizxatesok@gmail.com']  # Alıcı e-posta adresleri (liste olarak)

    try:
        send_mail(subject, message, from_email, to_email)
        print("Test email sent successfully!")
    except Exception as e:
        print(f"Error sending test email: {e}")
