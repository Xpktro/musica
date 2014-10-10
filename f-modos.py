#coding:utf-8
import math
import struct
import wave

from utils import rotate

raiz_doceava_de_dos = 2 ** (1.0/12)

actual = 220.0
frecuencias = [actual]
for i in range(50):
    actual *= raiz_doceava_de_dos
    frecuencias.append(actual)

TONO = 2
SEMITONO = 1

notas = []
modo = [TONO, TONO, SEMITONO, TONO, TONO, TONO, SEMITONO]
inicio = 0

# Existen 8 modos, se obtienen rotando los intervalos de la escala
for i in range(8):
    actual = inicio
    frecuencias_modo = [frecuencias[actual]]

    for intervalo in modo:
        actual += intervalo
        frecuencias_modo.append(frecuencias[actual])

    notas += frecuencias_modo
    inicio += modo[0]

    modo = rotate(modo)


muestras_por_segundo = 44100
duracion = 0.5

muestras_totales = duracion * muestras_por_segundo

muestras = []

for frecuencia in notas:
    ciclos_por_muestra = frecuencia / muestras_por_segundo
    incremento = 2 * math.pi * ciclos_por_muestra
    fase = 0

    for i in range(int(muestras_totales)):
        muestra = math.sin(fase)
        fase += incremento
        muestras.append(muestra)


nombre_archivo = 'f.wav'
archivo = wave.open(nombre_archivo, 'w')
archivo.setparams((1, 2, muestras_por_segundo, 0, 'NONE', 'not compressed'))

valores = []
for muestra in muestras:
    valor_bit = struct.pack('h', muestra * 32767)
    valores.append(valor_bit)

valores_str = ''.join(valores)
archivo.writeframes(valores_str)
archivo.close()
