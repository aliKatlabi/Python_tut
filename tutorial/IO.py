from random import randrange
user = 'user'
userlist = [str(user)+f"_{x:}@elte" for x in range(10)]

#Formatted string literals (also called f-strings for short) 
#let you include the value of Python expressions inside a string by prefixing the string with f or F 
#F or f"{variabl:format(like 2.2% or -9)}" it refers a variable or literal values

id = "9231A"

"{} has the id {}".format(userlist[1],id) 
#output>>>'user_1@elte has the id 9231A'
# another way of formatting output

idList = [f"{x}X{y}X{z}" for i in range(10) for x in [randrange(10)] for y in [randrange(10)] for z in [randrange(10)]]


users = set(zip(userlist , idList))

for x in users:
    print(f'{x[0]:15}==>{x[1]:>10}')
	#also print('{0[0]:20}==>{0[1]:10}'.format(users)) for subscriptable sequences [set is not subscriptable]
	
#check Format Specification Mini-Language to know how to formate {:here}
