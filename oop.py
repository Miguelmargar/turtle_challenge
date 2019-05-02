class Grid():
    
    def __init__(self):
        
        self.grid = {
            "size": (0, 0),
            "bombs": [],
            "start": (0, 0),
            "exit": (0, 0)
        }
        
    def set_size(self, x, y):
        self.x = x
        self.y = y
        self.grid["size"] = (self.x, self.y)
        
        
    def get_size(self):
        print("The size of the maze is:", self.grid["size"])
    
    
    def set_start(self, sx, sy):
        if sx > self.grid["size"][0] and sy > self.grid["size"][1]:
            print("invalid start as parameters given too big")
        else:
            self.sx = sx
            self.sy = sy
            self.grid["start"] = (self.sx, self.sy)
            
    def get_start(self):
        print("The start location is:", self.grid["start"])
    
        
    def set_exit(self, ex, ey):
        if ex > self.grid["size"][0] and ey > self.grid["size"][1]:
            print("invalid start as parameters given too big")
        else:
            self.ex = ex
            self.ey = ey
            self.grid["exit"] = (self.ex, self.ey)
            
    def get_exit(self):
        print("The exit is:", self.grid["exit"])
    
        
    def add_bombs(self, bx, by):
        if bx > self.grid["size"][0] and by > self.grid["size"][1]:
            print("invalid start as parameters given too big")
        else:
            self.bx = bx
            self.by = by
            self.grid["bombs"].append((self.bx, self.by))
            
    def get_bombs(self):
        print("the bombs are at:", self.grid["bombs"] )
        
    def remove_bombs(self, rx, ry):
        self.rx = rx
        self.ry = ry
        if (self.rx, self.ry) not in self.grid["bombs"]:
            print("The location specified has no bombs")
        else:
            self.grid["bombs"].remove((self.rx, self.ry))
        
    
a = Grid()
a.set_size(8, 12)
a.set_start(1,1)
a.set_exit(8,11)
a.add_bombs(2,3)
a.add_bombs(4,9)
a.remove_bombs(2,4)

print(a.get_bombs())