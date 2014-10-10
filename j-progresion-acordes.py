import math
import struct
import wave

from utils import grouper, rotate

raiz_doceava_de_dos = 2 ** (1.0/12)

actual = 220.0
frecuencias = [actual]
for i in range(50):
    actual *= raiz_doceava_de_dos
    frecuencias.append(actual)

TONO = 2
SEMITONO = 1

acordes = []
escala = [TONO, TONO, SEMITONO, TONO, TONO, TONO, SEMITONO]


inicio = 0
for x in range(8):
    actual = inicio
    notas = [frecuencias[actual]]
    for grupo in grouper(escala, 2, 0):
        actual += sum(grupo)
        notas.append(frecuencias[actual])

    acordes.append(notas)
    inicio += escala[0]

    escala = rotate(escala)


I, II, III, IV, V, VI, VII = range(7)

# Todas las canciones pop en existencia
acordes_cancion = (acordes[I], acordes[V], acordes[VI], acordes[IV], acordes[I])

muestras_por_segundo = 44100
duracion = 2

muestras_totales = duracion * muestras_por_segundo

muestras = []

for indice, acorde in enumerate(acordes_cancion):
    inicio_acorde = indice * duracion * muestras_por_segundo

    for frecuencia in acorde:
        ciclos_por_muestra = frecuencia / muestras_por_segundo
        incremento = 2 * math.pi * ciclos_por_muestra
        fase = 0

        for i in range(int(muestras_totales)):
            if inicio_acorde + i == len(muestras):
                muestras.append(0)
            muestras[inicio_acorde + i] += math.sin(fase)
            fase += incremento


maximo = max([abs(muestra) for muestra in muestras])
multiplicador = 1.0 / maximo
muestras = [multiplicador * muestra for muestra in muestras]

nombre_archivo = 'j.wav'
archivo = wave.open(nombre_archivo, 'w')
archivo.setparams((1, 2, muestras_por_segundo, 0, 'NONE', 'not compressed'))

valores = []
for muestra in muestras:
    valor_bit = struct.pack('h', muestra * 32767)
    valores.append(valor_bit)

valores_str = ''.join(valores)
archivo.writeframes(valores_str)
archivo.close()
