from glob import glob
import beta
import io
from sys import platform
from os import system
import requests


  

def new():
    list = glob('*.txt')
    url = input('Enter the Url : ')
    if url.split('/')[2] != 'www.animekisa.vip':
        print('[!]Not a proper url...')
        print('url should be like https://www.animekisa.vip/watch/anime_name or https://www.animekisa.vip/anime/anime_name')
    else:
        detail = "https://www.animekisa.vip/anime/"
        anime = url.split('/')[-1].split('-episode')[0]
        if (anime + '.txt') in list:
                if platform == 'win32':
                    system('del ' + anime + '.txt')
                elif platform == 'linux':
                    system('rm ' + anime + '.txt')
        r = requests.get(detail + anime)
        data = io.StringIO(r.text).readlines()
        search = '/watch/' + anime
        for line in data:
            if search in line:
                link = line.split(" ")[-1].split('=')[-1].replace('"','').replace('>\n','')
                w = open(anime + '.txt','a',encoding='utf-8')
                w.write(link + '\n')
                w.close()
        select(anime)
        
def select(anime):
    f = open(anime + '.txt', 'r', encoding = 'utf-8').readlines()
    ep_t = len(f)
    print('Total episodes are : ' + str(len(f)))
    num = input('Select Episode number : ')
    while True:
        try:
            int(num)
            if int(num) < 0 or int(num) > ep_t:
                print("[!] Enter from the list")
            else:
                url = f[int(num) - 1].replace('\n','')
                beta.web_page(url)
                break
        except ValueError:
            print('[!] Enter only Number')
        
        except:
            print('Something went wrong....')
        

def priv():
    list = glob("*.txt")
    total = len(list)
    if total == 0:
        return 0
    for i in range(1,(total + 1)):
        print(str(i) + " || " + list[i-1].replace(".txt",''))
    num = input("Anime Number : ")
    while True:
        try:
            int(num)
            if int(num) < 0 or int(num) > total:
                print("[!] Enter from the list")
            else:
                select((list[int(num) - 1].replace('.txt','')))
                break
        except ValueError:
            print('[!] Enter only Number')
        
        except:
            print('Something went wrong....')
         




while True:
    try:
        num = input(" 1 : List priv. anime\n 2 : Enter Url\n : ")
        if num == "":
            priv()
            break    
        int(num)
        if int(num) < 1 and int(num) > 2:
            print("[!]Enter From the Options")
        elif int(num) == 1:
            priv()
            break
        elif int(num) == 2:
            new()
            break
    except ValueError:
        print("Enter only number")
    except KeyboardInterrupt:
        print('Exiting...')
        break
    
    except:
        print("Something went Wrong...")  
    
        