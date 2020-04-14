from lib.menu import clear, menu
import lib.print as printMenu
import requests
import random

def mail():
    clear()
    API_KEY = input('Mail API: ')
    To = input('To: ')
    Subject = input('Subject: ')
    Message = input('Message: ')

    try:
        url = 'http://mail.kellis.fr/?key='+API_KEY+'&mail=simple'
        data = {
                'to':To,
                'subject':Subject,
                'message':Message
               }

        print ('Flood in progress. Type CTRL+C to stop flooding')

        r = requests.post(url = url, data = data)

        data2 = r.json()

        try:
            if (str(data2['code']) == '200'):
                pass
        except:
            clear()
            print ('An error has occurred')
            print ('Reason:')
            print ('    '+str(data2['error']['errors']['0']['reason']))
            print ('Message error:')
            print ('    '+str(data2['error']['message']))
            print ('Error code:')
            print ('    '+str(data2['error']['errors']['code']))
            input('Type ENTER to exit')
            clear()
            menu()
            print (printMenu.mailMenu)
    except KeyboardInterrupt:
        clear()
        menu()
        print (printMenu.mailMenu)
            
def statMail():
    clear()
    menu()
    API_KEY = input('Mail API: ')

    url = 'http://mail.kellis.fr/stat.php?key='+API_KEY
    r = requests.get(url)
    data2 = r.json()
    try:
        data = """
 "id"=>"%s"
 "name"=>"%s"
 "mailLimit"=>"%s"
 "differentMailLimit"=>"%s"
 "expiration"=>"%s"
 "mail"=>"%s"
        """ % (
            str(data2['id']),
            str(data2['name']),
            str(data2['mailLimit']),
            str(data2['differentMailLimit']),
            str(data2['expiration']),
            str(data2['mail'])
        )

        print (data)
        input('Type ENTER to exit')
        clear()
        menu()
        print (printMenu.mailMenu)
    except:
        clear()
        print ('An error has occurred')
        print ('Reason:')
        print ('    '+str(data2['error']['errors']['0']['reason']))
        print ('Message error:')
        print ('    '+str(data2['error']['message']))
        print ('Error code:')
        print ('    '+str(data2['error']['errors']['code']))
        input('Type ENTER to exit')
        clear()
        menu()
        print (printMenu.mailMenu)