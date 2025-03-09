# parent class (Father)
class Father:
    def surname(self):
        return "Faruqi"
    
    def family_business(self):
        return "Runs an Educational Institution"


# child calss 1(Son)
class Son(Father):
    def profession(self):
        return  "Software Enginner"


# child class 2(Daughter)
class Daughter(Father):
    def hobby(self):
        return "Loves Painting"

#Creating instance of son and Daughter
putro = Son()
meye = Daughter()

print(f"Son's surname: {putro.surname()}")
print(f"Son's Profession: {putro.profession()}")
print(f"Son's Family Business: {putro.family_business()}")



print(f"Daughter's Surname: {meye.surname()}")
print(f"Daughter's Hobby: {meye.hobby()}")
print(f"Daughter's Family Business: {meye.family_business()}")



#Output:
"""
Son's surname: Faruqi
Son's Profession: Software Enginner
Son's Family Business: Runs an Educational Institution

Daughter's Surname: Faruqi
Daughter's Hobby: Loves Painting
Daughter's Family Business: Runs an Educational Institution
"""
