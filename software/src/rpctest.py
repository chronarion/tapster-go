import zerorpc
import time
FLOAT_HEIGHT = -140
PRESS_HEIGHT = -158
PRESS_DURATION = 0.12
PAUSE_DURATION = 0.5
SWIPE_WAIT = 0.2
POKESTOP_X = -15
POKESTOP_Y = -5
NAV_X = 22 
NAV_Y = 32
BALL_X = -3
BALL_Y = -49


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
#c.go(NAV_X, NAV_Y, FLOAT_HEIGHT)
#time.sleep(1)
#c.go(NAV_X, NAV_Y, PRESS_HEIGHT-4)
#time.sleep(PRESS_DURATION)
#c.go(NAV_X, NAV_Y, FLOAT_HEIGHT)
#time.sleep(1)

def reset():
  c.go(0,0,FLOAT_HEIGHT)

def pokestop():
  c.go(POKESTOP_X,POKESTOP_Y, FLOAT_HEIGHT)
  time.sleep(PAUSE_DURATION)
  c.go(POKESTOP_X, POKESTOP_Y, PRESS_HEIGHT)
  time.sleep(PRESS_DURATION)
  c.go(POKESTOP_X,POKESTOP_Y, FLOAT_HEIGHT)
  time.sleep(PAUSE_DURATION)

def menu():
  # 0, -55, -150 for ball?
  c.go(BALL_X, BALL_Y, FLOAT_HEIGHT)
  time.sleep(PAUSE_DURATION)
  c.go(BALL_X, BALL_Y, PRESS_HEIGHT+3)
  time.sleep(PRESS_DURATION)
  c.go(BALL_X, BALL_Y, FLOAT_HEIGHT)
  time.sleep(PAUSE_DURATION)

def swipe():
  c.go(-5,0,FLOAT_HEIGHT)
  time.sleep(PAUSE_DURATION)
  c.go(-5,0,PRESS_HEIGHT)
  time.sleep(SWIPE_WAIT)
  c.go(NAV_X,0,PRESS_HEIGHT)
  time.sleep(PAUSE_DURATION)
  c.go(NAV_X,0, FLOAT_HEIGHT)

for x in range (0,100):
  pokestop()
  time.sleep(PAUSE_DURATION)
  for x in range (0, 10):
    swipe()
    time.sleep(PAUSE_DURATION)
  menu()
  time.sleep(PAUSE_DURATION)

reset()
