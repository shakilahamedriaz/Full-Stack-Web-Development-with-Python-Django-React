# Bismillahir Rahmanir Rahim
# author : Shakil Ahamed Riaz

def display_fibonacci_series():
    
    while True:
        print("\nChoose an option:")
        print("1. Generate Fibonacci series by number of terms")
        print("2. Generate Fibonacci series by maximum value")
        print("3. Exit now")


        taken_val = input("Enter your Choice: ")

        if taken_val == "1":
            n_terms = int(input("Enter the number of terms: "))
            if n_terms <= 0:
                print("Number of terms can't be non-negative integers - Try again")
                continue

            a = 0
            b = 1
            arr = []
            for i in range(n_terms):
                arr.append(a)
                a, b = b, a + b
            print(f"Fibonacci series ({n_terms} terms): {', '.join(map(str, arr))}")
        
        elif taken_val == "2":

            max_value = int(input("Enter the maximum value: "))
            if max_value <= 0:
                print("Number of terms can't be non-negative integers- Try again")
                continue    
            
            a = 0
            b = 1
            arr = []
            while a <= max_value:
                arr.append(a)
                a, b = b, a + b
            print(f"Fibonacci series (up to {max_value}): {', '.join(map(str, arr))}")
        
        elif taken_val == "3":
            print("Exiting now...")
            break
        

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    display_fibonacci_series()
