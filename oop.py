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
            
    def remove_bombs(self, rx, ry):
        self.rx = rx
        self.ry = ry
        if (self.rx, self.ry) not in self.grid["bombs"]:
            print("The location specified has no bombs")
        else:
            self.grid["bombs"].remove((self.rx, self.ry))

    def get_bombs(self):
        print("the bombs are at:", self.grid["bombs"] )



class Turtle():
    
    def __init__(self):
        self.location = (0, 0)
        self.lives = 3
    
    
    def get_location(self):
        print("You are currently at:", self.location)
        
        
    def move(self, order):
        self.order = order
        
        if self.order == "up":
            if self.location[1] + 1 > Grid().grid["size"][1]:
                print("Can not go up any more, you have reached the top of the board")
            else:
                self.location = self.location[1] + 1
        
        if self.order == "down":
            if self.location[1] -1 < Grid().grid["size"][1]:
                print("Can not go down any more, you have reached the bottom of the board")
            else:
                self.location = self.location[1] - 1
            
        elif self.order == "right":
            if self.location[0] + 1 > Grid().grid["size"][0]:
                print("Can not go right any more, you have reached the end of the board")
            else:
                self.location = self.location[0] + 1
            
        elif self.order == "left":
            if self.location[0] - 1 < Grid().grid["size"][0]:
                print("Can not go left any more, you have reached the beggining of the board")
            else:
                self.location = self.location[0] - 1
    
            
    def check_bombs(self):
        if self.location in Grid().grid["bombs"]:
            print("YOU HAVE EXPLODED")
            self.lives -= 1
            Grid().grid["bombs"].remove(self.location)
            if self.lives == 0:
                print("YOU HAVE NO MORE LIVES - GAME OVER")
                return False
        else:
            return True
        
    def check_exit(self):
        if self.location == Grid().grid["exit"]:
            print("SUCCESS YOU HAVE EXITED THE MAZE")
            return True
        else:
            return False
            
            


def game():
    a_grid = Grid()
    a_turtle = Turtle()

        
    y = int(input("Please type the heigth of the board: "))
    x = int(input("Please type the lenght of the board "))
    
    a_grid.set_size(x, y)
    
    b = int(input("How many bombs do you want to have: "))
    
    bomb_count = 1
    while bomb_count <= b:
        print("Place bomb number", bomb_count)
        bx = int(input("place bomb \'bomb_count\' in x axis "))
        yx = int(input("place bomb \'bomb_count\' in y axis "))
        a_grid.add_bombs(bx, yx)
        bomb_count += 1
        
    print("Where do you want the exit to be:")
    
    ex = int(input("Exit coordinate for X axis: "))
    ey = int(input("Exit coordinate for Y axis: "))
    
    a_grid.set_exit(ex, ey)
    
    print("Where do you want to start: ")
    
    sx = int(input("Start coordinate for X axis "))
    sy = int(input("Start coordinate for Y axis"))
    
    a_grid.set_start(sx, sy)
    
    while a_turtle.lives > 0:
        
        order = input("Where do you want to go in the board? Options: up, down, left, right ")
        a_turtle.move(order.lower())
        if a_turtle.check_bombs():
            a_turtle.check_exit
        else:
            break
        
game()