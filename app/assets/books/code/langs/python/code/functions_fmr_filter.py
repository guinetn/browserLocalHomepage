# FILTER

#  return a new array with all elements that passes the test.

# two parameters
# - an array
# - a test function

ages = range(30)
majeurs = filter(lambda x: x > 18, ages)
print(majeurs)
## [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# Typiquement, ce code peut être remplacé par une liste en intention dans le pur style Python :

majeurs = [a for a in ages if a > 18]
print(majeurs)


values=[0, 1, 2, 3, 4, 5, 6, 7,8,9,10]
def iseven(n):
  if n%2==0:
  	return True
  else:
  	return False

l1=filter(iseven, values)
print(l1)

l1=list(filter(iseven, values))
print(l1)




def filtering(arr, test):
    passed = []
    for element in arr:
        if (test(element)):
            passed.append(element)
    return passed

def isSuperNumber(num):
    return num >= 10

filtering([1, 5, 11, 3, 22], isSuperNumber)  # 11,22