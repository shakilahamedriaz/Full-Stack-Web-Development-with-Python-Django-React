class Example:
    class_variable = "I belong to the class"

    @staticmethod   #class er onno kicu access korte pare na
    def static_method():
        return "I don't use calss or instance variables"
    
    @classmethod
    def class_method(cls):  # class er onno kicu access korte pare
        return f"I can access {cls.class_variable}"

print(Example.static_method())
print(Example.class_method())