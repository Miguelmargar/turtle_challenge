import json

with open("grid.txt", "r") as f:
    data = f.read()
    grid = json.loads(data)


with open("exit.txt", "r") as f:
    data = f.read()
    instructions = json.loads(data)


def moves():
    x = grid["position"][0]
    y = grid["position"][1]  
    
    for i in instructions:
          
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
            print(grid["position"])
                
    if grid["position"] == grid["mines"][0:-1]:
        return "Turtle explosion"
        
    if grid["position"] == grid["exit"]:
        return "Turtle exit successful"
                
    if grid["position"] != grid["mines"][0:-1] and grid["position"] != grid["exit"][0]:
        return "Turtle still in danger"

print(moves())

        
        