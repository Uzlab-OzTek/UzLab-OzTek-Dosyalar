import RPi.GPIO as pin

pin.setwarnings(False)
pin.cleanup()

pin.setup(26,pin.OUT)
pin.setup(19,pin.OUT)
pin.setup(13,pin.OUT)

pin.setup(2,pin.IN)
pin.setup(3,pin.IN)
pin.setup(4,pin.IN)
