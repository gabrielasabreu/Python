Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from datetime import date
atual= date.today().year
nasc= int(input('Qual o ano de nascimento? '))
idade= atual - nasc
print('Você que nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade== 18:
    print('Você precisa de alistar esse ano!')
elif idade < 18:
    saldo= 18 - idade
    print('Você ainda não está na idade de se alistar, espere {} para completar 18 anos!'.format(saldo))
    ano= atual+ saldo
    print('Seu alistamento será em {}'.format(ano))
else:
    idade > 18
    saldo= idade - 18
    ano= atual - saldo
    print('Você deveria ter se alistado há {} anos atrás! FAÇA O SEU ALISTAMENTO IMEDIATAMENTE!'.format(saldo))
    print('Seu alistamento deveria ser feito em {}'.format(ano))
