
# Argument : A value passed to a function (or method) when calling

def move(by ,speed, direction = "north", after = 10, stealth =False):
        print(f"moving {by} km at speed {speed} km\h toward the {direction} after {after} min ..")
        if stealth == True:
                print("stealth mode..")


"""
KEYWORD argument: an argument preceded by an identifier (e.g. name=) in a function call
                  OR
                  passed as a value in a dictionary preceded by **.

complex(real=3, imag=5)
complex(**{'real': 3, 'imag': 5})

POSITIONAL argument: an argument that is not a keyword argument. Positional arguments can appear at the beginning of an argument list
                     and/or
                     be passed as elements of an iterable preceded by *.

complex(3, 5)
complex(*(3, 5))

RULES:
        - In a function call, keyword arguments must follow positional arguments.
        
        - All the keyword arguments passed must match one of the arguments accepted by the function and ((their order is not important)).
         This also includes non-optional arguments (e.g. parrot(voltage=1000) is valid too)
         
        - No argument may receive a value more than once .

##########

"""

move(1,10) # positional argument
move(after = 20 , speed = 20 , by =1) # arguments here are all keywords (order does not matter)

# move(speed = 10 ,"west") syntax error: positional arg follows a keyword argument

print("\n\n __next section__ \n\n")


"""
formal parameter forms :

*argument  : receives a tuple containing the _positional_ arguments beyond the formal parameter list
             DEAL with it as dictionary
             
**kwarg    : it receives a dictionary containing all _keyword_ arguments except for those corresponding to a formal parameter
             DEAL with it as tuple
"""

def shoot(damage, target,*function, ran =100 , **func_par):

        actqueue = []
        tar = target
        move_par = dict(func_par)
        actqueue = list(function)
    
        while tar > ran:
                if len(actqueue) != 0:
                        for a in actqueue:
                                if a == move :
                                        move(**func_par) # unpacking dictionary -> argument
                                        # move(**move_par) also works
                                        tar -= 10
        else:
                print("target destroyed")
        
                
shoot(10 , 150, move, by = 10 ,speed =10 , direction = "north", after = 1, stealth =True)

print("\n\n __next section__ \n\n")




"""
for more performence and redapility

if / and * peasented in the function definition

def f(positional only , /, pos_or_kwd (standard_arg) , *, key word only):


"""


def standard_arg(arg):
     print(arg)

def pos_only_arg(arg, /):
     print(arg)

def kwd_only_arg(*, arg):
     print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
     print(pos_only, standard, kwd_only)

######

#finally
##possible collision : what if a key in kwds has same name of argument in foo?
     
def foo(id ,**kwds):
        pass



foo( 3 , **{'id':123123}) #will give TypeError: foo() got multiple values for argument 'name'

#so it is better to split between name and kwds by making name argument as pos-only

# def foo(name ,/,**kwds):

















