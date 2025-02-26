# ekta class er sudhu matro ektai object thekbe
# on use , login, Database connection,  authentication etc

class Singleton:
    _instance = None #class-level variable

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


s1 = Singleton()
s2 = Singleton()

print(s1 is s2)