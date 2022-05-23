Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> preço= float(input('Qual é o preço do produto? R$'))
novo= preço - (preço*5/100)
print('O produto que custava {:.2F}R$ na promoção com desconto de 5% vai custar {:.0f}R$'.format(preço , novo))