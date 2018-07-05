import json


with open("instructions.txt", "r") as instructions_file:
    data = instructions_file.read()
    instructions = json.loads(data)


exit = instructions["exit"]
none = instructions["none"]
explosion = instructions["explosion"]

def moves(inst):
    
    with open("grid.txt", "r") as grid_file:
        data = grid_file.read()
        grid = json.loads(data)
    
    for i in inst:
        x = grid["position"][0]
        y = grid["position"][1]   
          
        if i == "r":
            grid["dir"] += 1
            if grid["dir"] > 3:
                grid["dir"] = 0
        
        if i == "m":
            if grid["dir"] == 0:
                grid["position"] = [x, y + 1]
            if grid["dir"] == 1:
                grid["position"] = [x + 1, y]
            if grid["dir"] == 2:
                grid["position"] = [x, y - 1]
            if grid["dir"] == 3:
                grid["position"] = [x - 1, y]
                
    if grid["position"] in grid["mines"]:
        return "Turtle explosion"
        
    if grid["position"] == grid["exit"]:
        return "Turtle exit successful"
                
    if grid["position"] not in grid["mines"] and grid["position"] != grid["exit"][0]:
        return "Turtle still in danger"

print(moves(explosion))

print(moves(none))

print(moves(exit))
        
        