# how StopIteration works
data =[1,2,3]
it = iter(data)
print(next(it))
print(next(it))
print(next(it))
 #print(next(it))  # This will raise StopIteration exception


# generators
def get_squares(n):
    return [i**2 for i in range(n)] # returns a list of squares all at once
# generator function 
def generate_squares_gen(n):
    for i  in range(n):
        yield i**2  # yields one square at a time
gen = generate_squares_gen(100000) # creates a generator object
print (next(gen))  # prints 0
print (next(gen))  # prints 1  
print (next(gen))   # print 2

# decorator 
def say_hello():
    print("hello")

def my_decorator(func):
    def wrapper():
        print("before function call")
        func()
        print("before function call")
    return wrapper

#@my_decorator # @ symbol makes decorator apply to the function
var= my_decorator(say_hello)
var()

#say_hello()









