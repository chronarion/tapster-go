import zerorpc
import time
FLOAT_HEIGHT = -140
PRESS_HEIGHT = -160
PRESS_DURATION = 0.15
NAV_X = 22 
NAV_Y = 30
BALL_X = -3
BALL_Y = -45


c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")
print c.hello("RPC")

#c.go(-30,-45,-130) # bottom left
#time.sleep(2)
#c.go(30,50,-130) # top right

#time.sleep(2)
#c.go(-30,50,-130) # top left

#time.sleep(2)
#c.go(30,-45,-130) # bottom right

# nav button
c.go(NAV_X, NAV_Y, FLOAT_HEIGHT)
time.sleep(1)
c.go(NAV_X, NAV_Y, PRESS_HEIGHT)
time.sleep(PRESS_DURATION)
c.go(NAV_X, NAV_Y, FLOAT_HEIGHT)
time.sleep(1)

# 0, -55, -150 for nav button?
c.go(BALL_X, BALL_Y, FLOAT_HEIGHT)
time.sleep(1)
c.go(BALL_X, BALL_Y, PRESS_HEIGHT)
time.sleep(PRESS_DURATION)
c.go(BALL_X, BALL_Y, FLOAT_HEIGHT)
time.sleep(1)
