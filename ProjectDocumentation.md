# Assesment Task 2
##### By Mazen Nassar

## Requirements Outline

 ### The Need
 My family has recently gotten into growing and nurturing plants. A major part of growing plants is giving them sufficient water and making sure they they dont drown or shrivel up. Due to everyday life, sometimes the plant goes forgotten for long periods of time thus influencing the amount of water it recieves.


 ### Proposed Solution
 My proposed solution is to create a system which measure the level of moisture in the soil and then uses an rgb LED to output how high the moisture levels are with red indicating moisture levels between 0% and 20%, yellow between 21% and 40%, green indicating between 40% and 70%, blue indicating 70% and above 


 ### Key Actions
 + System accurately measures moisture level in the soil
 + System indicates the moisutre level using the rgb LED
 + System sets the rgb to red if plant needs more water to ensures its arrival



 ### Functional Requirements
   + When soil moisture levels fall under 20% the rgb LED turns red
   + When soil moisture levels are between 20% & 40% the rgb LED turns yellow to signal that the moisture level is getting better
   + When soil moisture levels are between


### Test Cases
| Test Case             | Input                                   | Expected Output   |
|----------             |----------                               |----------------   |
|Sufficient moisturae   | soil moisture sensor reads >40% & <70%  | LED turns Green   |
|Insufficient moisture  | soil moisture sensor reads <20%         | LED turns Red     |
|Excessive moisture     | soil moisture sensor reads >70%         | LED turns blue    | 


### Non-Functional Requirements
 + __Enclosure:__ I must make sure that the circuitry is suitably enclosed to survive harsh weather conditions such as  rain, wind or heat 
 + __Clean Circuitry:__ Clean presentable circuitry which minimises the space taken by the project




 ## Algorithm

### Flowchart
![image of flowchart](Mechatronics%20Flowchart%20Image.png)



 ### Pseudocode
   ```
   BEGIN too_much()
   clear_output()
   OUTPUT led(0,0,255)-(Colour blue)
   END too_much

   BEGIN not_enough()
   clear_output()
   OUTPUT led(255,0,0)-(Colour red)
   END not_enough
    
   BEGIN enough()
   clear_output()
   OUTPUT led(255,255,0)-(Colour yellow)
   END enough

   BEGIN healthy()
   clear_output()
   OUTPUT led(0,255,0)-(Colour green)
   END healthy()


BEGIN
      WHILE true
         READ moisture_levels
         IF moisture_level < 20
            not_enough()
         ELSE IF moisture_level < 40
            enough()
         ELSE IF moisture_level < 70
            healthy()
         ELSE
            too_much()
         ENDIF
      ENDWHILE
END

```

### Testing & Debugging
Moisture Sensor Test:

The Moisture sensor I was using  [keyestudio](https://wiki.keyestudio.com/Ks0049_keyestudio_Soil_Humidity_Sensor#Sample_Code_2) was a resistive sensor, meaning it sensed moisture levels by seeing how much voltage passes through the circuit. This works because water is a conducter meaning when the sensor is put in soil the voltage in the circuit is directly influenced by how much water there is in the soil to conduct the electricity. In a perfect world (Ideal Conditions) the ADC readings from the sensor in air should be ~0 and in water should be ~65,000.



As I ran my initial test I noticed that the ADC reading  from the sensor when I dipped it into a cup of water was maxing out at ~35,000, After carefully inspecting my code to ensure there were no software issues, a closer lok at the hardware caused me to realise the issue, my sensor was a 5V sensor while the raspberry pi pico pins can only handle up to 3.3V meaning the gpio pin can only output a max of 36,000 instead of 65,000. One "solution" includes supplying power for the sensor from the VBUS pin (Pin 40) however this risks overloading the pico's GPIO pin. To fix this I calibrated the wet value to ensure correct moisture readings:

```max_moisture = 65000``` -------->  ```max_moisture = 35000```

Another issue I encountered during this intial test was the percentage conversion was stuck at 0.8-0.9% even when the sensor was dipped in water, Seeing this I took a look at the code for calculating the percentage and realised because the code reading the value was outside the while loop it was only reading it once and outputing that. It was an easy fix with me putting the code inside of the while loop

LED light strip:
my project utilises the [lorikeet](https://piaustralia.com.au/products/little-bird-lorikeet-ws2812b-rainbow-board) which is a 5V sensor. I plugged the power wire into the VBUS pin. With this sensor however we will not run into issues such as the pico frying the board becuase the voltage is too high, this is becuase the LED strip isn't writing anything to the board. Then I connected the signal pin into GPIO pin 28 and the ground wire into a ground pin.

I ran into an issue when trying to make the light strip light up. In this code I was trying to set each pixel to the colour individually and it would refuse to run giving me an empty script. After some searching I found a solution courtesy of [Micropython Documentation Page](https://docs.micropython.org/en/latest/library/neopixel.html) which showed me I could just use fill()
```
    for i in range[num_LED]:
        pixels = colour
    pixels.write
```

``` fill() ```

After overcoming this issue the lights still would not turn on however after looking at my code I realised I had forgotten to add a parentheses when writing the colour data onto the LED strip

```pixels.write``` ----> ```pixels.write()```



## Evaluation:



