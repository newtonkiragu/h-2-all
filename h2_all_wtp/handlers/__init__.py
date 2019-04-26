import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
from handlers.sim800l_handler import SIM800L
from handlers.simple_data_handler import SimpleDataHandler
from handlers.water_handlers import Valve,Waterflow
