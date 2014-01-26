# Hardware

LightRider Board

How it works

* Raspberry Pi
  * GPIOs
* LightRider
* * ["NightRider" Lights](http://www.raspberrypi-spy.co.uk/2012/06/knight-rider-cylon-lights-for-the-raspberry-pi/)
* * [Darlington Arrays](http://www.petervis.com/Raspberry_PI/Raspberry_Pi_GPIO_Header/Raspberry_Pi_GPIO_Header_Pin_Interfacing.html) with Raspebrry Pi and LEDs
* * Resistor Arrays
* * * Link
* * * Buttons
* Power
  * For all lights on we will need about 250mA
    * 12 x White LEDs 14mA 
    * 4 x LEDs red, green, orange and yellow about 10mA each
    * 12 x 14 + 4 * 10 = 168 + 40 = 208mA i add some "buffer" so 250mA should be safe
    * USB Ports may supply up to 500mA while all my tests i used a onboard USB port from my desktop pc without problems  or deep-fry the port
  * Some 5V/500mA USB port (not Pi recommend, could work i'm not trying it)
  * "old" Raspberry Pi Powersupply thats what i use 5V/1000mA Raspberry Pi powersupply. This safty costs about 3€.

### Breadboard Layout
![Breadboard Layout](https://raw2.github.com/thomaskneisel/LightRider/master/docs/images/Light%20Rider_Steckplatine.png)
### Circuit diagram
![Circuit diagram](https://raw2.github.com/thomaskneisel/LightRider/master/docs/images/LightRider_Schaltplan.png "")

### Circuit diagram without Raspbery Pi
![Circuit diagram Pi-less](https://raw2.github.com/thomaskneisel/LightRider/master/docs/images/Light Rider_RPi_free_Schaltplan.png "")

### Complete fritzing layout
[fritzing layout](https://github.com/thomaskneisel/LightRider/blob/master/docs/fritzing/LightRider.fzz "")

## Hardware List

* comming soon ... see images so long

