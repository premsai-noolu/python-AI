""" In Python, static methods are part of a class but do not require an instance of that class to be called. They are defined using the @staticmethod decorator. Here’s a breakdown of how static methods work and their benefits:

Definition: To create a static method, define a method in a class and decorate it with @staticmethod. This indicates that it does not depend on instance attributes or methods."""


'''Calling a Static Method: Static methods can be called on the class itself or an instance of the class. For example:

result = MyClass.my_static_method(5, 10)  # Calls the method from the class.
instance = MyClass()
result_instance = instance.my_static_method(5, 10)  # Calls the method from an instance.'''






class ChaiUtils:

    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    
raw=" mil, cofee    , sugar, tea   "

print(ChaiUtils.clean_ingredients(raw))