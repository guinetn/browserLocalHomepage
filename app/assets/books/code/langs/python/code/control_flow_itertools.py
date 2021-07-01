# itertools
# Functions creating iterators for efficient looping

- https://docs.python.org/3/library/itertools.html

## Infinite iterators:
count(10)                                       10 11 12 13 14 ...
cycle('ABCD')                                   A B C D A B C D ...
repeat(10, 3)                                   10 10 10

## Iterators terminating on the shortest input sequence:

accumulate([1,2,3,4,5])                         1 3 6 10 15
chain('ABC', 'DEF')                             A B C D E F
chain.from_iterable(['ABC', 'DEF'])             A B C D E F
compress('ABCDEF', [1,0,1,0,1,1])               A C E F
dropwhile(lambda x: x<5, [1,4,6,4,1])           6 4 1
filterfalse(lambda x: x%2, range(10))           0 2 4 6 8
islice('ABCDEFG', 2, None)                      C D E F G
starmap(pow, [(2,5), (3,2), (10,3)])            32 9 1000
takewhile(lambda x: x<5, [1,4,6,4,1])           1 4
zip_longest('ABCD', 'xy', fillvalue='-')        Ax By C- D-

## Combinatoric iterators:

product('ABCD', repeat=2)                       AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
permutations('ABCD', 2)                         AB AC AD BA BC BD CA CB CD DA DB DC
combinations('ABCD', 2)                         AB AC AD BC BD CD
combinations_with_replacement('ABCD', 2)        AA AB AC AD BB BC BD CC CD DD