#!/usr/bin/python
# -*- coding: utf-8 -*-

fich=open("/etc/passwd","r")
num_usuarios=fich.readlines()
print "El numero de usuarios de este ordenador es: " + str(len(num_usuarios))
fich.close()

# Primera parte hecha

dicc = {}

fich=open("/etc/passwd","r")

for user in num_usuarios:
    
    conf = user.split(":");
    username = conf[0]
    shell = conf[-1][:-1]
    print "El usuario: *" + username + "* utiliza la shell: " + shell
    dicc[username] = shell
    #dicc[conf[0]]  = conf[-1][:-1]

print "root", dicc["root"]

fich.close()
