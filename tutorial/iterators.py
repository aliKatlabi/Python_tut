# Iterator
# An object representing a stream of data

"""

 Repeated calls to the iterator’s __next__() method
 (or passing it to the built-in function next()) return successive items in the stream
 
 Iterators are required to have an __iter__() method
 that returns the iterator object itself

 When there are no more elements, __next__() raises a StopIteration exception
 which tells the for loop to terminate
 
"""

m = [23, 44, 1, 232, 33, 11, 24, 11, 2, 3, 90, 2111, 12]

it = iter(m) # return iterator object which contain __next__ attribute

print (it.__next__()) # __next__ is also wraped in the built-in next()

print(next(it))

print("#"*10)

# when I code .. for x in m : (for calls iter(m) and uses the next())






# to make my own iterator I need to override the attributes __next__ and __iter__ properly

class Leap:

        """

        Iterate through sequence from a starting position with a specific leap (jump)
        until it reach the stop ( it might take few labs through the seq.)

        """
        def __init__(self, _object_,*,pos = 0, stop = 0, leap =1):
                self.object = _object_
                self.length = len(self.object)
                self.pos = pos
                self.stop = stop
                self.leap = leap
                self.index = self.pos - self.leap
    

        def __iter__(self):
                return self

        def __next__(self):
                self.index = self.index + self.leap

        
                if self.index >= self.length:
                        self.index = self.index - self.length
                        
                if self.index == self.stop:
                          raise StopIteration

                return self.object[self.index]


# stats = [23, 44, 1, 232, 33, 11, 24, 11, 2, 3, 90, 2111, 12]
        
leap = Leap(stats, pos = 10, stop = 6, leap =4)

for i in leap :
        print(i)





















