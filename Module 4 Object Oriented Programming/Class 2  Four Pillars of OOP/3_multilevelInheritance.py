#chain wise inherit method, like dada theke baba, baba theke child

#grandParend class
class Grandpa:
    def wishdom(self):
        return "I have a lot of Experience in life"

#parent class (inherits from grandpa)
class Father(Grandpa):
    def profession(self):
        return "Father is doctor"


#child class (inherits from father)
class Child(Father):
    def hobby(self):
        return "I love painting"


child1 = Child()

print(child1.wishdom())
print(child1.profession())
print(child1.hobby())

"""
output:
I have a lot of Experience in life
Father is doctor
I love painting

"""