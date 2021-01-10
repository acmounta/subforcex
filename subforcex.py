import requests

#target
domain = "google.com"

# open wordlist
wordlist = open("subdomains.txt")

# read wordlist
content = wordlist.read()

# split by a newline
subdomains = content.splitlines()

for sub in subdomains:
    #construct url
    url = f"https://{sub}.{domain}"
    try:
        #subdomian not live = error
        requests.get(url)
    except:
        #if error = pass
        pass
    else:
       print("[+]", url) 
