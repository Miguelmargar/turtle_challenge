# import json
# import sys

# # For command line use of files give - python3 turtle.py then: 1st provide grid file then provide instruction file needed
# # grid.txt goes with inst.txt and grid_hard.txt goes with inst_hard.txt
# grid_file = sys.argv[1]
# instructions_file = sys.argv[2]

# # Opens instructions file
# with open(instructions_file, "r") as i:
#     data = i.read()
#     instructions = json.loads(data)


# exit = instructions["exit"]
# none = instructions["none"]
# explosion = instructions["explosion"]


# def moves(inst):
#     # opens grid file    
#     with open(grid_file, "r") as g:
#         data = g.read()
#         grid = json.loads(data)
        
#     # move through the grid
#     for i in inst:
#         x = grid["position"][0]
#         y = grid["position"][1]   
          
#         if i == "r":
#             grid["dir"] += 1
#             if grid["dir"] > 3:
#                 grid["dir"] = 0
        
#         if i == "m":
#             if grid["dir"] == 0:
#                 grid["position"] = [x, y + 1]
#             if grid["dir"] == 1:
#                 grid["position"] = [x + 1, y]
#             if grid["dir"] == 2:
#                 grid["position"] = [x, y - 1]
#             if grid["dir"] == 3:
#                 grid["position"] = [x - 1, y]
        
#     # gives out result            
#     if grid["position"] in grid["mines"]:
#         return "Turtle explosion"
        
#     if grid["position"] == grid["exit"]:
#         return "Turtle exit successful"
                
#     if grid["position"] not in grid["mines"] and grid["position"] != grid["exit"][0]:
#         return "Turtle still in danger"
    
# print(moves(explosion))

# print(moves(none))

# print(moves(exit))
        
