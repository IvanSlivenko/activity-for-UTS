import smtplib
from email.message import EmailMessage

test="k5V4deTDXviQVuIW"

# Створюємо повідомлення
message = EmailMessage()

message["Subject"] = "Hello from UmanProger"
message["From"] = "UmanProger@ukr.net"
message["To"] = "UmanProger@ukr.net"

message.set_content("Hello Student")

# Підключаємося до SMTP-сервера UKR.NET
with smtplib.SMTP_SSL("smtp.ukr.net", 465) as server:

    # Авторизація
    server.login(
        "UmanProger@ukr.net",
        test
    )

    # Відправлення листа
    server.send_message(message)

print("Email sent successfully!")