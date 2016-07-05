
class Point:
    """ Represents a point in 2D space """
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '({},{})'.format(self.x,self.y)
    
class Rectangle:
    """Represents a rectangle. attributes: width, height, corner."""
#    def __init__(self,width=0.0,height=0.0,corner=Point()):
    def __init__(self,width=20.0,height=10.0,corner=Point()):
        self.width = width
        self.height = height
        self.corner = corner
    
    def find_center(self):
        center = Point()
        center.x = self.corner.x + self.width/2.0
        center.y = self.corner.y + self.height/2.0
        return center
    
    def __str__(self):
        return '{:.1f} by {:.1f}, corner is {:s}'.format(self.width,self.height,self.corner)



a_box = Rectangle(100.0,200.0)

#Start
print a_box


#Next
another_rect = Rectangle()
print another_rect


#Finally
third_rect = Rectangle(30,30,Point(5,5))
print third_rect