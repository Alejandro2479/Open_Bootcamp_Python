import time

hora_actual = time.localtime().tm_hour  # obtenemos la hora actual

if hora_actual >= 19:  # 19 es la hora en formato 24 horas
    print("¡Hora de ir a casa!")
else:
    # calculamos el tiempo que queda de trabajo
    minutos_restantes = (19 - hora_actual) * 60 - time.localtime().tm_min
    horas_restantes = minutos_restantes // 60
    minutos_restantes = minutos_restantes % 60
    print("Quedan {} horas y {} minutos para ir a casa".format(horas_restantes, minutos_restantes))
