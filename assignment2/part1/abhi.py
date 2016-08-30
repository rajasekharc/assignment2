
class A:
    'This class is used to define a shapes.'
    #variables
    name='Bat'
    
    @staticmethod
    def change_name(updated_name):
        A.name = updated_name
        
    def __init__(self, len,color,diameter):
        self.length = len
        self.color = color
        self.diameter = diameter
    
    def display(self):
        print ("Calling from A, size  color :  diameter " )
        

a_object=A(10,'red',108)
A.name = 'Ball'
print (a_object.display())
print (A.name)


class B(A):
    def __init__(self,rad,area):
        super().__init__(1,'blue',89)
        self.radius=rad
        self.area=area
    
    def display(self):
        print ("Radius : %d, Area = %s" %(self.radius, self.color))


b_object = B(1,'3.14')
b_object.display()
print (b_object.color)

print (A.__name__)
print (A.__module__)
print (A.__doc__)

A.change_name("Racket")
print (A.name)

