from lib.menu import clear, menu
import lib.print as printMenu
import requests

def mail():
    clear()
    API_KEY = input('Mail API: ')
    To = input('To: ')
    Subject = input('Subject: ')
    Message = input('Message: ')
    From = input('From: ')
    i = int(0)

    while True:
        try:
            url = 'https://mail.kellis.fr?key'+API_KEY
            data = {'to':To,
                    'subject':Subject,
                    'message':Message,
                    'From':From}
            r = requests.post(url = url, data = data)

            if (r.text == 'yes'):
                i += 1
                print (str(i))
            else:
                print ('Not sent')
        except KeyboardInterrupt:
            clear()
            menu()
            print (printMenu.mailMenu)
            break
            