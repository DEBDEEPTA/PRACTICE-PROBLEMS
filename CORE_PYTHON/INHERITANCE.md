## _INHERITANCE_
* Inheritance means a `child class can reuse and extend the properties and methods of a parent class`.
* When one class inherits another class:
  * Parent/Base/Super class → existing class
  * Child/Derived/Sub class → new class using parent features
  ```text
                        PYTHON INHERITANCE
                               │
         ┌─────────────────────┼─────────────────────┬─────────────────────┐
         │                     │                     │                     │
         │                     │                     │                     │
      Single                "Multi"              Multiple              Multilevel
    Inheritance          (Hierarchical)         Inheritance           Inheritance
         │                     │                     │                     │
         ▼                     ▼                     ▼                     ▼
    
         A                     A                     A     B                 A
         │                   ┌─┴─┐                    \   /                  │
         B                   B   C                     \ /                   B
                                                    C (child)                │
                                                                             C
  ```
 1. <u>_*Single Inheritance*_</u>
     ```python
        class Animal:
            def eat(self):
                print("Animal eats food")
    
        class Dog(Animal):
            def bark(self):
                print("Dog barks")
        
        d = Dog()
        d.eat()    # inherited from Animal              # op -> Animal eats food
        d.bark()   # own method                         #    -> Dog barks
     ```
 2. <u>*_Multi Inheritance_*</u>
    ```python
    class Animal:
        def eat(self):
            print("Animal eats")
    
    class Dog(Animal):
        def bark(self):
            print("Dog barks")
    
    class Cat(Animal):
        def meow(self):
            print("Cat meows")
    
    d = Dog()
    c = Cat()
    
    d.eat()         # O/P -> Animal eats
    d.bark()        #     -> Dog bark
    
    c.eat()         #     -> Animal eats
    c.meow()        #     -> Cat meows
    ```
 3. <u>*_Multi Level Inheritance_*</u>
    ```python
    class Grandparent:
        def house(self):
            print("Grandparent owns a house")
    
    class Parent(Grandparent):
        def car(self):
            print("Parent owns a car")
    
    class Child(Parent):
        def bike(self):
            print("Child owns a bike")
    
    obj = Child()
    obj.house()             # O/P -> Grandparent owns a house
    obj.car()               #     -> Parent owns a car
    obj.bike()              #     -> Child owns a bike
    ```
 4. <u>*_Multiple Inheritance_*</u>
    ```python
    class A:
        def show(self):
            print("A.show")
    
    class B:
        def show(self):
            print("B.show")
    
    class C(A, B):
        pass
    
    """
    note -> Call __mro__ on the object of the class
         -> return a tuple which includes it's parent classes in the order in which python interpreter checks for a method
    """
    obj = C()
    obj.show()
    print(C.__mro__)
    ```
    O/P :
    ```commandline
        A.show
        (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
    ```
    * <u>*_MRO (Method Resolution Order)_*</u>
      1. MRO tells Python: “In what order should I search the classes when looking for a method?”
      2. Without MRO, Python would not know:
         1. which parent method to call first 
         2. how to avoid duplicate searches 
         3. how to maintain a consistent inheritance order