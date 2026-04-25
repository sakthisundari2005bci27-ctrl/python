import urllib.request

def check_status(url):
    try:
        status_code = urllib.request.urlopen(url).getcode()
        if status_code == 200:
            print(f"{url} is ONLINE.")
    except:
        print(f"{url} is OFFLINE or invalid.")

# Add your websites here
sites = ["https://google.com", "https://github.com", "https://thissitedoesnotexist.com"]
for site in sites:
    check_status(site)
