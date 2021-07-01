### Radix Sort

- https://www.youtube.com/watch?v=XiuSW_mEn7g

It's all about grouping together elements by place values. 
Take radix LSD base 10 for example. Since our number system is base 10, this makes sense. 
Let's say our list is: 
986, 354, 209, 4, 59, 86
 
1. Pad everything to three digits with zeroes: 
986, 354, 209, 004, 059, 086.
2.Now group these numbers together based on their least significant digit (ones place), while maintaining the original order within each group:
[354, 004] [986, 086] [209, 059]
See that the numbers ending in 4 are in one group, the numbers ending in 6 are in another, and so on.
Note that since 354 came before 004 in the original list, that order is maintained within the "4s" group.
3. Removing the brackets, the list is now:
354, 004, 986, 086, 209, 059
4. Now, look at the second-to-least significant digit (tens place) and group them by this digit again, while maintaining keeping the elements of each group in the same order they were in at the end of the last step:
[004, 209] [354, 059] [986, 086]
004, 209, 354, 059, 986, 086
 
5. Now repeat for the final digit, the 100s place.
[004, 059, 086] [209] [354] [986]
004, 059, 086, 209, 354, 986
4, 59, 86, 209, 354, 986
 
6. The list is now sorted.
 
Radix MSD goes from highest place value to lowest instead of lowest-to-highest.
The base refers to what base number system is used for place values. For example, the number 17 is 11 in hexadecimal (base 16) and 10001 in binary (base 2).