from flask import Flask
from flask import request

import time
#import atexit

# Importiere die Adafruit PCA9685 Bibliothek
import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
#PCA9685_pwm = Adafruit_PCA9685.PCA9685(busnum=1)
PCA9685_pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 601  # Max pulse length out of 4096

FREQUENCY = 50
MIN_PULSE_WIDTH = 650
MAX_PULSE_WIDTH = 2350
DEFAULT_PULSE_WIDTH = 1500

# Set frequency to 100hz, good for l298n h-bridge.
PCA9685_pwm.set_pwm_freq(FREQUENCY)

# todo calculate offsets for 0 or 90 degree angle
# todo calculate min and max (maybe from PCA width inverse)

def arduino_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

# todo specify as params min and max and offset
def calculate_pca_pulse_width(angle_degrees):
    """
    degrees between 0-180 convert to between MIN_PULSE_WIDTH and MAX_PULSE_WIDTH for normal microsecond delay
    then convert to analog PCA9685 pulse width value
    """
    mapped_microsecond_delay = arduino_map(angle_degrees, 0, 180, MIN_PULSE_WIDTH, MAX_PULSE_WIDTH)
    print('mapped_microsecond_delay:', mapped_microsecond_delay)
    analog_value = int(float(mapped_microsecond_delay) / 1000000 * FREQUENCY * 4096)
    print(analog_value)
    return analog_value

print(calculate_pca_pulse_width(0))
print(calculate_pca_pulse_width(180))
#sys.exit()

# servo1 still moves at 120 so: 120 * 1000000 / 50 / 4096 = 585.93 is min?
# and 490 so 490 * 1000000 / 50 / 4096 = 2392.57

app = Flask(__name__)

@app.route("/")
def web_interface():
  html = open("index.html")
  response = html.read().replace('\n', '')
  html.close()
  return response

@app.route("/set_servo1")  
def set_servo1():  
  speed = request.args.get("speed")
  print("Received " + str(speed))
  PCA9685_pwm.set_pwm(0, 0, int(speed))
  return "Received " + str(speed)   
  
@app.route("/set_servo2")  
def set_servo2():  
  speed = request.args.get("speed")
  print("Received " + str(speed))
  PCA9685_pwm.set_pwm(1, 0, int(speed))  
  return "Received " + str(speed)  

@app.route("/set_servo3")  
def set_servo3():  
  speed = request.args.get("speed")
  print("Received " + str(speed))
  PCA9685_pwm.set_pwm(2, 0, int(speed))  
  return "Received " + str(speed) 

@app.route("/set_servo4")  
def set_servo4():  
  speed = request.args.get("speed")
  print("Received " + str(speed))
  PCA9685_pwm.set_pwm(3, 0, int(speed))  
  return "Received " + str(speed) 
 
@app.route("/set_servo5")  
def set_servo5():  
  speed = request.args.get("speed")
  print("Received " + str(speed))
  PCA9685_pwm.set_pwm(4, 0, int(speed))  
  return "Received " + str(speed) 

@app.route("/set_servo6")  
def set_servo6():  
  speed = request.args.get("speed")
  print("Received " + str(speed))
  PCA9685_pwm.set_pwm(5, 0, int(speed))  
  return "Received " + str(speed)   

@app.route("/set_servo7")  
def set_servo7():  
  speed = request.args.get("speed")
  print("Received " + str(speed))
  PCA9685_pwm.set_pwm(6, 0, int(speed))  
  return "Received " + str(speed)  

@app.route("/set_servo1_angle")
def set_servo1_angle():
  angle = request.args.get("angle")
  print("Received " + str(angle))
  pca_pulse_width = calculate_pca_pulse_width(int(angle))
  PCA9685_pwm.set_pwm(0, 0, int(pca_pulse_width))
  return "Received " + str(angle) + " converted to pulse width: " + str(pca_pulse_width)

@app.route("/set_servo2_angle")
def set_servo2_angle():
  angle = request.args.get("angle")
  print("Received " + str(angle))
  pca_pulse_width = calculate_pca_pulse_width(int(angle))
  PCA9685_pwm.set_pwm(1, 0, int(pca_pulse_width))
  return "Received " + str(angle) + " converted to pulse width: " + str(pca_pulse_width)

@app.route("/set_servo3_angle")
def set_servo3_angle():
  angle = request.args.get("angle")
  print("Received " + str(angle))
  pca_pulse_width = calculate_pca_pulse_width(int(angle))
  PCA9685_pwm.set_pwm(2, 0, int(pca_pulse_width))
  return "Received " + str(angle) + " converted to pulse width: " + str(pca_pulse_width)

@app.route("/set_servo4_angle")
def set_servo4_angle():
  angle = request.args.get("angle")
  print("Received " + str(angle))
  pca_pulse_width = calculate_pca_pulse_width(int(angle))
  PCA9685_pwm.set_pwm(3, 0, int(pca_pulse_width))
  return "Received " + str(angle) + " converted to pulse width: " + str(pca_pulse_width)

@app.route("/set_servo5_angle")
def set_servo5_angle():
  angle = request.args.get("angle")
  print("Received " + str(angle))
  pca_pulse_width = calculate_pca_pulse_width(int(angle))
  PCA9685_pwm.set_pwm(4, 0, int(pca_pulse_width))
  return "Received " + str(angle) + " converted to pulse width: " + str(pca_pulse_width)

@app.route("/set_servo6_angle")
def set_servo6_angle():
  angle = request.args.get("angle")
  print("Received " + str(angle))
  pca_pulse_width = calculate_pca_pulse_width(int(angle))
  PCA9685_pwm.set_pwm(5, 0, int(pca_pulse_width))
  return "Received " + str(angle) + " converted to pulse width: " + str(pca_pulse_width)
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8181, debug=True)
