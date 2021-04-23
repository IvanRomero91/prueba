hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

#1° lo hice así:
#horaMin=hora*59 #pasa horas a minutos
#total=(horaMin+min+dura) #suma todo en min
#horaFin=(horaMin+min+dura)//59 #divide los minutos en horas
#horaFin%=24 #para que las horas no pasen de 24
#minFin=(horaMin+min+dura)%60 #minutos que no llegan a una hora

#Después lo simplifiqué así:
horaFin=(((hora*59)+min+dura)//59)%24
minFin=((hora*60)+min+dura)%60

print('El evento terminará a las: ',horaFin,':',minFin,sep='')