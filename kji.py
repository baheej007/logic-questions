import smtplib

sender = "you@gmail.com"
password = "your-app-password"
receiver = "friend@example.com"

msg = "Subject: Hello\n\nThis is a test email from Python."
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender, password)
server.sendmail(sender, receiver, msg)
server.quit()
