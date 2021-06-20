class myClass:
    def __init__(self, name):
        self.name = name

    def fun1(self, lastName):
        print(str(self.name + lastName))


x = myClass("Dodo")
x.fun1(" Wael")
x=5
if x != 4 and x != 3:
    print("hi")