def home():
    import os
    os.system("cls")
    import socket
    import pystyle
    from pystyle import Colors, Colorate
    import requests
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW('Made by Plasma')

    print(Colorate.Vertical(Colors.blue_to_cyan,'''                                 ('-.                    ('-. .-.   ('-.             .-. .-')     ('-.  _  .-')   
                                _(  OO)                  ( OO )  / _(  OO)            \  ( OO )  _(  OO)( \( -O )  
    ,--.      ,-.-')    ,------.(,------.         .-----. ,--. ,--.(,------.   .-----. ,--. ,--. (,------.,------.  
    |  |.-')  |  |OO)('-| _.---' |  .---'        '  .--./ |  | |  | |  .---'  '  .--./ |  .'   /  |  .---'|   /`. ' 
    |  | OO ) |  |  \(OO|(_\     |  |            |  |('-. |   .|  | |  |      |  |('-. |      /,  |  |    |  /  | | 
    |  |`-' | |  |(_//  |  '--. (|  '--.        /_) |OO  )|       |(|  '--.  /_) |OO  )|     ' _)(|  '--. |  |_.' | 
   (|  '---.',|  |_.'\_)|  .--'  |  .--'        ||  |`-'| |  .-.  | |  .--'  ||  |`-'| |  .   \   |  .--' |  .  '.' 
    |      |(_|  |     \|  |_)   |  `---.      (_'  '--'\ |  | |  | |  `---.(_'  '--'\ |  |\   \  |  `---.|  |\  \  
    `------'  `--'      `--'     `------'         `-----' `--' `--' `------'   `-----' `--' '--'  `------'`--' '--' 
    Version:                                                                                                    2.0
    »-----------------------------------------------•--------------------------------------------------------------«
    {1}IP INFO                                                                  {3}WEBSITE IP CHECKER 
    {2}HOST CHECKER                                                             {4}Credits '''))

    choice = input(Colorate.Vertical(Colors.blue_to_cyan,''' 
    -o>'''))









    def opt_1():

        def getipinfo(ip_address):
            url = f"http://ipinfo.io/{ip_address}/json"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                return None
        ip_address = input(Colorate.Horizontal(Colors.blue_to_cyan,'''    Ip address -> '''))
        ip_info = getipinfo(ip_address)

        if ip_info:
            print(Colorate.Horizontal(Colors.green_to_white,f'''\n     Coordinates: {ip_info.get('loc', 'N/A')}'''))
            print(Colorate.Horizontal(Colors.green_to_white,f'''     Hostname: {ip_info.get('hostname', 'N/A')}'''))
            print(Colorate.Horizontal(Colors.green_to_white,f'''     City: {ip_info.get('city', 'N/A')}'''))
            print(Colorate.Horizontal(Colors.green_to_white,f'''     Region: {ip_info.get('region', 'N/A')}'''))
            print(Colorate.Horizontal(Colors.green_to_white,f'''     Country: {ip_info.get('country', 'N/A')}'''))
            print(Colorate.Horizontal(Colors.green_to_white,f'''     Organization: {ip_info.get('org', 'N/A')}'''))
            input(Colorate.Horizontal(Colors.blue_to_cyan,'''\n    Press enter to Continue...'''))
            home()
        else:
            print(Colorate.Horizontal(Colors.blue_to_cyan,f'''    Unable to retrieve information for IP address: {ip_address}'''))
            input(Colorate.Horizontal(Colors.blue_to_cyan,'''    Press enter to Continue...'''))
            home()


    




    
    def opt_4():
        print(Colorate.Horizontal(Colors.red_to_yellow, '''    Made by ! Plasma [ kfsman ] '''))
        input(Colorate.Horizontal(Colors.blue_to_cyan,'''    Press enter to Continue...'''))
        home()





    


    def opt_2():
        def is_host_reachable(host, port):
            try:
                socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket_obj.settimeout(5)
                socket_obj.connect((host, port))

                return True
            except (socket.timeout, ConnectionRefusedError):
                return False
            finally:
                socket_obj.close()

        if __name__ == "__main__":
            host = input(Colorate.Horizontal(Colors.blue_to_cyan,'''    Enter the host or IP address to check: '''))
            port = int(input(Colorate.Horizontal(Colors.blue_to_cyan,'''    Enter the port to check: ''')))
        
            if is_host_reachable(host, port):
                print(Colorate.Horizontal(Colors.green_to_white,f'''\n    [+] {host}:{port} is reachable.\n'''))
                input(Colorate.Horizontal(Colors.blue_to_cyan,'''    Press enter to Continue...'''))
                home()
                
            else:
                print(Colorate.Horizontal(Colors.red_to_white,f'''\n    [-] {host}:{port} is not reachable.'''))
            input(Colorate.Horizontal(Colors.blue_to_cyan,'''\n    Press enter to Continue...'''))
            home()

    def opt_3():
        def get_ip_address(url):
            try:
                ip_address = socket.gethostbyname(url)
                return ip_address
            except socket.gaierror:
                return "Unable to resolve the host."

        if __name__ == "__main__":
            website_url = input(Colorate.Horizontal(Colors.blue_to_cyan,'''    Enter the website URL to check its IP address: '''))
        
            ip_address = get_ip_address(website_url)
            print(Colorate.Horizontal(Colors.green_to_white,f'''\n    The IP address of "{website_url}" is << {ip_address} >>'''))
            input(Colorate.Horizontal(Colors.blue_to_cyan,'''\n    Press enter to Continue...'''))
            home()



    if choice == "1":
        opt_1()       
    if choice == "4":
        opt_4()

    if choice == "2":
        opt_2()
    if choice == "3":
        opt_3()
    else:
        home()
home()
