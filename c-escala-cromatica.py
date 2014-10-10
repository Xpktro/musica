#coding:utf-8
import math
import struct
import wave

# El semitono siguiente de una nota se obtiene multipicando su frecuencia por
# la raíz doceava de dos
raiz_doceava_de_dos = 2 ** (1.0/12)

# Existen 12 notas en una octava.
actual = 220.0
frecuencias = [actual]
for i in range(12):
    actual *= raiz_doceava_de_dos
    frecuencias.append(actual)

muestras_por_segundo = 44100
duracion = 0.5

muestras_totales = duracion * muestras_por_segundo

muestras = []

for frecuencia in frecuencias:
    ciclos_por_muestra = frecuencia / muestras_por_segundo
    incremento = 2 * math.pi * ciclos_por_muestra
    fase = 0

    for i in range(int(muestras_totales)):
        muestra = math.sin(fase)
        fase += incremento
        muestras.append(muestra)


nombre_archivo = 'c.wav'
archivo = wave.open(nombre_archivo, 'w')
archivo.setparams((1, 2, muestras_por_segundo, 0, 'NONE', 'not compressed'))

valores = []
for muestra in muestras:
    valor_bit = struct.pack('h', muestra * 32767)
    valores.append(valor_bit)

valores_str = ''.join(valores)
archivo.writeframes(valores_str)
archivo.close()
