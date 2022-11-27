# FreeCodeCamp
# For this project, you will write a program to determine the approximate probability 
# of drawing certain balls randomly from a hat.
import random

class Hat(object):
    contents = []
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        
        for k,v in self.__dict__.items():
            for r in range(v):
                self.contents.append(k)
        

    def draw(self,num):
        current_contents = self.contents[:]
        self.num = num
        values = []
        for n in range(self.num):
            value = random.choice(current_contents)
            current_contents.remove(value)
            values.append(value)

        return values
           
        
    
def experiment(hat, expected_balls,num_balls_drawn,num_experiments):
    hat = hat
    guess = []
    for k,v in expected_balls.items():
        for r in range(v):
            guess.append(k)
    count = 0
    for r in range(num_experiments):
        drawn = hat.draw(num_balls_drawn)
        if set(guess).issubset(drawn):
            count +=1
    return count/num_experiments


hat1 = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat1,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)
