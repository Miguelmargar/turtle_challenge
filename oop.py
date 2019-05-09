from random import *

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
            self.x = int(input("Please type the lenght of the board "))
            self.y = int(input("Please type the heigth of the board: "))
            
            self.grid["size"] = [self.x, self.y]
        
        
    def get_size(self):
        print("The size of the maze is:", self.grid["size"])
    
    
    def set_start(self):
        if self.random == "yes":
            big = False
            while not big:
                self.sx = choice(range(boardSizeMax))
                self.sy = choice(range(boardSizeMax))
                
                # Check that start location given in not out of board
                if (self.sx > self.grid["size"][0]) or (self.sy > self.grid["size"][1]) or ([self.sx, self.sy in self.grid["bombs"]]):
                    continue
                else:
                    self.grid["start"] = [self.sx, self.sy]
                    big = True
        
        if self.random =="no":
            big = False
            while not big:
                self.sx = int(input("Start coordinate for X axis: "))
                self.sy = int(input("Start coordinate for Y axis: "))
                
                # Check that start location given in not out of board
                if (self.sx > self.grid["size"][0]) or (self.sy > self.grid["size"][1]):
                    print("Invalid start as parameters given too big")
                elif ([self.sx, self.sy in self.grid["bombs"]]):     
                    print("Invalid start as parameters collide with a bomb")
                else:
                    self.grid["start"] = [self.sx, self.sy]
                    big = True
      
            
    def get_start(self):
        print("The start location is:", self.grid["start"])
    
        
    def set_exit(self, ex, ey, random):
        if self.random == "yes":
            pass
        
        if self.random =="no":
            if ex > self.grid["size"][0] and ey > self.grid["size"][1]:
                print("invalid start as parameters given too big")
            else:
                self.ex = ex
                self.ey = ey
                self.grid["exit"] = [self.ex, self.ey]
            
    def get_exit(self):
        print("The exit is:", self.grid["exit"])
    
        
    def add_bombs(self, bx, by, random):
        if random == "yes":
            pass
        
        if randrange == "no":
            if bx > self.grid["size"][0] and by > self.grid["size"][1]:
                print("invalid start as parameters given too big")
            else:
                self.bx = bx
                self.by = by
                self.grid["bombs"].append([self.bx, self.by])
            
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
        self.location = obj.grid["start"]
        self.lives = 3
    
    
    def get_location(self):
        print("You are currently at:", self.location)
        
        
    def move(self, order):
        self.order = order

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
            return True
        else:
            return False
      



def game():
    
    play = True
    
    while play:
        
        # Intantiate grid
        a_grid = Grid()
    
        a_grid.set_random()
            
        a_grid.set_difficulty()        
            
        a_grid.set_size()
        a_grid.get_size()
            
        #     # place random bombs
        #     b = 1
        #     bomb_count = choice(range(bomb_count_min, bomb_count_max))
        #     while b > bomb_count:
        #         bx = choice(range(boardSizeMax)) 
        #         by = choice(range(boardSizeMax))
        #         a_grid.add_bombs(bx, by)
        #         b += 1
        
        
        a_grid.get_start()
                
        #     # Get exit location
        #     ex = choice(range(boardSizeMax))
        #     ey = choice(range(boardSizeMax))
        #     a_grid.set_exit(ex, ey)
        #     # If exit has bomb get a new exit until exit doesn't have a bomb
        #     while a_grid.set_exit(ex, ey) in a_grid.grid["bombs"]:
        #         ex = choice(range(boardSizeMax))
        #         ey = choice(range(boardSizeMax))
        #         a_grid.set_exit(ex, ey)

            
        #     a_grid.get_start()
        #     print()
            
        
        # # Do not randomise grid settings--------------------------------------------------------------
        # else:    
         
        #     # Place bombs
        #     b = int(input("How many bombs do you want to have: "))
        #     print()
        #     bomb_count = 1
        #     bc_str = str(bomb_count)
        #     while bomb_count <= b:
        #         print("Place bomb number:", bomb_count)
        #         bx = int(input("place bomb " + bc_str + " in x axis: "))
        #         by = int(input("place bomb " + bc_str + " in y axis: "))
        #         print()
        #         a_grid.add_bombs(bx, by)
        #         bomb_count += 1
        
        #     # Place the exit   
        #     print("Where do you want the exit to be: ")
        #     ex = int(input("Exit coordinate for X axis: "))
        #     ey = int(input("Exit coordinate for Y axis: "))
        #     print()
        #     a_grid.set_exit(ex, ey)
          
    
    
        # # Instantiate Turtle
        # a_turtle = Turtle(a_grid)
        
        # # Move turtle around the board
        # while a_turtle.lives > 0 and a_turtle.check_exit() == False:
            
        #     order = input("Where do you want to go in the board? Options: up, down, left, right ")
        #     a_turtle.move(order)
        #     a_turtle.check_bombs()
        #     if a_turtle.check_exit():
        #         print("SUCCESS YOU HAVE EXITED THE MAZE ")
        #         print()
        
        
        # # Ask if play again
        # again = input("Would you like to play again? (yes/no): ")
        
        # if again == "yes":
        #     play = True
        # else:
        #     print("Good bye!")
        #     play = False
    

game()