"""This program shows the URL with more results"""
# -*- coding: utf-8 -*-
import urllib
WORDS_URL1=[]
WORDS_URL2=[]
url1ingress = "https://es.wikipedia.org/wiki/Duda"
url2ingress = raw_input("Insert second URL")
url1 = urllib.urlopen(url1ingress)
url2 = urllib.urlopen(url2ingress)

palabra = raw_input("insert a word\n")
lines = url1.readline()
repetidas = 0
for line in lines:
  palabras = line.split(".")
  for p in palabras:
    if p in palabra:
      WORDS_URL1.append(palabra)
      repetidas = repetidas +1
print "la palabra \"%s\" se repite %s veces en el url%s"%(palabra,repetidas,url1ingress)
print WORDS_URL1.count(palabra)
print WORDS_URL1

raw_input("gii")
repetidas1= 0
lines1 = url2.readline()
for line in lines1:
  palabras = line.split(".")
  for p in palabras:
    if p in palabra:
      WORDS_URL2.append(palabra)
      repetidas1 = repetidas1 +1
print "la palabra \"%s\" se repite %s veces en el URL %s"%(palabra,repetidas1,url2ingress)
print WORDS_URL2.count(palabra)
print WORDS_URL2

raw_input("gii")
  