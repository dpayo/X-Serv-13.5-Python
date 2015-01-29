#!/usr/bin/python
# -*- coding: utf-8 -*-

dic= {};
fich = open ('/etc/passwd', 'r');
list_lines = fich.readlines();
for line in list_lines:
    print line
    conf = line.split(':')
    user = conf[0]
    passw = conf[-1]
    dic = {user : passw}
    try:
        print dic['root']
        print dic ['imaginario']
    except KeyError:
        print ' No existe el usuario '
        break
        
        



