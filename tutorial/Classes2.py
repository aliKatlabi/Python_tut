# function defined outside the class
def f(self):
    return self.counter


class Machine:
    counter = 0  # this is class variable same for all instances (static)
    get_counter = f  # class function (like static function)
    # also can be assigned from function defined inside the class

    def __init__(self, model, name):
        self.model = model  # this is instance variable
        self.name = name
        self.parts = []
        self.counter += 1

    def add_part(self, part):
        self.parts.append(part)

    def info(self):
        part_inf = tuple(map(lambda x: x.info(), self.parts))
        return f"{self.name}{self.model}\nparts : {part_inf}"
    def run(self):
        pass

# private variable does not exist in python, however we can treat
# variable as private like (__var) 
"""
name mangling: Any identifier of the form __spam (at least two leading underscores,
at most one trailing underscore) is textually replaced with _classname__spam,
where classname is the current class name with leading underscore(s) stripped.

Name mangling is helpful for
letting subclasses override methods without breaking intraclass method calls
"""
class MachinePart:
    # names here are all class variabl (static)
    counter = 0
    factoryName = "AK."  # class variable
    material = "steel"
    get_counter = f

    def __init__(self, name, material):
        self.name = name  # instance variable
        self.material = material  # has same as class variable -> attribute lookup prioritize the instance variable
        self.counter += 1

    def info(self):
        return f"{self.name}| made of {self.material}"


motor = Machine("X001", "Motor")
motor.info()
motor.add_part(MachinePart("skeleton", "aluminum"))
motor.add_part(MachinePart("screw", "steel"))
print(motor.info())

print(motor.parts[0].factoryName)
print(motor.parts[1].factoryName)
print("__________________")
