## Prime number

A number wich has only 1 and itself as divisors

||Complexity|Time|Explanation|
|---|---|---|---|
|1.| O(N) | 80 sec. | Check all divisors giving a zero modulo in a loop from [2 ; N–1]|
|2.| O(N/2) | 40 sec. |Even divisors can be avoided. At start check N%2==0, if not then check all odd divisors in the loop (divisor=3; divisor+=2)|
|3.| O((✓N)/2) | 0.02 sec |A divisible number has symmetrical pairs of divisors. 24 has (2,12), (3,8), (4,6) If a number is divisible, there is necessarily a divisor to the left of its root square:  2 3 4 → ✓24 ← 6 8 12|
