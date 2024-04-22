class Example:
    def __init__(self, name):
        self.name = name

    def __str__(self):  # __repr__
        return f'Jestem obiektem, a moje imie to: {self.name}'


obj_ex = Example('kubek')
obj_ex2 = Example('kubek')
print(obj_ex)

print(obj_ex.__class__.__name__)
if obj_ex.__class__.__name__ == 'Exmple':
    print('Prawda!')

# number = 3.0
# print(isinstance(number, float))

print(isinstance(obj_ex, int))


# __eq__: a method which determines whether this object is equal to another. There are also other methods for determining if it’s not equal,
# less than, etc.. These methods are used in object comparisons, for example when we use the equality operator == to check if two objects are equal.


def __eq__(self, other):
    if isinstance(other, Example):
        return self.name == other.name
    else:
        return False


print(__eq__(obj_ex, obj_ex2))
