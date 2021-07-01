# random

import random
random.random() 		# a random float number between 0.0 to 1.0:  0.645173684807533
random.randint(0, 10) 	# a random integer between 0 and 10
random.randint(1,100) 	# a random integer between the specified integers.  ie: 95

#random.randrange(start, stop, step): Returns a randomly selected element from the range created by the start, stop and step arguments. The value of start is 0 by default. Similarly, the value of step is 1 by default.
random.randrange(1,10)		# 2
random.randrange(1,10,2)  	# 5   from [1 3 5 7 9]
random.randrange(0,101,10) 	# 80  from [0 10 20 30 40 50 60 70 80 90 100]

randoom.choice('computer')				# 't'.  randomly selected element from a non-empty sequence. An empty sequence as argument raises an IndexErro
random.choice([12,23,45,67,65,43]) 		# 45
random.choice((12,23,45,67,65,43))      # 67

random.uniform(7.5, 9.5) 


# Choose from the list randomly.
random_options = ['apple', 'pear', 'banana']
random_choice = random.choice(random_options)  # i.e. 'apple'
assert random_choice in random_options

# Sampling without replacement.
random_sample = random.sample(range(100), 10)  # i.e. [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
for sample in random_sample:
    assert 0 <= sample <= 100

# Choose random number.
random_float = random.random()  # i.e. 0.17970987693706186
assert 0 <= random_float <= 1

# Random integer chosen from range(6)
random_integer = random.randrange(6)  # i.e. 4
assert 0 <= random_integer <= 6




# shuffle: randomly reorders the elements in a list.
numbers=[12,23,45,67,65,43]
random.shuffle(numbers)   
numbers
[23, 12, 43, 65, 67, 45]
random.shuffle(numbers)
numbers
[23, 43, 65, 45, 12, 67]


import random
[random.random() for _ in range(4)]    # produces 4 numbers uniformly between 0 and 1

from numpy.random import rand
X = rand(100)  # 100 points



import matplotlib.pyplot as plt
from numpy.random import rand
X = rand(100)  # 100 points
y = rand(100)
plt.scatter(X, y)
plt.show()


import random
four_uniform_randoms = [random.random() for _ in range(4)]    # produces numbers uniformly between 0 and 1
# [0.8444218515250481, 0.7579544029403025, 0.420571580830845, 0.25891675029296335] 	

# produces pseudorandom (deterministic) numbers based on an internal state that you can set with random.seed to get reproducible results:
random.seed(10) 
print random.random() 	# 0.57140259469
random.seed(10) 	# reset the seed to 10
print random.random() 	# 0.57140259469 again

my_best_friend = random.choice(["Alice", "Bob", "Charlie"]) # randomly pick one element from a list 

random.randrange(10) 	# choose randomly [0, 1, ..., 9]
random.randrange(3, 6) 	# choose randomly [3, 4, 5]  [3..6[

up_to_ten = range(10) 	    # 1-10	
random.shuffle(up_to_ten)   # randomly reorders the elements of a list:

lottery_numbers = range(60) 			    # randomly choose a sample of elements without replacement (no duplicates)
winning_numbers = random.sample(lottery_numbers, 6) # [16, 36, 10, 6, 25, 9]


four_with_replacement = [random.choice(range(10)) for _ in range(4)]  # Sample of elements with replacement (allowing duplicates)

def random_kid():
	return random.choice(["boy", "girl"])
random.seed(0)
for _ in range(10000):
	younger = random_kid()
                                                                      # [9, 4, 4, 2] 

n = 10
a = [[random.randint(0, 10) for _ in range(random.randint(3, 5))] for _ in range(n)]                                                                      


import numpy as np
n = 10
df = pd.DataFrame(
    {
        "col1": np.random.random_sample(n),
        "col2": np.random.random_sample(n),
        "col3": [[random.randint(0, 10) for _ in range(random.randint(3, 5))] for _ in range(n)],
    }
)

col1	col2	col3
0	0.162344	0.732179	[3, 1, 10, 9]
1	0.764896	0.418250	[0, 2, 8, 3]
...
9	0.647189	0.718494	[0, 0, 7, 4]