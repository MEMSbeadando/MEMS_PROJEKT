#!/usr/bin/python
from sense_hat import SenseHat #importaljuk a senshat konyvtarat
import time # ido konyvtar, hogz idozitest tudjunk csinalni
from datetime import datetime
import sys #valtozokhoz hozzaferes
from csv import writer #modulbeimportalas
import csv


sense = SenseHat() # kapcsolat a senshattel
sense.clear() #minden ledet takarit

try:
      while True:
          
           temp = sense.get_temperature()
           temp = round(temp - 10, 1) #10 fokkal korrigalom, mert magat meri nem a homersekletet
           print("Hom",temp) 

           humidity = sense.get_humidity()  
           humidity = round(humidity, 1)  
           print("Parat",humidity)  

           pressure = sense.get_pressure()
           pressure = round(pressure, 1)
           print("Legny",pressure)
           
           hour = str(datetime.now().strftime("%H:%M"))
           print(hour) 
            
           with open('adat.csv', 'a', newline='') as csvfile: #adat kiirasa a regi fajlba irva
                thewriter = csv.writer(csvfile)
                thewriter.writerow([hour,temp, humidity,pressure])
                csvfile.close()
                
           
           sense.show_message("Hom.: " + str(temp) + " C " + "Parat.:" + str(humidity) + " % " + "Legny.:" + str(pressure) + " hPa"
                              + "Ido: " + str(hour), scroll_speed=(0.08), back_colour= [0,0,0], text_colour= [187,10,48],)

           time.sleep(30) # mennyi idokozonkent fusson a kod
except KeyboardInterrupt:
      pass