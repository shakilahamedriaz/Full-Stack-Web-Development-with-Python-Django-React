#demo.py

#creating a module

def add(a, b):
    result = a + b
    return result



#5.5   __name__ == __main__ concept
print(__name__)

if __name__ == '__main__':
    def mul(a, b):
          return a * b
    print("This runs only when demo.py file directly executed")
else:
    print("imported")