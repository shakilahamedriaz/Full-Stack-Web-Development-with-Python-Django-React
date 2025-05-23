"""
https://ostad.app/dashboard/my-courses/672a1282474c0ab783efefa8/videos?module=672a12a0474c0ab783eff3d0
if __name__ == "__main__" 

 - in Python This condition is used to check 
  whethera Python script is being run directly
  or imported as a module in another script.



#How It Works:

-Every Python file has a special built-in variable called __name__.
-When a script is run directly, __name__ is set to "__main__".
-When a script is imported into another file, __name__ is set to the file’s name (not "__main__").

"""


"""
# directly run korle name er against e value (__main__ pai)
# import kora file thakle __name__ is set to 'file's name'

"""
from demo import add as a , mul
print(a(2, 2)) #4

#print(mul(8, 8)) #64
#cannot import name 'mul' from 'demo'

"""
The if __name__ == "__main__" is used to:
-Testing pourpose
-Security to un
-Runs code only when the script is executed directly.
-Prevents code from running when the script is imported as a module into another script

"""

