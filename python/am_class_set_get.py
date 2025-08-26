# Demonstration of property decorators for getters, setters, and deleters in Python.
# This example shows how to define a property with custom behavior for getting, setting, and deleting an attribute.
# The property 'x' is managed through methods decorated with @property, @x.setter, and @x.deleter.
# When the property is accessed, modified, or deleted, the corresponding method is invoked.
# This allows for encapsulation and control over attribute access in a class.
# The output will show when each method is called.
# Revelation!
class C:
    # Initialize the private attribute
    def __init__(self):
        self._x = None

    # Define the property 'x' with getter, setter, and deleter
    # Define the getter for property 'x'
    @property
    def x(self):
        """I'm the 'x' property."""
        print("getter of x called")
        return self._x

    # Define the setter for property 'x'
    @x.setter
    def x(self, value):
        print("setter of x called")
        self._x = value

    # Define the deleter for property 'x'
    @x.deleter
    def x(self):
        print("deleter of x called")
        del self._x


c = C()
c.x = "foo"  # setter called
foo = c.x  # getter called
del c.x  # deleter called
