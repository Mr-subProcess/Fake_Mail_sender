import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#sender and receiever information

sender="Sender Mail"
receiever="Receiever Mail"
subject="subject"
message="Your message"

#Mail SMTP Server İnformation
smtp="smtp.gmail.com"
port=587
password="your password"


file_path=""#if you are not going to add a file path, leave it blank


#Creatw Mail object
mail = MIMEMultipart()
mail['From']=sender
mail['To']=receiever
mail['Subject']=subject

mail.attach(MIMEText(message, 'plain'))

def main():
    try:
        if  file_path:
            with open(file_path, "rb") as dosya:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(dosya.read())
                encoders.encode_base64(part)  # Dosyayı base64 olarak şifrele
                part.add_header('Content-Disposition', f'attachment; filename={file_path}')
        
                # Dosyayı e-postaya ekle
                mail.attach(part)







        server = smtplib.SMTP(smtp, port)
        server.starttls()  # TLS bağlantısı başlat
        server.login(sender, password)
        server.sendmail(sender, receiever, mail.as_string())
        print("Mail has been sent")
    except Exception as e:
        print("Error :" ,e)

main()

