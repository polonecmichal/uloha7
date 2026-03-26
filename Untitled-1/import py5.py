
import py5

#def setup():
#    py5.size(200, 200)
#    py5.rect_mode(py5.CENTER)
#
#def draw():
#    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)
#
#py5.run_sketch()

#Hviezda
class Star:
    def __init__(self):
        self.x = py5.random(0, py5.width)
        self.y = py5.random(0, py5.height)
        self.z = py5.random(0, py5.width)

    def update(self):
        pass

    def show(self):
        py5.fill(255)
        py5.no_stroke()
        py5.ellipse(self.x, self.y, 8, 8)



#Array
stars = [Star() for _ in range(100)] #preco?



#Void
def setup():
    py5.size(400, 400)
    for i in range(len(stars)):
        stars[i] = Star()



def draw():
    py5.background(0)
    for i in range(len(stars)):
        stars[i].update()
        stars[i].show()
