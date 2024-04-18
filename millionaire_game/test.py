class Example:

    def __init__(self, name):
        self.name = name


obj_ex = Example('Kubek')
print(obj_ex)

print(obj_ex.__class__.__name__)
if obj_ex.__class__.__name__ == 'Example':
    print('Prawda!')

print(isinstance(obj_ex, int))
