# Assesment Task 2
##### By Mazen Nassar

## Requirements Outline

 ### The Need
    My family has recently gotten into growing and nurturing plants. A major part of growing plants is giving them sufficient water and making sure they they dont drown or shrivel up. Due to everyday life, sometimes the plant goes forgotten for long periods of time.


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
The purpose of this test was to collect data on the sensor reading in air (In dry conditions) and in a cup of water (100% wet). In a perfect world (Ideal Conditions) the reading for when the sensor is in the air should have been ~0 and for when the sensor is in water should be ~45000. However when I ran the code printing the ADC value when it was dry it was  ~200 and the value when wet was ~36,000 so using this data I calibrated the values for wet and dry in my code to ensure accurate readings and therefore accurate moisture level percentages.


Another issue I encountered during this intial test was the percentage conversion was stuck at 0.8-0.9% even when the sensor was dipped in water, upon further inspection I realised while my sensor is a resistive sensor meaning it checks for moisture by sensing voltage, becuase air is an insulator and water is a conducter, the amount of voltage which passes through is directly reliant on the water level, the specific model I have made by [keyestudio](https://wiki.keyestudio.com/Ks0049_keyestudio_Soil_Humidity_Sensor#Sample_Code_2) has already solved the problem of inverting the values.
The code below was the code I was using to calculate the percentage
```
 moisture = (min_moisture - value) / (min_moisture - max_moisture)
 moisture_percent = moisture * 100
```
 
