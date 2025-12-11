''' Classes and Objects Relationship: Each object is an individual entity with its own properties, which differentiate it from other objects.'''
'''Namespaces in Action: Changes to one object's properties do not affect other objects or the original class, emphasizing the importance of namespaces.'''
'''Key Takeaway: Each object maintains its own namespace, allowing for unique characteristics without interference from others or the class itself.'''


class chai:
    origin="india"

print(chai.origin)

chai.is_hot=True
print(chai.is_hot)

masala = chai()
print(f"masala {masala.origin}")
print(f"masala {masala.is_hot}")
masala.is_hot = False

print(f"class: {chai.is_hot}")
print(f"masala: {masala.is_hot}")