#coding:utf-8
import math
import struct
import wave

# El número de oscilaciones por segundo de la señal
frecuencia = 440.0

# Cuántos puntos de la onda se reproducirán por segundo
muestras_por_segundo = 44100

# El tiempo que la onda oscilará
duracion = 1.0

muestras_totales = duracion * muestras_por_segundo

# Se define la fracción de onda a avanzar por cada muestra
ciclos_por_muestra = frecuencia / muestras_por_segundo
# Y se escala al periodo de la onda a generar
incremento = 2 * math.pi * ciclos_por_muestra
fase = 0

muestras = []

for i in range(int(muestras_totales)):
    # Añadimos cada una de las cantidades calculadas a una lista
    muestra = math.sin(fase)
    fase += incremento
    muestras.append(muestra)


nombre_archivo = 'a.wav'
archivo = wave.open(nombre_archivo, 'w')

# Inicializamos el archivo de sonido (1 canal, 2 bytes)
archivo.setparams((1, 2, muestras_por_segundo, 0, 'NONE', 'not compressed'))

valores = []
for muestra in muestras:
    # Añadimos los bytes de cada una de las muestras, escalados a 16 bits
    # que es el objetivo de struct.pack
    valor_bit = struct.pack('h', muestra * 32767)
    valores.append(valor_bit)

# Concatenamos todos los valores en un único string que se escribe
valores_str = ''.join(valores)
archivo.writeframes(valores_str)
archivo.close()
