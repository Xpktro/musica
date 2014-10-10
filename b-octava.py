#coding:utf-8
import math
import struct
import wave

# Las octavas de una frecuencia se obtienen doblándola o reduciéndola a la
# mitad
frecuencias = [220.0, 440.0, 880.0]
muestras_por_segundo = 44100
duracion = 1.0

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


nombre_archivo = 'b.wav'
archivo = wave.open(nombre_archivo, 'w')
archivo.setparams((1, 2, muestras_por_segundo, 0, 'NONE', 'not compressed'))

valores = []
for muestra in muestras:
    valor_bit = struct.pack('h', muestra * 32767)
    valores.append(valor_bit)

valores_str = ''.join(valores)
archivo.writeframes(valores_str)
archivo.close()
