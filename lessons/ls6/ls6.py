import random

a,b,c,d = random.choice([True, False]), random.choice([True, False]), random.choice([True, False]), random.choice([True, False])

f_1 = not a and (b or c) or d

print (f_1)

f_2 = (a or b) and (not c and d)

print (f_2)