import smtplib
from email.message import EmailMessage

'''TO make it more dynamic'''
from string import Template # refer notes
from pathlib import Path

            # file path          # reads data of the file
html = Path('./HTML/index.html').read_text()
wrap_name = Template(html) # remember we used $name

'''Make sure to turn on less secured apps in sender gmail account'''

'''we create a email object'''
email = EmailMessage()

''' we filled up email here '''
email['from'] = 'Nirmal'
email['to'] = 'firenirmal45@gmail.com'
email['subject'] = 'YOU WON a MACBOOK air m1 !!! :-D'

email.set_content(wrap_name.substitute({'name': 'Herby'}), 'html') # Now it parse to html


'''To send an email we communicate with smtp server'''
        # connects to the server
with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as smtp:
    smtp.ehlo() # It's part of protocol says hello to server

    '''smtp.starttls()  It does encryption connects securely to server it's only needed for port 587'''

                # email                    #password
    smtp.login('karurnirmal04@gmail.com', '13032004')

    ''' if you don't fill email use send_mail to fill details '''
    smtp.send_message(email)
    print('all done!!')
