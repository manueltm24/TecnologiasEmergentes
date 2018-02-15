import nltk
from nltk.tag.util import str2tuple
from nltk.tag.util import untag
from nltk.tag.util import tuple2str



textoSucio = 'It/pps recommended/vbd that/cs Fulton/np legislators/nns act/vb ``/`` to/to have/hv these/dts laws/nns studied/vbn and/cc revised/vbn to/in the/at end/nn of/in modernizing/vbg and/cc improving/vbg them/ppo ''/'' ./.'
palabras = nltk.word_tokenize(textoSucio)
palabraSucias=[]

for palabra in palabras:
    palabraSucias.append(str2tuple(palabra))
    # print(palabraSucias)

textoLimpio= untag(palabraSucias)


textoLimpio = [palabra for palabra in textoLimpio if len(palabra) > 1]


for texto in textoLimpio:
    if(texto=='``'):
        textoLimpio.remove(texto)


# stopwords = set(nltk.corpus.stopwords.words('english'))  # StopWords Configuracion
# textoLimpio = [palabra for palabra in textoLimpio if palabra not in stopwords]

print(textoLimpio)

