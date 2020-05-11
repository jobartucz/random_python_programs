# define the Vehicle class
class Vehicle:

    def __init__(self, name = "", kind = "car", color = "", value = 0.0):
        super().__init__()

        self.name = name
        self.kind = kind
        self.color = color
        self.value = value

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

    def setName(self, name):
        self.name = name


car1 = Vehicle()
car1.color = "black"
car1.setName("Eleanor")
car1.value = -100

# test code
print(car1.description())
