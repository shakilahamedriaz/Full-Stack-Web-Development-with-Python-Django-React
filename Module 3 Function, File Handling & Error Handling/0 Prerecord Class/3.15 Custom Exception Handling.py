
# Custom error handling

def check_file(filename):
    if not filename.endswith('.png'):
        raise ValueError("Only .png files are allowed")
    print("Valid file")



try:
    check_file('data.txt')
except Exception as e:
    print(e)