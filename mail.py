import re
from time import sleep
from tempmailx import TempMail

mail = TempMail()
print(f"Email: {mail.email}")

while True:
    emails = mail.fetch_emails()

    for email in emails:
        data = email.fetch_data()
        data = str(data)

        code = re.findall("[0-9]+\d{5,6}", data)[-1]

        print(f"Code: {code}")
    
    print("Aguardando novos emails ...")
    sleep(5)
