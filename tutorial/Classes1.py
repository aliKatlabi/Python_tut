#class ClassName:
#   <statement-1>
#    .
#    .
#    .
#    <statement-N>
#(In practice, the statements inside a class definition will usually be function definitions,
#but other statements are allowed)


class A:
    """Documentation of the class A""" # saved in attribute __doc__
  
    def __init__(self,id):
        print("class initiation auto invoked (constructed)")
        self.id = id #data attribute
        
    #method attribute 
    def method(self): #(this by it self a function object)
        return "method of A ran"
    
  
x = A(9090)

print(f"id : {x.id}  " + x.method())
print(f"docs of x : {x.__doc__}")

# x.method is a method object can be stored and used later
methodObject = x.method
#a method object is created by packing (pointers to)
#the instance object and the function object
#just found together in an abstract object(class or other abstract object)

#method object + argument list (a,b..) construct a function object
print(methodObject()+" from method object")
