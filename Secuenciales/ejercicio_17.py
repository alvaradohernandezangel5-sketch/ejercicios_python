# CalcularHoraLlegada

print("Hora de salida:")
horapartida = int(input())

print("Minutos de salida:")
minpartida = int(input())

print("Segundos de salida:")
segpartida = int(input())

print("Tiempo que has tardado en segundos:")
segviaje = int(input())

seginicial = horapartida * 3600 + minpartida*60 + segpartida;

segfinal = seginicial + segviaje;

minllegada = ((segfinal % 3600) / 60);
segllegada = (segfinal % 3600) % 60;

print("Hora de llegada")
horallegada = int(input())

print(horallegada,":",minllegada,":",segllegada)