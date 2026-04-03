## _POLYMORPHISM_
* Polymorphism in Python means “one interface, multiple implementations”. 
* The same function, method, or operator behaves differently depending on the object or data type.

### <u>_Polymorphism Types in python_</u>
```text
                                               POLYMORPHISM (Python)
                                                     │
   ┌───────────────────────────────────┬────────────────────────────────┬─────────────────────────────────┐
   │                                   │                                │                                 │                      
   │                                   │                                │                                 │                      
Runtime Polymorphism              Duck Typing                  Operator Overloading           ❌ Method Overloading
(Method Overriding)               (Dynamic)                    (Operators)                    (Not Supported)
   │                                   │                                │                                │
   │                                   │                                │                                │
Parent Class                     Object Behavior                  Same Operator,                Same method name,
    │                            (Method Presence)                Different Meaning             different params ❌
    │                                   │                               │                              │
    ▼                                   ▼                               ▼                              │
Child Classes                    No type checking                Built-in / Custom                     ▼
override method                  → only method                   (__add__, __str__)            Achieved via:
same name                        existence matters                                               • Default args
   │                                   │                               │                         • *args / **kwargs
   ▼                                   ▼                               ▼                                 │
Different outputs               Same function                   + → add numbers                          ▼
for same method                 works for                       + → concat strings              def add(a,b,c=0)
call                            different objects               + → combine objects             def add(*args)
                                (fly(), pay(), etc.)
```
 1. <u>_*Method Overriding (Runtime Polymorphism)*_</u>
    * A child class provides its own implementation of a method already defined in the parent class
        ```python
            class Animal:
                def sound(self):
                print("Animal makes sound")
    
            class Dog(Animal):
                def sound(self):
                    print("Dog barks")
            
            class Cat(Animal):
                def sound(self):
                    print("Cat meows")
            
            # Polymorphism
            animals = [Dog(), Cat()]
            
            for a in animals:
                a.sound()
        ```
 2. <u>_*Duck Typing*_</u>
    * Python doesn’t care about the object type, only whether the object has the required method.
        ```python
        class Bird:
             def fly(self):
                 print("Bird can fly")
    
        class Airplane:
            def fly(self):
                print("Airplane can fly")
        
        def start_flying(obj):
            obj.fly()
        
        start_flying(Bird())
        start_flying(Airplane())
        ```
    * `e,g,`: A “payment system” accepts UPI, card, or wallet → as long as each has a pay() method, it works.
 3. <u>_*Operator Overloading*_</u>
    * In build
        ```python
            print(5 + 3)        # Integer addition
            print("Hello " + "World")  # String concatenation
        ```
    * Custom 
        ```python
             
             class Point:
                 def __init__(self, x, y):
                     self.x = x
                     self.y = y
        
                 def __add__(self, other):
                     return Point(self.x + other.x, self.y + other.y)

             p1 = Point(2, 3)
             p2 = Point(4, 5)
             p3 = p1 + p2
                
             print(p3.x, p3.y)        
        ```
 

