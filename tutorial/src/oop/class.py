class SimpleClass:
    
    # instance attribute and class constructor
    def __init__(self, name):
        self.name = name
    
    # parameterless function    
    def speak(self):
        print(f"Name: {self.name}")
        
    # simple function
    def ask(self, age):
        self.age = age
        SimpleClass.speak()
        print(f"Age: {self.age}") 
        
    '''
    __init__ = special function to create class constructors.
    self = represents instance of a class. It points to current instance of the object.
    
    if a function takes no arguments, it still have to pass 'self' as parameters.
    '''
    
