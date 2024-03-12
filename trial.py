import requests
from requests.exceptions import SSLError

def checkHTTPOrS(url):
    custom_headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    try:
        response = requests.get(url, headers=custom_headers)
    except SSLError:
        return False
    headers = response.headers

    httpOrS = headers.get('alt-svc') or headers.get('Alt-Svc')
    return "443" in httpOrS if httpOrS else False

if __name__ == '__main__':
    links = ['http://testphp.vulnweb.com/login.php', 
             'http://httpforever.com/',
             'https://www.google.com',
             'http://www.google.com',
             'https://www.youtube.com/',
             'https://www.instagram.com',
             'https://www.facebook.com']

    for url in links:
        print(f"Url: {url}\n HTTPS? : {checkHTTPOrS(url)} ")
