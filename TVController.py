class TV():
    def __init__(self):
        self.isOn=False
        self.isMuted=False
        self.channelList=[2,4,5,7,9,11,20,36,44,54,65]
        self.nChannels=len(self.channelList)
        self.channelIndex=0
        self.VOLUME_MINIMUM=0   #常數
        self.VOLUME_MAXIMUM=10  #常數
        self.volume=5

    def power(self):
        self.isOn= not self.isOn #開關

    def volumeUP(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted=not self.isMuted
        if self.volume<self.VOLUME_MAXIMUM:
            self.volume=self.volume+1
    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            return
        if self.volume>self.VOLUME_MINIMUM:
            self.volume=self.volume-1
    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex=self.channelIndex+1
        if self.channelIndex == self.nChannels:
            self.channelIndex=0
    
    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex=self.channelIndex-1
        if self.channelIndex <0:
            self.channelIndex=self.nChannels-1 #最後一個頻道 頻道個數從0開始

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted
    
    def setChannel(self,channel):
        if channel in self.channelList: #確認有這個channel
            self.channelIndex=self.channelList.index(channel) #找出這個Channel的順序

    def showInfo(self):
        print()
        if self.isOn:
            print('Channel is ',self.channelList[self.channelIndex])
            if self.isMuted:
                print('TV is muted')
            else:
                print('TV volume: ',self.volume)
        else:
            print('TV is off')

if __name__ == '__main__':
    tv=TV()
    tv.power()
    tv.showInfo()
    tv.channelUp()
    tv.volumeUP()
    tv.showInfo()
    tv.setChannel(10)
    tv.showInfo()
    tv.channelDown()
    tv.channelDown()
    tv.volumeDown()
    tv.showInfo()
    tv.setChannel(4)
    tv.showInfo()
    tv.power()
    tv.showInfo()