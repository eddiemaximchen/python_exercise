#DimmerSwitch class

class DimmerSwitch():
    def __init__(self):
        self.switchIson=False
        self.brightness=0
    
    def turnOn(self):
        self.switchIson=True

    def turnOff(self):
        self.switchIson=False
        self.brightness=0

    def raiseLevel(self):
        if self.brightness<10 and self.switchIson==True:
            self.brightness=self.brightness+1

    def lowerLevel(self):
        if self.brightness>0:
            self.brightness=self.brightness-1

    def show(self):
        print('Switch mode: ',self.switchIson)
        print('Brightness is ',self.brightness)

if __name__ == '__main__':
    Dimmer=DimmerSwitch()
    Dimmer.turnOn()
    Dimmer.raiseLevel()
    Dimmer.raiseLevel()
    Dimmer.raiseLevel()
    Dimmer.raiseLevel()
    Dimmer.raiseLevel()
    Dimmer.show()
    Dimmer.turnOff()
    Dimmer.show()
    Dimmer.raiseLevel()
    Dimmer.show()
    Dimmer.turnOn()
    Dimmer.raiseLevel()
    Dimmer.show()
