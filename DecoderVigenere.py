#!/usr/bin/python
# -*- coding: utf-8 -*-

print (""" 
╔═╗╔═╗╔═══╗╔════╗╔════╗╔╗─╔╗╔═══╗──────     ╔═══╗╔═══╗╔╗──╔╗╔═══╗╔═══╗
║║╚╝║║║╔═╗║║╔╗╔╗║║╔╗╔╗║║║─║║║╔══╝──────     ║╔═╗║║╔═╗║║╚╗╔╝║║╔═╗║║╔══╝
║╔╗╔╗║║║─║║╚╝║║╚╝╚╝║║╚╝║╚═╝║║╚══╗╔╗╔╗╔╗     ║╚═╝║║╚═╝║╚╗╚╝╔╝║║─╚╝║╚══╗
║║║║║║║╚═╝║──║║────║║──║╔═╗║║╔══╝║╚╝╚╝║     ║╔══╝║╔╗╔╝─╚╗╔╝─║║─╔╗║╔══╝
║║║║║║║╔═╗║──║║────║║──║║─║║║╚══╗╚╗╔╗╔╝     ║║───║║║╚╗──║║──║╚═╝║║╚══╗
╚╝╚╝╚╝╚╝─╚╝──╚╝────╚╝──╚╝─╚╝╚═══╝─╚╝╚╝─     ╚╝───╚╝╚═╝──╚╝──╚═══╝╚═══╝ 
______________________________________________________________________
\n""")    
print "Script criado por MATTHEW PRYCE\n"
print "YouTube: https://www.youtube.com/channel/UCil0gtkIVAGQ82HVahqpZ8A\n"
print "Facebook: https://www.facebook.com/profile.php?id=100016244164478\n"


plaintext   = raw_input("Digite o texto Encriptado: ").upper()
key         = raw_input("Digite a chave: ").upper()

if len(key) == 0:
    print "A chave deve ter um comprimento igual ou superior a 1."; exit()
if not plaintext.isalpha() or not key.isalpha():
    print "Entrada e chave devem ser compostas apenas por letras."; exit()

crypt = ''
decrypt = ''
for n in range(0, len(plaintext)):
    new = ord(plaintext[n]) + ord(key[n%len(key)]) - 65
    if new > 90:
        new -= 26
    crypt += chr(new)
    new = ord(plaintext[n]) - ord(key[n%len(key)]) + 65
    if new < 65:
        new += 26
    decrypt += chr(new)


print "Texto Decifrado é: " + decrypt

