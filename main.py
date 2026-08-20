
from machine import ADC, Pin
import time
import neopixel


num_LED = 5
pixels = neopixel.NeoPixel(Pin(27), num_LED)

soil = ADC(Pin(26)) # Setting up the sensor by connecting to to GPIO pin 26 (ADC0)
value = soil.read_u16()
#Calibraton values
min_moisture= 200 # ADC reading in air (Dry)
max_moisture=35000 #ADC reading in water (wet)    
readDelay = 0.5 # time between readings
moisture_percent = 0

def getPercentage():
    moisture = (value - min_moisture) / (max_moisture - min_moisture) #Caclulates the percentage by finding
    if value - min_moisture != 0:
        moisture_percent = moisture * 100
    else:
        moisture_percent = 0      # Needed to prevent zerodivisible error

 

 
while True: # prints the reading
    getPercentage()

    if moisture_percent > 70:
        colour = (0, 0, 255) #sets colour to blue
    elif moisture_percent > 40 and moisture_percent < 70:
        colour = (0,255,0) # SEts colour to green
    elif moisture_percent > 20 and moisture_percent < 40:
        colour = (255,255,0) #Sets colour to yellow
    else:
        colour = (255,0,0)

    pixels.fill(colour)
    pixels.write()

    print(f"Moisture: {moisture_percent}%" + "  Value: " + str(value)) # Prints moisture levels (Temporary)
    time.sleep(readDelay) # set a delay between readings





    
colour = (0,0,0)
pixel.fill()
