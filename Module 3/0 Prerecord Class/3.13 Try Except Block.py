
try:  # je code e exception thakte pare
    with open('name.txt', 'r') as file:  # rahim.txt
         print(file.read())
         print(10/10)  #10/0
         x = int("44") #'abc'
         a = [1,2,3,4]
         print(a[1])   #a[100] , 100 th index nai
         a = abc       #abc ki is string or variable , that not defined



except FileNotFoundError:
    print("File not found")  # user can understand by this message
except ZeroDivisionError:
    print("Error: Division by zero is not possible")    
except ValueError:
    print("Invalid Value")
except IndexError:
    print("Invalid Index")
except Exception as here: #specefic name na thakle eta hobe, Onakima error
    print("Some error occoured!", here)


# Like this way, we will handle exception