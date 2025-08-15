'''
Classes vs Objects


Classes and objects serve different purposes. A class is a blueprint, while an object is what you build from that blueprint.

Here is an example of a class:

class Dog:

    # shared by all dogs
    species = "Canis familiaris"
Now we can access the class attribute directly using Dog.species where Dog is the class name:

print(f"Class species: {Dog.species}")
# Class species: Canis familiaris
This accesses data from the class itself, not from any specific object.

Now lets explore how it works in objects. Create objects from the Dog class:

dog1 = Dog()
dog2 = Dog()
Objects can have individual attributes that classes cannot:

dog1.name = "Nicky"
dog1.breed = "Siberian Husky"

dog2.name = "Teemon" 
dog2.breed = "Shu'ali"
Compare what classes and objects can do:

print(f"Object 1: {dog1.name} is a {dog1.breed}")
print(f"Object 2: {dog2.name} is a {dog2.breed}")
print(f"Both share class attribute: {Dog.species}")
Output:

Object 1: Nicky is a Siberian Husky
Object 2: Teemon is a Shu'ali
Both share class attribute: Canis familiaris
Key Difference: The class Dog defines what all dogs have in common, while objects dog1 and dog2 represent specific, individual dogs with unique properties.

challenge
Complete the code to create a Student class and two student objects. Add different names and grades to each student.

student.py: This is where you'll define your Student class.
driver.py: Main execution file that will import and use your Student class:

Complete the code to create a Student class and two student objects. Add different names and grades to each student.

student1 name is "Alice" with grade "A".

student2 name is "Bob" with grade "B".
'''