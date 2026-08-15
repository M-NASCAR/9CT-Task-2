
from machine import ADC, Pin
import utime
 
# use variables instead of numbers:
soil = ADC(Pin(26)) # Connect Soil moisture sensor data to Raspberry pi pico GP26 
 
#Calibraton values
min_moisture= 200 # ADC reading in air (Dry)
max_moisture=36000 #ADC reading in water (wet)       2200

value = soil.read_u16()
 
 
readDelay = 0.1 # time between readings
 
while True: # prints the reading
    moisture = (min_moisture - value) / (min_moisture - max_moisture)
    moisture_percent = moisture * 100
    # print values
    print("moisture: " + " " % moisture +"% (adc: "+ str(soil.read_u16())+")") 
    utime.sleep(readDelay) # set a delay between readings


    
