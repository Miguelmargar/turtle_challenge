import json

with open("exit.txt", "r") as f:
    data = f.read()
    exit = json.loads(data)

print(len(exit))

with open("grid.txt", "r") as f:
    data = f.read()
    grid = json.loads(data)

print(grid["position"])