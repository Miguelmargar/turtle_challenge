from random import choice

class Grid():
    
    def __init__(self):
        
        self.grid = {
            "size": [0, 0],
            "bombs": [],
            "start": [0, 0],
            "exit": [0, 0]
        }
        
        self.random = "no"
        
        self.boardSizeMin = 0
        self.boardSizeMax = 0
        self.bomb_count_min = 0
        self.bomb_count_max = 0
        
    def set_difficulty(self):
        if self.random == "yes": 
            self.difficulty = input("Choose difficulty level (easy/hard): ")
            print()
                
            if self.difficulty == "easy":
                self.boardSizeMin = 3
                self.boardSizeMax = 5
                self.bomb_count_min = 1
                self.bomb_count_max = 2
    
            elif self.difficulty == "hard":
                self.boardSizeMin = 5
                self.boardSizeMax = 10
                self.bomb_count_min = 3
                self.bomb_count_max = 7
        else:
            pass

        
    def set_random(self):
        self.random = input("Do you want to randomise Grid locations? (yes/no): ")
        print()
        
    def set_size(self):
        if self.random == "yes":
            self.y = choice(range(self.boardSizeMin, self.boardSizeMax + 1))
            self.x = choice(range(self.boardSizeMin, self.boardSizeMax + 1))    
        
            self.grid["size"] = [self.x, self.y]
        
        if self.random == "no":
            self.x = int(input("Please type the lenght of the board: "))
            self.y = int(input("Please type the heigth of the board: "))
            
            self.grid["size"] = [self.x, self.y]
        
        
    def get_size(self):
        print("The size of the maze is:", self.grid["size"])
    
    
    def set_start(self):
        if self.random == "yes":
            self.sx = choice(range(self.x))
            self.sy = choice(range(self.y))

            # Check that start location given in not out of board or has bomb in it
            while (self.sx > self.grid["size"][0]) or (self.sy > self.grid["size"][1]) or ([self.sx, self.sy] in self.grid["bombs"]):
                self.sx = choice(range(self.x))
                self.sy = choice(range(self.y))
            
            self.grid["start"] = [self.sx, self.sy]
        
        if self.random =="no":
            big = False
            while not big:
                self.sx = int(input("Start coordinate for X axis: "))
                self.sy = int(input("Start coordinate for Y axis: "))
                
                # Check that start location given in not out of board
                if (self.sx > self.grid["size"][0]) or (self.sy > self.grid["size"][1]):
                    print("Invalid start as parameters given too big")
                elif ([self.sx, self.sy] in self.grid["bombs"]):     
                    print("Invalid start as parameters collide with a bomb")
                else:
                    self.grid["start"] = [self.sx, self.sy]
                    big = True
      
            
    def get_start(self):
        print("The start location is:", self.grid["start"])
    
        
    def set_exit(self):
        if self.random == "yes":
            self.ex = choice(range(self.x))
            self.ey = choice(range(self.y))
            # If exit has bomb get a new exit until exit doesn't have a bomb or is not the start
            while (self.ex, self.ey) in self.grid["bombs"] or (self.ex, self.ey) in self.grid["start"]:
                self.ex = choice(range(self.x))
                self.ey = choice(range(self.y))
            self.grid["exit"] = [self.ex, self.ey]        
        
        if self.random =="no":
            print("Where do you want the exit to be: ")
            self.ex = int(input("Exit coordinate for X axis: "))
            self.ey = int(input("Exit coordinate for Y axis: "))
            print()
            if self.ex > self.grid["size"][0] and self.ey > self.grid["size"][1]:
                print("invalid start as parameters given too big")
            else:
                self.grid["exit"] = [self.ex, self.ey]
       
            
    def get_exit(self):
        print("The exit is:", self.grid["exit"])
    
        
    def add_bombs(self):
        if self.random == "yes":
            self.b = 1
            self.bomb_count = choice(range(self.bomb_count_min, self.bomb_count_max))
            while self.b < self.bomb_count:
                self.bx = choice(range(self.x)) 
                self.by = choice(range(self.y))
                self.grid["bombs"].append([self.bx, self.by])
                self.b += 1
                
        # if not random
        if self.random == "no":
            # ask user how many bombs
            self.b = int(input("How many bombs do you want to have: "))
            print()
            self.bomb_count = 1
            self.bc_str = str(self.bomb_count)
            # put number of bombs selected by user
            while self.bomb_count <= self.b:
                print("Place bomb number:", self.bomb_count)
                self.bx = int(input("place bomb " + self.bc_str + " in x axis: "))
                self.by = int(input("place bomb " + self.bc_str + " in y axis: "))
                print()
                # if bomb location is not in grid ask for a new one else place
                if self.bx > self.grid["size"][0] and self.by > self.grid["size"][1]:
                    print("invalid start as parameters given too big")
                    print()
                else:
                    self.grid["bombs"].append([self.bx, self.by])
                    self.bomb_count += 1
          
            
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
    
    def __init__(self, obj):
        self.obj = obj
        self.location = self.obj.grid["start"]
        self.lives = 3
    
    
    def get_location(self):
        print("You are currently at:", self.location)
        
        
    def move(self):
        while self.lives > 0 and self.check_exit() == False:
        
            self.order = input("Where do you want to go in the board? Options: up, down, left, right ")

            if self.order == "up":
                if self.location[1] + 1 > self.obj.grid["size"][1]:
                    print("Can not go up any more, you have reached the top of the board")
                else:
                    self.location[1] += 1
            
            if self.order == "down":
                if self.location[1] -1 < 0:
                    print("Can not go down any more, you have reached the bottom of the board")
                else:
                    self.location[1] -= 1
                
            elif self.order == "right":
                if self.location[0] + 1 > self.obj.grid["size"][0]:
                    print("Can not go right any more, you have reached the end of the board")
                else:
                    self.location[0] += 1
                
            elif self.order == "left":
                if self.location[0] - 1 < 0:
                    print("Can not go left any more, you have reached the beggining of the board")
                else:
                    self.location[0] -= 1
            
            self.check_bombs()
            
            self.get_location()
            
    def check_bombs(self):
        if self.location in self.obj.grid["bombs"]:
            print("YOU HAVE EXPLODED")
            self.lives -= 1
            self.obj.grid["bombs"].remove(self.location)
            if self.lives == 0:
                print("YOU HAVE NO MORE LIVES - GAME OVER")
                return False
        else:
            return True
        
    def check_exit(self):
        if self.location == self.obj.grid["exit"]:
            print("SUCCESS YOU HAVE EXITED THE MAZE ")
            print()
            return True
        else:
            return False
      



def game():
    
    play = True
    
    while play:
        
        # Intantiate grid
        a_grid = Grid()
    
        # Set randomness
        a_grid.set_random()
            
        # Set game difficulty
        a_grid.set_difficulty()        
            
        # Set the size
        a_grid.set_size()
        a_grid.get_size()
            
        # Add the bombs    
        a_grid.add_bombs()
        a_grid.get_bombs()
        
        # Set the start
        a_grid.set_start()
        a_grid.get_start()
                
        # Set the exit
        a_grid.set_exit()
        a_grid.get_exit()
    
        # Instantiate Turtle
        a_turtle = Turtle(a_grid)
        
        a_turtle.move()
        
        # Ask if play again
        again = input("Would you like to play again? (yes/no): ")
        
        if again == "yes":
            play = True
        else:
            print("Good bye!")
            play = False
    

game()