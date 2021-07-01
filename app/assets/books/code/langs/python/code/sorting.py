x = [4,1,2,3]

largest_value = max(x) 
smallest_value = min(x) 

sorted_values = sorted(x)
smallest_value = sorted_values[0] 
second_smallest_value = sorted_values[1] 
second_largest_value = sorted_values[-2]


y = sorted(x) # is [1,2,3,4], x is unchanged
x.sort() # now x is [1,2,3,4]

By default, sort, sorted sort a list from smallest → largest 

# reverse=True: sorted from largest → smallest 
# sort the list by absolute value from largest to smallest
x = sorted([-4,1,-2,3], key=abs, reverse=True) # is [-4,3,-2,1]

# Custom sort
# sort the words and counts from highest count to lowest
wc = sorted(word_counts.items(), key=lambda (word, count): count, reverse=True)

