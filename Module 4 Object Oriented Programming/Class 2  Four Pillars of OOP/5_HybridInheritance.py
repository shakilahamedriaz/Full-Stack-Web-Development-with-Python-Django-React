# parent class(Grandfather)
class Grandfather:
    def legacy(self):
        return "I built a real estate empire"


# Father class (inherits from GrandFather)
class Father(Grandfather):
    def profession(self):
        return "I am a Software Engineer"


# Mother class (inherits from Grandfather)
class Mother(Grandfather):
    def talent(self):
        return "I am a housewife"



class Son(Father, Mother):
    def hobby(self):
        return "I love Coding"


# Creating an instance of Son
son = Son()

#Accessing properties from diffrent levels of inheritance
print(son.legacy())     # from Grandfather  -> I built a real estate empire
print(son.profession()) # from Father       -> I am a Software Engineer
print(son.talent())     # from mother       -> I am a housewife
print(son.hobby())      # from own method   -> I love Coding