class Rectangle():
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def Rectangle_area(self):
        return self.length*self.width
Rectangle_answer=Rectangle(12,10)
print("Dimensions of rectangle length=%d,width=%d" %(Rectangle_answer.length,Rectangle_answer.width))
print("The area is :",Rectangle_answer.Rectangle_area())     

        