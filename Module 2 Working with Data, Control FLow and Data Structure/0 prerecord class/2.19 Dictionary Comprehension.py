#dictonary comprehension
nums = list(range(0, 11)) # 10 value
result = {i : "even" if i%2 == 0 else "odd" for i in nums}

print(result)

#output:
"""{0: 'even', 1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}"""