### Binary (base 2)

`Bits` 
Binary numbers: the 0s and 1s common to digital computers
A bit is a binary digit - 0 or 1, true or false, on or off. 

`Bytes`
Eight bits is a byte, which is the basic unit of information that computers work with.

`Nibble`
4 bits

|  Binary | Decimal| 2^x |
|---|---|---|
|00000001| 1|    0|
|00000010| 2|    1|
|00000100| 4|    2|
|00001000| 8|    3|
|00010000| 16|   4|
|00100000| 32|   5|
|01000000| 64|   6|
|10000000| 128|  7|
|11111111| 255|  8|
| 8 bits = 1 byte|||

## Snippets
Test k<sup>th</sup> bit is set: num & (1 << k) != 0.
Set k<sup>th</sup> bit: num |= (1 << k).
Turn off k<sup>th</sup> bit: num &= ~(1 << k).
Toggle the k<sup>th</sup> bit: num ^= (1 << k).
To check if a number is a power of 2, num & num - 1 == 0.
 
## Convert decimal to binary
* Divide the number by 2
* Get the integer quotient for the next iteration
* Get the remainder for the binary digit (order is reverse, read from last quotient)
* Repeat the steps until the quotient is equal to 0

<pre>
        13 ÷ 2
  R  ▲   1   └─ 6 ÷ 2
  E  |          0   └─ 3 ÷ 2
  A  |                 1   └─ 2 ÷ 2
  D  |                        1 
                            
13 (Base 10) → 1101 (Base 2)
</pre>

## Procedure to convert from base 10 to any base
1. Divide the number by the base to get the remainder. ...
2. Repeat the process by dividing the quotient of step 1, by the new base. ...
3. Repeat this process until your quotient becomes less than the base.

  6954¹⁰ = 15452⁸
  8 | 6954
  8 | 869 → → → 2
  8 | 108 → → 5
  8 | 13 → → 4
  8 | 1 → → 5
  0 → → 1

  4823¹⁰ = 12D7¹⁶
  16 | 4823
  16 | 3017 → 7
  16 | 18 → → 13 (= D)
  16 | 1 → → 2
  0 → → 1


  49¹⁰ = 110001²
  2 | 49
  2 | 24 → → → → 1
  2 | 12 → → → 0
  2 | 6 → → 0
  2 | 3 → 0
  2 | 1 → 1
  0 → 1

## Convert to base 2

![](assets/chapters/computer_science/assets/convert_to_base_2.png)
## Convert to base 10

  So C14A¹⁶ = 49482¹⁰
  C14A¹⁶ = (12 x 16³) + (1 x 16²) + (4 x 16¹) + 10 x 16⁰)
        = (12 x 4096) + (1 x 256) + (4 x 16) + (10 x 1) = 49482
      
  61732⁸ = 25562¹⁰
  61732 = (6 x 4096) + (1 x 512) + (7 x 64) + (3 x 8) + (2 x 1)
        = 24576 + 512 + 448 + 24 + 2

  So 100111² = 39¹⁰
  100111² = (1 x 2⁵) + (1 x 2²) + (1 x 2¹) + ( 1 x 2⁰) = 39



JAVASCRIPT - DISPLAY BIN, HEXADECIMAL 
```js
var i=19;
console.log(`19 (b10) = ${i.toString(2)} (b2)`); 
console.log(`19 (b10) = ${i.toString(8)} (b8)`); 
console.log(`19 (b10) = ${i.toString(16)} (b16)`); 
19 (b10) = 10011 (b2)
19 (b10) = 23 (b8)
19 (b10) = 13 (b16)

function toBinary(n)
{
    if (n < 2) return n;
    var divisor =  Math.trunc(n / 2);
    var remainder = n % 2;
    return toBinary(divisor) + '' + remainder;
}
toBinary(13);
```

Convert from base 10 to any base
```js
const sets='0123456789ABCDEF';
function convert(input, base) {
    if (input < base) return sets[input];
    const divisor =  Math.trunc(input/base);
    const remainder = input % base;
    return convert(divisor, base) + '' + sets[remainder];
}

const data=[
'769→10=769',
'769→16=301',
'769→2=1100000001',
'10→16=A',
'10→2=1010',
'255→10=255',
'255→2=11111111',
'255→16=FF',
'1453→16=5AD',
'276→16=114',
'276→8=424',
'276→10=276',
'276→2=100010100',
'276→2=MUST_FAILED'
]

data.map((x) => { 
	let z=x.split('→');
	const input=z[0]; 
	const baseTest=z[1].split('=');
	const base = baseTest[0]; 
	const result = convert(input*1,base*1);
	console.log(`${input} in base ${base} = ${result} ${result==baseTest[1] ? '✔️' : '❌'}`) });
```

C# - DISPLAY BIN, HEXADECIMAL 
```csharp
int value = 13;
string binary = Convert.ToString(value, 2); // To Binary
value = Convert.ToInt32("1101", 2);         // From Binary

int v = 19;
string hexValue = v.ToString("x")); // To Hex
hexValue = v.ToString("X"));
hexValue = v.ToString("X2"));
hexValue = v.ToString("X8"));
int value = 0x2045e;
hexValue = value.ToString("X"));
int.Parse(hexValue, System.Globalization.NumberStyles.HexNumber));

// Convert from any base to any base 
// Supported bases: 2, 8, 10, 16
String number = "1101";
int fromBase = 2;
int toBase = 10;
String result = Convert.ToString(Convert.ToInt32(number, fromBase), toBase);
```