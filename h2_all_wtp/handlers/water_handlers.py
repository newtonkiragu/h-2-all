from handlers import GPIO

class Valve:
	def __init__(self,pin=18):
		self.map={True:GPIO.HIGH,False:GPIO.LOW}
		self.pin=pin
		GPIO.setup(self.pin,GPIO.OUT)
                self.state=True
		GPIO.output(self.pin,self.map[self.state])

	def toggle(self):
		self.state= not self.state
		GPIO.output(self.pin,self.map[self.state])

	on=lambda self:GPIO.output(self.pin,GPIO.LOW)
	off=lambda self:GPIO.output(self.pin,GPIO.HIGH)


class Waterflow:
	def __init__(self, flow_pin=16, verbose=False):
		self.count = 0
		self.verbose = False
		self.water_flow = 0 

		GPIO.setup(flow_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		GPIO.add_event_detect(flow_pin, GPIO.FALLING, callback=self.count_pulse)

	def count_pulse(self, channel):
		self.count += 1
		self.water_flow = self.count / 450
