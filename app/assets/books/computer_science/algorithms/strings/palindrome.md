## PALINDROME

A word, phrase, number, or other sequence of characters which reads the same backward or forward
Axa, radar, toot, madam
"A man, a plan, a canal, Panama"
  
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar.

Ways to determine if a string is a palindrome:
- Reverse the string and it should be equal to itself. (spaces included?)
- Have two pointers at the start and end of the string. Move the pointers inward till they meet. At any point in time, the characters at both pointers should match.
- use a deque: remove both last/first of them directly, we can compare them and continue only if they match. If we can keep matching first and the last items, we will eventually either run out of characters or be left with a deque of size 1 depending on whether the length of the original string was even or odd. In either case, the string must be a palindrome.

```cs
IsPalindrome Recursive public static bool IsPalindrome(string text)
{
    if (text.Length <= 1)
        return true;
    else
    {
        if ( text[0] != text[ text.Length - 1 ] )
            return false;
        else
            return IsPalindrome( text.Substring( 1, text.Length-2 ) );
    } 
}
```

```python
from collections import deque

def is_palindrome(characters):
    character_deque = deque(characters)

    while len(character_deque) > 1:
        first = character_deque.popleft()
        last = character_deque.pop()
        if first != last:
            return False

    return True

is_palindrome('lsdkjfskf')   # => False
is_palindrome('radar')   # => True
```

## More

- https://bradfieldcs.com/algos/deques/palindrome-checker/
