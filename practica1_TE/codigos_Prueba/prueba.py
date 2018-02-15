#!/usr/bin/env python

import nltk
import os
import sys
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

path = os.getcwd()
parametro = str(sys.argv[1])

#Clenning the text
def clean(fileString):

    fileString = re.sub('/[^\s]*', '', fileString)
    return fileString.lower()

#1.1 Toekenizar Texto
def tokenize(fileString):
    tokens = nltk.word_tokenize(fileString)
    return tokens

#1.2 StopWords
def mystopwords(fileString):

    stop_words = set(stopwords.words('english'))

    filtered_sentence = []

    for w in fileString:
        if w not in stop_words:
            filtered_sentence.append(w)

    fileString = filtered_sentence
    return filtered_sentence

#1.3 Raices
def porter_stemmer(fileString):
    ps = PorterStemmer()
    sentence = []

    for w in fileString:
        sentence.append(ps.stem(w))

    return sentence

#1.4 Numero de Palabras
# def contador_palaras(fileString):


#1.5 Cantidad terminos unicos

#1.6 50 palabras mas frecuentes

#1.7
for filename in os.listdir(parametro):
    file = open(path+'/'+parametro + '/' + filename, 'r')
    fileString = file.read()
    file.close()

    #Llamada a las funciones
    fileString = clean(fileString)
    fileString = tokenize(fileString)
    fileString = mystopwords(fileString)
    fileString = porter_stemmer(fileString)
    print(fileString)


#1.8