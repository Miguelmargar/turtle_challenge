class Grid():
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.bx = 0
        self.by = 0
        self.sx = 0
        self.sy = 0
        self.ex = 0
        self.ey = 0
        
        self.grid = {
            "size": (self.x, self.y),
            "bombs": (self.bx, self.by),
            "start": (self.sx, self.sy),
            "exit": (self.ex, self.ey)
        }
        
    def set_size(self, x, y):
        self.x = x
        self.y = y
        
    def get_size(self):
        return self.grid["size"]
    
    def set_start(self, sx,sy):
        if sx > x and sy > y:
            print("invalid start as parameters given too big")
        else:
            self.sx = sx
            self.sy = sy
        
    def set_exit(self, ex, ey):
        if ex > x and ey > y:
            print("invalid start as parameters given too big")
        else:
            self.ex = ex
            self.ey = ey
        
    def set_bombs(self, bx, by):
        if bx > x and by > y:
            print("invalid start as parameters given too big")
        else:
            self.bx = bx
            self.by = by
    
    
a = Grid()
a.set_size(8, 12)
print(a.get_size())