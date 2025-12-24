# built-in: (math, random, datatime, json, os, sys,  csv, collections, re, tkinter)
# third-party: (numpy, pandas, seaborn, django, tensorflow, skicit-learn, ploty, flask, fasta pi)

# math
import math;
print (math.sqrt(16))

 #random            
import random; print (random.randint(1,10)) #random  integer between 1 and 10

 # datetime
import datetime; now= datetime.datetime.now(); print(now) #datetime now

#os
import os; print(os.getcwd()) #os current working directory

#json
import json; data={"name": "Yolisa", " age":20}; json_string= json.dumps(data); print (json_string) # json string

# exception handling
#try , except

try:
    print(4/0)
except Exception as e:
    print (" an error occured:", e)

# try , except , else , finally
try:
    print(10/0)

except Exception as e:
    print(" an error occured:", e)
else:
        print(" no error occured")
finally:
        print(" execution completed")

#raise (throw)



# file handling
with open("sample.txt", "w") as file: # with statement auto closes the file
    file.write("Hello, World!")
    file.write("\nHello, Yolisa")
    file.write("\nHello, World!")

with open("sample.txt", "r") as file:
     data= file.read()
     print(data) 



