
globalvar = 1
globalvar2 = 2

#table of global variabls contains [globalvar, globalvar2, fun1, funout]


#each function will own a ((new symbol table)) to store local variables
def fun1(parameter):#parameter introduced (passed by value)
	"""
	documentation
	"""
	#table of local variabls contains [var1,var2,parameter]

	var1 = parameter**2 #stroes in the variable symbol table
	var2 = parameter%2  # "" "" ""
	globalvar= 22 #global variables and variables of enclosing functions cannot be directly assigned a value within a function
	return var1*var2
	
print(fun1(13))
print("global is not changed: ",globalvar)


def funout(): #funout() is enclosing function of funin()
	"""
	documentation
	"""
	v_funout = 1
	#to funin table of local variabls of funout is the table of enclosing function which contain[v_funout]
	
	def funin(): #function defined in another
	
		v_funout=3 #variable references first look in the local symbol table then -> local symbol tables of enclosing functions -> global symbol table
		# LEGB rule
		
		v_funin ="in"
		print("v_funout inside funin: " + str(v_funout))
		
	funin()	#The (((execution of a function not the defining))) introduces a new symbol table used for the local variables of the function
	
	print("v_funout original after assignment in funin: " + str(v_funout))
funout()

