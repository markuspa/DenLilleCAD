

class Dlcadcore:
    def __init__(self, canvas):
        #self.db = 
        self.canvas = canvas
        self.scale = 1
        self.camera = (0,0,100,0,3.14/2,0) # x,y,z,thx,thy,thz



    def test(self):
        print('test')

    def line(self, x0, y0, x1, y1):
        self.canvas.create_line(x0, y0, x1, y1)



        pass
    def select(self, objs): pass
    def transform(self, objs, p0, r, scale, rot_matrix): pass


