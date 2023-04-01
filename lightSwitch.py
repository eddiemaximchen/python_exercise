class lightSwitch():
    def __init__(self):
        self.switchIsOn=False
    
    def turnOn(self):
        self.switchIsOn=True

    def turnOff(self):
        self.switchIsOn=False
    
    def show(self):
        print(self.switchIsOn)

if __name__ == '__main__':
    LightBoob=lightSwitch() #建立一個lightswitch物件
    
    LightBoob.show()
    LightBoob.turnOn()
    LightBoob.show()
    LightBoob.turnOff()
    LightBoob.show()