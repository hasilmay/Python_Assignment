#Random numbers
import random
#generate 5 random float numbers between 0 and 10
random_floats = [random.uniform(0, 10) for _ in range(5)]

#calculating min & max using functions
min_val = min(random_floats)
max_val = max(random_floats)

print("Generated numbers:", random_floats)
print("Min:", min_val)
print("Max:", max_val)