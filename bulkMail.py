import smtplib, ssl, csv

def sendMail(f, smail, spass, ssub, msg):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = smail  # Enter your address
    password = spass
    SUBJECT = ssub  
    TEXT = msg
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    context = ssl.create_default_context()

    # Keep all the emails from CSV in array
    
    with open(f) as file:
        mailList = []
        count = 0
        reader = csv.reader(file)
        next(reader)  
        for value in reader:
            mailList.append(value[0].strip())
            count = count + 1
    

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        # print('Successfully logged in')
        server.sendmail(sender_email, mailList, message)
        # print('Successfully Sent in')
    return count