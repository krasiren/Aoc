with open('in.txt') as f:
    lines = f.read().splitlines()

maxCalories = [0, 0, 0]
currentCalories = 0
for line in lines:
    if line != '':
        currentCalories += int(line)
    else:
        if currentCalories > maxCalories[0]:
            maxCalories[0] = currentCalories
        elif currentCalories > maxCalories[1]:
            maxCalories[1] = currentCalories
        elif currentCalories > maxCalories[2]:
            maxCalories[2] = currentCalories

        currentCalories = 0

print(maxCalories[0])   # part one
print(sum(maxCalories)) # part two