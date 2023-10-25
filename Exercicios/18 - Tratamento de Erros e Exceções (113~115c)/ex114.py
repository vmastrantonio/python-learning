import urllib.request

try:
    site = urllib.request.urlopen("http://pudim.com.br/")
except:
    print("O site Pudim não está acessível no momento.")
else:
    print("O site Pudim está acessível.")