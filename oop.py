#類別
class House:
    floor:int
    color:str

    def __init__(self,floor:int,color:str):
        self.floor=floor
        self.color=color
    def __str__(self):
        return f"This is a {self.floor} floor high {self.color} house."
house =House(floor=2,color="black")
print(house)
#繼承
class BaseHouse:
    floor:int
    color:str

    def __init__(self,floor:int,color:str):
        self.floor=floor
        self.color=color
    def __str__(self):
        return f"This is a {self.floor} floor high {self.color} house."    

class Apartment(BaseHouse):

    #overwrite
    def __str__(self):
        return f"This is a {self.floor} floor high {self.color} apartment."    

class Skyscraper(BaseHouse):
    #overwrite
    def __str__(self):
        return f"This is a {self.floor} floor high {self.color} skyscraper."

apartment = Apartment(floor=10, color="red")
skyscraper = Skyscraper(floor=100, color="gold")
print(apartment)
print(skyscraper)   