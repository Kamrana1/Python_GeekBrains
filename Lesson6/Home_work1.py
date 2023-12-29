import time
class TrafficLight:

    def __init__(self):
        pass

    def running(self):
        while True:
            print("\rКрасный", end='' )
            time.sleep(7)
            print("\rЖелтый", end='')
            time.sleep(2)
            print("\rЗеленый", end='')
            time.sleep(7)

traf=TrafficLight()

traf.running()