import Classes2

# derived(base1, base2, base3)
# resolving attribute : deriverd -> base1 -> base2 > base3 ->.. -> Object

# also search the base classes of base1 , base2 ,base3 based on C3 Algorithm
# which is needed for comlications like the Diamond relation between classes
"""
Diamond relation : in multi inheritance there will always be at least one
diamond relation

           O
       //  ||  \\
      A    B     C
      \\   ||   //
       A1  B1  C1
        \\ || //
           D
          
D ( A1 , B1 , C1)

the method resolution will start from depth(left to right)
starting ftom D to A1 and its base (A ,O) same with B1 (B ,O) same with C1
the problem is that the search will produce more than one path for some classes
(means it will be accessed and searched more than once like O in this case)

that is why there is Algorithm : The C3 Method Resolution Order

"""
class Tester:

    def __init__(slef):
        self.testtype
        
    def test(self,tt):
        self.testtype = tt
        print(f"{self.testtype} testing ..")
        
class Engine(Classes2.Machine ,Tester):

# all methods in Python are effectively virtual
    def run(self):
        print(f"running {self.__class__.__name__}.. \nDone ..")
        
    def test(self, tt, time = 13.1):
        self.testtype = tt
        print(f"{self.__class__.__name__} {self.testtype} testing for {time} hours..")


class Grinder(Classes2.Machine , Tester):

     def run(self):
        print(f"running {self.__class__.__name__}.. \nDone ..")

#self.__class__.__name__ gives the name of the class
machines = [ ]
E1 = Engine("X133","Disel Engine")
G1 = Grinder("T12Y" , "Wheat Grinder")

E1.run()

machines.append(E1)
machines.append(G1)


tuple(map(lambda x: x.test("resistence") , machines))
tuple(map(lambda x: x.run() , machines))


    
