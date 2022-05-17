import random
def roll_dice(num=1, sides=6, mod=0):
    for i in range(1,num+1):
        mod += random.randint(1,sides)
    return mod

print(roll_dice(2,44,7))
print(roll_dice(5,82))
print(roll_dice(1,30))
