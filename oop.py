#inheritance
class product:
    name:str
    price:int

    def __init__(self,name:str,price:int):
        self.name=name
        self.price=price

class food(product):
    def __init__(self, name: str, price: int):
        super().__init__(name, price)

class Notebook(product):
    def __init__(self, name: str, price: int):
        super().__init__(name, price)

    #encapsulation
    def __sleep(self):
        print('you can not access me')

if __name__=="__main__":
    shopping_list=[]

    #polymorphism
    nb1 = Notebook(name="Asus",price=30000)
    nb2 = Notebook(name="Asus",price=20000)
    f1 = food(name="cookie",price=200)

    shopping_list.append(nb1)
    shopping_list.append(nb2)
    shopping_list.append(f1)

    all_bill=0
    for item in shopping_list:
        all_bill=all_bill+item.price
    print("all_bill=%d"%all_bill)
    nb_bill=0
    for item in shopping_list:
     if (isinstance(item,Notebook)):
       nb_bill = nb_bill+item.price
    print("nb bill is %d"%nb_bill) 
 
