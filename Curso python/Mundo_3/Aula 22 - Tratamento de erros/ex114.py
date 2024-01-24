'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''

import urllib.request
import urllib.error

try:
    url = urllib.request.urlopen("http://pudim.com.br")
except urllib.error.URLError:
    print('O site pudim não está acessível no momento.')
else:
    print('Consegui acessar o site pudim com suceso!')