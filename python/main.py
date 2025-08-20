#!/usr/bin/env python3
"""
Python Types from Scratch
=========================

This file provides a comprehensive overview of Python's type system,
from basic types to advanced type hints and annotations.
"""

# =====================
# SECTION 1: BASIC TYPES
# =====================
print("\n=== BASIC TYPES ===")

# Integer type
integer_value = 42
print(f"Integer: {integer_value}, Type: {type(integer_value)}")

# Float type
float_value = 3.14159
print(f"Float: {float_value}, Type: {type(float_value)}")

# String type
string_value = "Hello, Python!"
print(f"String: {string_value}, Type: {type(string_value)}")

# Boolean type
boolean_value = True
print(f"Boolean: {boolean_value}, Type: {type(boolean_value)}")

# None type
none_value = None
print(f"None: {none_value}, Type: {type(none_value)}")

# Type conversion
print("\n--- Type Conversion ---")
print(f"int('10'): {int('10')}")
print(f"float('3.14'): {float('3.14')}")
print(f"str(42): {str(42)}")
print(f"bool(1): {bool(1)}")
print(f"bool(0): {bool(0)}")
print(f"bool(''): {bool('')}")
print(f"bool('text'): {bool('text')}")

# =====================
# SECTION 2: COLLECTION TYPES
# =====================
print("\n=== COLLECTION TYPES ===")

# List - mutable, ordered collection
my_list = [1, 2, 3, "four", 5.0]
print(f"List: {my_list}, Type: {type(my_list)}")
print(f"List element access: my_list[3] = {my_list[3]}")
my_list.append(6)
print(f"After append: {my_list}")
my_list.remove("four")
print(f"After remove: {my_list}")

# Tuple - immutable, ordered collection
my_tuple = (1, 2, 3, "four", 5.0)
print(f"\nTuple: {my_tuple}, Type: {type(my_tuple)}")
print(f"Tuple element access: my_tuple[3] = {my_tuple[3]}")
# Tuples are immutable, so the following would raise an error:
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Dictionary - mutable, unordered collection of key-value pairs
my_dict = {"name": "Alice", "age": 30, "is_student": False}
print(f"\nDictionary: {my_dict}, Type: {type(my_dict)}")
print(f"Dictionary access: my_dict['name'] = {my_dict['name']}")
my_dict["location"] = "New York"
print(f"After adding key: {my_dict}")
del my_dict["is_student"]
print(f"After deleting key: {my_dict}")

# Set - mutable, unordered collection of unique elements
my_set = {1, 2, 3, 3, 4, 4, 5}  # Duplicates are automatically removed
print(f"\nSet: {my_set}, Type: {type(my_set)}")
my_set.add(6)
print(f"After add: {my_set}")
my_set.remove(3)
print(f"After remove: {my_set}")

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"\nSet A: {set_a}, Set B: {set_b}")
print(f"Union (A | B): {set_a | set_b}")
print(f"Intersection (A & B): {set_a & set_b}")
print(f"Difference (A - B): {set_a - set_b}")
print(f"Symmetric Difference (A ^ B): {set_a ^ set_b}")

# =====================
# SECTION 3: TYPE HINTS AND ANNOTATIONS
# =====================
print("\n=== TYPE HINTS AND ANNOTATIONS ===")

# Basic type annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(f"Function with type hints: {greet('World')}")
print(f"Function annotations: {greet.__annotations__}")

# Type hints for collections
from typing import List, Dict, Tuple, Set, Optional, Union, Any

def process_items(items: List[int]) -> int:
    return sum(items)

print(f"Sum of list [1, 2, 3]: {process_items([1, 2, 3])}")

# Optional type (can be None)
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

print(f"Find user 1: {find_user(1)}")
print(f"Find user 3: {find_user(3)}")

# Union type (can be one of several types)
def process_input(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Processed integer: {value * 2}"
    else:
        return f"Processed string: {value.upper()}"

print(f"Process 5: {process_input(5)}")
print(f"Process 'hello': {process_input('hello')}")

# Type aliases
UserId = int
UserName = str

def get_user_info(user_id: UserId) -> UserName:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id, "Unknown")

print(f"User info for ID 2: {get_user_info(2)}")

# =====================
# SECTION 4: TYPE CHECKING
# =====================
print("\n=== TYPE CHECKING ===")

# isinstance() - check if an object is an instance of a class or type
value = "Hello"
print(f"Is '{value}' a string? {isinstance(value, str)}")
print(f"Is '{value}' an integer? {isinstance(value, int)}")

# issubclass() - check if a class is a subclass of another class
print(f"Is bool a subclass of int? {issubclass(bool, int)}")

# Type checking with multiple types
value = 42
print(f"Is {value} either an int or a str? {isinstance(value, (int, str))}")

# =====================
# SECTION 5: CUSTOM TYPES AND CLASSES
# =====================
print("\n=== CUSTOM TYPES AND CLASSES ===")

# Creating a custom class
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I'm {self.age} years old."

# Using the custom class
alice = Person("Alice", 30)
print(f"Person instance: {alice}")
print(f"Person type: {type(alice)}")
print(f"Person greeting: {alice.greet()}")

# Inheritance
class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id
    
    def study(self) -> str:
        return f"{self.name} is studying hard!"

bob = Student("Bob", 20, "S12345")
print(f"\nStudent greeting: {bob.greet()}")
print(f"Student studying: {bob.study()}")
print(f"Is bob a Student? {isinstance(bob, Student)}")
print(f"Is bob a Person? {isinstance(bob, Person)}")

# =====================
# SECTION 6: ADVANCED TYPE FEATURES
# =====================
print("\n=== ADVANCED TYPE FEATURES ===")

# Type checking with protocols (structural subtyping)
from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None:
        print("Drawing a circle")

class Square:
    def draw(self) -> None:
        print("Drawing a square")

class Triangle:
    def calculate_area(self) -> float:
        return 0.0

def draw_shape(shape: Drawable) -> None:
    shape.draw()

circle = Circle()
square = Square()
triangle = Triangle()

print(f"Is Circle Drawable? {isinstance(circle, Drawable)}")
print(f"Is Square Drawable? {isinstance(square, Drawable)}")
print(f"Is Triangle Drawable? {isinstance(triangle, Drawable)}")

# Generic types
from typing import TypeVar, Generic

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, content: T):
        self.content = content
    
    def get_content(self) -> T:
        return self.content

int_box = Box[int](42)
str_box = Box[str]("Hello")

print(f"\nInt box content: {int_box.get_content()}")
print(f"String box content: {str_box.get_content()}")

# Type checking with mypy
# To check types statically, run: mypy main.py
# This will catch type errors without running the code

print("\nThis file provides a comprehensive overview of Python's type system.")
print("To check types statically, you can use mypy: mypy main.py")
print("Run this file to see all the examples in action!")

if __name__ == "__main__":
    print("\nSuccessfully completed all type examples!")