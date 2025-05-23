"""
#What is a Module in Python?

-A module in Python is a file containing Python code (functions, 
 classes, or variables) that can be reused in other programs. 
 It helps organize code and promotes code reusability.




Types of Modules in Python:

-Built-in Modules      → Pre-installed in Python (e.g., math, random, os).
-User-defined Modules  → Custom modules created by users.
-Third-party Modules   → Installed using pip (e.g., numpy, pandas).

"""

 #created a demo.py, now we import it here

 #importing module
import demo
print(demo.add(5,5))
#10


#re-naming a module

import addTowNumber as ad
print(ad.add(55, 5))
#60

# Module vs Pakage:
# Module : A module is a piece of code
# Pakage : A pakage is a collection of modules.abs


""" 
Modules vs Packages:


 #Modules:
-Small code units for specific tasks.
-Contain functions or methods.
-Reusable in a program.
-Importable into other modules.


 #Packages:
-Collection of modules in a directory.
-Can have sub-packages/modules.
-Each has a unique namespace.
-Installed using import

"""

"""

#Example of a package:
my_package/
│── __init__.py      # Constructor - (commonly used to initialize the package)
│── module1.py       # First module
│── module2.py       # Second module
│── app.py           # also a module


"""