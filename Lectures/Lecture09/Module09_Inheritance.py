"""
- We can use inheritance to create a new class from an existing class.
    - A "Child" is a specialised object that has all the characteristics of the general object, plus unique characteristics.
    - Inheritance in code is similar to family trees:
        - The traits of the parent are inherited by the child.

- Inheritance is an "is a" relationship.
    - "specialised class *is a* special version of the general"
    - E.g.,:
        - Rectangle is a Shape
        - Daisy is a Flower
        - Elf is a Character

- Inheritance is not to be confused with composition.
- Composition is a "has a" relationship:
    - E.g.,:
        - Car has a Wheel
        - Person has a Leg
        - Band has a Musician

- We might say "Bob is a Person", but Bob is just an instance.

- Inheritance is shown with an open arrowhead from subclass to superclass.

- Bound methods have an instance in front of the method call and automatically pass self
    - It is possible to call a method without Python binding self. In that case, the programmer does it explicitly.
    - DO NOT USE UNBOUND METHODS UNLESS YOU HAVE TO
        - E.g., use name.upper() not str.upper(name)
    - Do we ever use unbound methods?
        - When we create a specialised subclass, we want to ensure that we initialise our new class instances the
            way they are supped to, by calling __init__ of the super class.
        - class SubClass(SuperClass):

- If we don't explicitly say so, our class may inherit stuff from the super class, but we must make sure we call
    it in the proper context.
        - For example, the __init__ would be:
        class SubClass(SuperClass):
            def __init__(self):
                SuperClass.__init__(self)
                # do anything special to SubClass
        - Instead of passing positional arguments explicitly, we can pass all arguments using **kwargs
            - kwargs = keyword arguments = a dictionary of all the arguments
        - **kwargs passes all keyword arguments from the parent class to the child class
            - E.g.:
                - Person() knows name and dob, and passes those using **kwargs to...
                - Student(), which then knows name, dob, and student id and course name

- Polymorphism allows us to treat similar classes similarly
    - If you have a list of objects that are not all the same type (class), but they all have the same method name
        defined, you can call that method on each element in the exact same way:
    - E.g.:
        performers = [dancer, comedian, musician]
        for performer in performers:
            performer.perform()
    - Each performer is an object of a different class
    - perform() does different things for each class

"""
