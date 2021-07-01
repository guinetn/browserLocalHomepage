# Python 3.7
import math  # Used for trigonometric functions, log, pow, etc.

# nulber, target base, expected
data=[
(769, 10, 769),
(769, 16, 301),
(769, 2, 1100000001),
(10, 16, 'A'),
(10, 2, 1010),
(255, 10, 255),
(255, 2, 11111111),
(255, 16, 'FF'),
(1453, 16, '5AD'),
(276, 16, 114),
(276, 8, 424),
(276, 10, 276),
(276, 2, 100010100),
(276, 2, 'MUST_FAILED')
]


sets='0123456789ABCDEF'
def convert(entry, base):
    if entry<base:
        return sets[entry]

    divisor = entry//base
    remainder = entry%base
    return convert(divisor, base) + sets[remainder];

def testConvert(v):    
    entry, base, expected = v  
    result = convert(entry,base)
    test = '' if result==str(expected) else f"--> FAILED, EXPECT '{expected}'"
    print(f"{entry} in base {base} = {result} {test}")


if __name__ == '__main__':	
    print('')       
    
    res = map(testConvert, data)
    for x in res:
        pass


            

	
