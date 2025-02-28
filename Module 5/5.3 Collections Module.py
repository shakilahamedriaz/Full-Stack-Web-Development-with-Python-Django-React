from collections import defaultdict
import collections
#from collections import defaultdict as (new name)

#print(collections.__doc__)
#print(dir(collections))

fruits = ['apple', 'banana', 'orange', 'watermelon', 'banana', 'orange' ]
#used to count hashable objects
print(collections.Counter(fruits))
#Counter({'banana': 2, 'orange': 2, 'apple': 1, 'watermelon': 1})


#  Returns a list of the top 2 most frequent items 
print(collections.Counter(fruits).most_common(2))
#[('banana', 2), ('orange', 2)]



# value gula list hisebe thakbe
# Creating a defaultdict where values are stored as lists
student_subjects = defaultdict(list)

#adding subject for diffrent student
student_subjects['Alice'].append('Math')
student_subjects['Alice'].append('Physics')

student_subjects['Bob'].append('Chemistry')
student_subjects['Bob'].append('Biology')

student_subjects['Shakil'].append('Software Engineering')

#print the dictionary
print(student_subjects)
# defaultdict(<class 'list'>, {'Alice': ['Math', 'Physics'], 'Bob': ['Chemistry', 'Biology'], 'Shakil': ['Software Engineering']})



