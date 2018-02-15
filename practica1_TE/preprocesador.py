import nltk
import os
import sys

from nltk.tag.util import str2tuple
from nltk.tag.util import untag
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize


path = os.getcwd() #Obtengo ruta absoluta
rutasArchivos = []
print('Bienvenido, Pre-Procesador. Autor: Manuel Tolentino - (20120467)')

### 1.1) TODO TERMINAR FUNCION
def tokenizacion(archivo):
    # Tokens
    palabras = nltk.word_tokenize(archivo.read())


    palabraSucias = []

    for palabra in palabras:
        palabraSucias.append(str2tuple(palabra))
        # print(palabraSucias)

    textoLimpio = untag(palabraSucias)

    # Borro los signos de puntuacion
    textoLimpio = [palabra for palabra in textoLimpio if len(palabra) > 1]
    #
    # for texto in textoLimpio:
    #     if (texto == '``'):
    #         textoLimpio=textoLimpio.remove(texto)

    for palabra in textoLimpio:
        palabra.lower()
    return textoLimpio
### 1.2)
def stopwords(tokens):
    stopwords = set(nltk.corpus.stopwords.words('english'))  # StopWords Configuracion
    noStopwwords=[]
    for palabra in tokens:
        noStopwwords.append(palabra.lower())

    palabras = [palabra for palabra in noStopwwords if palabra not in stopwords]
    return palabras
### 1.3)
def raices_Porter(tokens):
    raices = []
    ps = PorterStemmer()
    for word in tokens:
        raices.append(ps.stem(word))
    return raices



def opciones(opcionArchivo):
    print('Ruta archivo seleccionado: ' + rutasArchivos[opcionArchivo - 1])
    ruta = rutasArchivos[opcionArchivo - 1]

    file = open(ruta, 'r')



    print('1.Tokenizacion')
    print('2.Escribir archivo')
    opcion=int(input('Seleccione una opcion:'))


    if(opcion==1):
        tokens = tokenizacion(file)
        print(tokens)
        print('Tokenizacion realizada!')


        print('Opciones:')
        print('1.Eliminar StopWords')
        print('0.Salir')
        opcion=int(input('Seleccione una opcion:'))

        if(opcion==1):
            noStopwords = stopwords(tokens)
            print(noStopwords)
            print('Stopwords eliminados!')

            print('Opciones:')
            print('1.Extraer raices de cada término')
            print('0.Salir')
            opcion = int(input('Seleccione una opcion:'))

            if (opcion == 1):
                print(raices_Porter(noStopwords))
                print('Raices de cada termino.')

        elif (opcion == 0):
            sys.exit()

    elif(opcion==2):
        palabras = stopwords(tokenizacion(file))

### 1.4)
        contadorPalabras = 0
        for palabra in palabras:
            contadorPalabras += 1
        print('Total de palabras: ' + str(contadorPalabras))

        fdist = nltk.FreqDist(palabras)

### 1.5)
        contadorPalabrasUnicas = 0
        for palabra in fdist:
            contadorPalabrasUnicas += 1
        print('Total de palabras únicas: ' + str(contadorPalabrasUnicas))

### 1.6)
        print('50 palabras mas frecuentes:')
        for palabra, frequency in fdist.most_common(50):
            print(u'{}={}'.format(palabra, frequency))

### 1.8)
        with open('salida.txt', 'a') as salida:
            salida.write('SALIDA DEL PROGRAMA PRE-PROCESADOR:\n\n')
            salida.write('Total de palabras de la colección:'+str(contadorPalabras)+'\n')
            salida.write('Total de palabras unicas (Vocabulario):'+str(contadorPalabrasUnicas)+'\n\n')
            salida.write('Palabras frecuentes:\n')
            contador=1
            for palabra, frequency in fdist.most_common(50):
                salida.write(str(contador)+'. ')
                salida.write(u'{}={}'.format(palabra, frequency))
                salida.write('\n')
                contador+=1



    elif(opcion==0):
        sys.exit()

    # else:
    #     print('\n\n\nOpcion no existe!\n')
    #     opciones(opcionArchivo)

def menuArchivos():
    print('OPCION #1')
    contador = 0
    print('\nListado de archivos:')

    # Guardo las rutas de cada archivo dentro de la carpeta indicada por parámetro
    for filename in sorted(os.listdir(str(sys.argv[1]))):
        contador += 1
        print(str(contador) + '. ' + filename)
        # print('Ruta del archivo:'+path+'/'+str(sys.argv[1])+filename)
        rutasArchivos.append(path + '/' + str(sys.argv[1]) + filename)
        # file = open(path+'/'+str(sys.argv[1])+filename,'r')
        # print(file.read())
    print('0. Volver atras')
    opcionArchivo = int(input('Seleccione el archivo que desea trabajar:'))


    if(1 <= opcionArchivo and opcionArchivo<=contador ):
        opciones(opcionArchivo)

    elif(opcionArchivo == 0):
        print('\n\n')
        menu()

### 1.7) Programa principal, secuencia de pasos
def menu():

    print('Menu:')
    print('1. Buscar archivos')
    print('2. Salir')

    opcion=input('Seleccione una opcion:')

    if(opcion=='1'):
        menuArchivos()



    elif(opcion=='2'):
        sys.exit()



    else:
        print('\nOpcion inválida!\n\n')
        menu()


menu()









