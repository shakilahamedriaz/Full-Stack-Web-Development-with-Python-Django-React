class School:
    School_name = "Abc High Shcool"  # class variable

    def __init__(self, name):
        self.student_name = name    #instance variable




#class variable prottekt ta object er jonne same thakbe,but instance variable unique thakbe
sc1 = School("Rahim")
sc2 = School("Karim")

#sc1.School_name = "KN High School"
#School.School_name = "All High School"

print(sc1.School_name)
print(sc1.student_name)

print(sc2.School_name, sc2.student_name)