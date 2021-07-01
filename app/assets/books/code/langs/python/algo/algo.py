# Finding Max Number
findmax = lambda x,y: x if x > y else y 
findmax(5,14) # or max(5,14)


# Fizzbuz
['FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else i  for i in range(1,20)]

# Palindrome: a number or a string that looks the same when it gets reversed.
text = 'level'
ispalindrome = text == text[::-1]
print(ispalindrome)

# anagram
def check_anagram(first_word, second_word):
  return sorted(first_word) == sorted(second_word)
  
print(check_anagram("silent", "listen"))   # True
print(check_anagram("ginger", "danger"))   # False

# Fibonacci: each number ( Fibonacci number ) is the sum of the two preceding numbers.
fibo = [0,1]
[fibo.append(fibo[-2]+fibo[-1]) for i in range(5)]
print(fibo) # [0, 1, 1, 2, 3, 5, 8]

# Prime Number
# A prime number is a number that is divisible only by itself and 1. eg: 2,3,5,7 etc. To generate prime numbers in a range we can use the list function with filter and lambda to generate prime numbers.
list(filter(lambda x:all(x % y != 0 for y in range(2, x)), range(2, 13)))
# [2, 3, 5, 7, 11]

# Square of all numbers in a given range
from itertools import repeat
n = 5
squares = map(pow, range(1, n), repeat(2))
print(squares)   # [1, 4, 9, 16, 25]


# most frequent in a list
def mostfreq(n):
        return max( set(n), key = n.count )