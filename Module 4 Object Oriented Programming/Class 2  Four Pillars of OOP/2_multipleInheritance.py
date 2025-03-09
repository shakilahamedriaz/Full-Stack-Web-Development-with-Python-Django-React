#parent class 1
class Father:
    def height(self):
        return("I am tall like my father")
    

#parent class 2
class Mother:
    def skin_color(self):
        return "I have fair skin like my mother"


#child inheriting from both father and mother
class Child(Father, Mother):
    def hobby(self):
        return "I love playing football"



#cerating object:
child = Child()

print(child.height())           # I am tall like my father
print(child.skin_color())       # I have fair skin like my mother
print(child.hobby())            # I love playing football