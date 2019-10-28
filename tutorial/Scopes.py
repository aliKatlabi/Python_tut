#LEGB rule : interpreter looks for a name in the following order
#Local - > Enclosing -> Global -> Builtin

###############
#Built-in 

################
#Globals

G = "global G"
print("original global G :",G)

def enclosingfunc1(): #Enclosing
    D = "enc1 D"
    print(f"before local assign. D :{D:}")
    def enclosingfunc2():
        B = "enc2 B"
        C = "enc2 C"
        print(f"before local assign. B :{B:} , C : {C:}, G : {G:}")
        
        def innermostfunc(): #Locals
            print("innermostfunc run")
            
            B = "local B"
            nonlocal C #will become in the enlosing  scope and rebind var's with same name 
            C = "C from local to nearest enclosing func."
            nonlocal D #will become in the enlosing  scope and rebind var's with same name 
            D = "D from local to nearest enclosing func."
            global G #will become in the global scope and rebind var's with same name
            G = "G from local to global"

        
        innermostfunc()
        print(f"after local assign. B :{B:} , C : {C:}, G : {G:}")

            
    enclosingfunc2()

    
enclosingfunc1()

