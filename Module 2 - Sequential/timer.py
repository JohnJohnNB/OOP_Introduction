segundos = int(input())

h = int(segundos/3600)
m = int((segundos - (h*3600))/60)
s = int(segundos - (h*3600+m*60))


print("{}:{}:{}".format(horas, minutos, segundos2))