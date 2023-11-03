import ssl
import time
from email.message import EmailMessage
import smtplib
import pandas as pd
df = pd.read_csv('email_addresses.csv', usecols=['Email'])
# df = df.dropna()


company_mails = list(df['Email'])
# company_mails = ['']
# print(company_names)
# print(company_mails)
# print(recruiter_names)


smtp_server = 'smtp.gmail.com'
smtp_port = 465
sender_email = 'priyanshurajput822400@gmail.com'
sender_password = 'hrmnmsyjstpzjruf'  # password
subject = 'Regarding Software Developer Role'

context = ssl.create_default_context()
server = smtplib.SMTP_SSL(smtp_server, smtp_port, context=context)
server.login(sender_email, sender_password)


for email in company_mails:
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["Subject"] = subject
#     msg["Cc"] = ''
    message = f"""
Hello Sir/Ma'am,

Hope you are doing well. I am writing to express my interest in the  Developer  role. I am a highly motivated and skilled computer science student.

In particular, I am well-versed with data structures and algorithms and have experience in developing efficient and optimized code using react framework. I'm confident that my skills and passion for technology make me an ideal candidate for this position.I will be graduating in june 2024.

I am eager to contribute to your team and help develop innovative solutions. I am a quick learner and am always looking for new challenges and opportunities to grow.

I am attaching my resume and a cover letter with this email for your reference.

Thank you for your time and consideration and I am looking forward to hearing from you

Kind Regards,
Priyanshu Rajput

https://drive.google.com/file/d/165jQ5R4CPQN6Kk5fVuMavIhFQj1AYLmv/view?usp=sharing
"""
    msg["To"] = [str(st) for st in email.split(' ') if st]
    msg.set_content(message)
    try:
        server.send_message(msg)
        print(f'Mail sent to {email}')
    except Exception as e:
        print(f'An error occurred while sending email to {email}:', e)
        break
    del msg
    time.sleep(5)
    # break


server.quit()
