import requests
import io

#url = "https://www.animekisa.vip/watch/sousei-no-onmyouji-dub-episode-1"

def web_page(url):

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0", 
        "Connection": "close", 
        "Prefer": "safe", 
        "Host": "www.animekisa.vip", 
        "Accept-Encoding": "gzip, deflate", 
        "Accept-Language": "en-US,en;q=0.5"
    }

    r = requests.request("GET", url, headers=headers)

    data = io.StringIO(r.text).readlines()
    search = 'id="iframe-to-load"'
    for line in data:
        if search in line:
            link = line

    
    link = link.split(" ")
    for i in link:
        if "src=" in i:
            video_link = i.split("=")[-1].replace('"','')
            break
	 

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0", 
        "Connection": "close", 
        "Referer": url, 
        "Prefer": "safe", 
        "Host": "ani.googledrive.stream", 
        "Accept-Encoding": "gzip, deflate", 
        "Accept-Language": "en-US,en;q=0.5"
    }

    r = requests.request("GET", video_link, headers=headers)
    data = io.StringIO(r.text).readlines()
    for line in data:
	    if '<source src=' in line:
		    links = line
		    break
    
    links = links.split(" ")
    for i in links:
        if "src=" in i and ".js" not in i:
            print("link  : "+i.replace('src=','').replace('&amp;','&').replace('"',''))
            