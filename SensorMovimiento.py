import RPi.GPIO as GPIO
import time
import csv
import json

# Definir el pin GPIO como 23
pir_gpio = 23

# Set up del GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_gpio, GPIO.IN)

#Funcion en caso de que no hay movimiento.
def no_motion():
    print("No hay movimiento.")

#Funcion en caso de que hay movimiento. 
def motion_detected():
    timestamp = time.ctime()
    print("***MOVIMIENTO DETECTADO***")

    #Guardar la información al archivo CSV
    with open('motion_data.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([timestamp, 'Movimiento detectado'])
                
try:
    while True:
        if GPIO.input(pir_gpio) == 0:
            no_motion()
        elif GPIO.input(pir_gpio) == 1:
            motion_detected()
        time.sleep(1)  

except KeyboardInterrupt:
    print('Programa detenido por el usuario.')
    GPIO.cleanup()
