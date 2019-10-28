
# Unpacking Argument Lists

# *-operator to unpack the arguments out of a list or tuple
# **-operator to unpack the arguments out of a dictionaries


"""
map(function, iterable, ...)

Return an iterator
that applies function to every item of iterable, yielding the results

"""

m = [ (3,44,1) ,(123,2) ,(12,222,11111)]

mapm = map(max,m) # applies max on each tuple from m
           # returns iterator of type map
           # can be made into known data structure types list , tuple ,..

listm = list(mapm)
print(listm)

          #or it can be unpacked using * (astrik)
print(*map(max,m))


# lambda function is lambda [parameters]: expression

#Like nested function definitions,
#lambda functions can reference variables from the containing scope

def inc(n):
        return lambda x: x+n # the return is function type lambda

print(inc(3)) #<function inc.<locals>.<lambda> at 0x0581C028>

f = inc(3)

print(f(27)) # 30

#[ (3,44,1) ,(123,2) ,(12,222,11111)]
# sum(sum(i^2+1))

print(*map(lambda x : sum(map(lambda i:i**2+1,x)),m)) # 1949 15135 123503752

print(sum(map(lambda x : sum(map(lambda i:i**2+1,x)),m))) #sum(1949 15135 123503752) 123520836


















        
