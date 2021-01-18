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