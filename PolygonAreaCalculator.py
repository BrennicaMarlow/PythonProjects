
class Rectangle():
    def __init__(self,width,height):
        self.width = width
        self.height = height   

    def set_width(self,width):
        self.width = width
        return self.width
        

    def set_height(self,height):
        self.height = height
        return self.height

    def get_area(self):
        return self.width * self.height
    
    
    def get_perimeter(self):
        w2 = 2*self.width
        h2 = 2*self.height
        return w2 + h2

    def get_diagonal(self):
        w2 = self.width**2
        h2 = self.height**2
        return (w2 + h2)**0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture"
        else:
            stars = self.width*"*"
            lines = ""
            for i in range(self.height):
                lines += stars+"\n"
                
        return lines

    def get_amount_inside(self,shape):
        w = self.width
        h = self.height
        
        self.shape = shape
        fit_h = self.shape.height
        fit_w = self.shape.width
        
        dw = w - fit_w
        dh = h - fit_h
        if (dw % 1 == 0) and (dh % 1 == 0):
            a = self.get_area()
            fits = a//(fit_w*fit_h)
            return fits
        else:
            return 0

        

class Square(Rectangle):
    def __init__(self, length):
        self.length = length
        self.height = self.length
        self.width = self.length
        

    def set_side(self,side):
        self.height = side
        self.width = side       
        return side

        

r = Rectangle(width=10,height=5)
print(r.get_area())
r.set_height(3)
print(r.get_perimeter())
print(r.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq.get_picture())

r.set_height(8)
r.set_width(16)
print(r.get_amount_inside(sq))