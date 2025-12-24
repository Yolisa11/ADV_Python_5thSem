my_list=[1,2,3,4,5]

for index, value in enumerate(my_list):
    print(f"Index:{index}, value:{value}")

    

   # zip function
my_list1=[1,2,3,4]
my_list2=[4,5,6,7]
for a in zip(my_list1, my_list2):
    print (a)


#reverse
str1="asiloy"
print(str1[::-1]) #-1 reverse the string
# str1.reverse() will give the error as strings are immutable in pyhton


# function in python
def outer_function():
    outer_variable="i am nonlocal non  modified variable"
    print(outer_variable) #printing outer variable before modifying the inner function

    def inner_function():
        nonlocal outer_variable # to modify outer variable inner func we use nonlocal 
        outer_variable="i am modified"
        print(outer_variable) #printing modified outer variable

    inner_function()
    print(outer_variable) #printing outer variable after modifying in inner function 

outer_function()  



str1="dlrow nohtyp"
" ".join([word[::-1] for word in input.split()]) #1 line 


#pass is a null operation; nothing happens when it executes
def y_function():
    pass #pass function does nothing for now

#def my_function():
 #   print("before continue")
  #  continue
   # print("after continue")
 #my_function()   

