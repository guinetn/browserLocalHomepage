## ANAGRAMS (PERMUTATIONS)

Two strings are said to be anagrams of one another if you can turn the first string into
the second by rearranging its letters

table / bleat
tear / rate



1. Brute force O(n!)

list off all permutations of the first string and see if any of them are equal to the second string

```cs
private boolean areAnagrams(String first, String second) {
    return areAnagramsRec("", first, second);
}
private boolean areAnagramsRec(String soFar, String remaining, String target) {
    if (remaining.length() == 0) {
        return soFar.equals(target);
    }
    for (int i = 0; i < remaining.length(); i++) {
        String whatsLeft = remaining.substring(0, i) + remaining.substring(i+1);
        if (areAnagramsRec(soFar + remaining.charAt(i), whatsLeft, target)) 
            return true;
    }
    return false;
}
```

2. Sorting

With a standard sorting algorithm like quicksort or heapsort, it runs in time O(n log n). 
Using counting sort, this will run in time O(n) (~ histogram approach)

```cs
private boolean areAnagrams(String first, String second) {
    char[] one = Arrays.sort(first.toCharArray());
    char[] two = Arrays.sort(second.toCharArray());
    return Arrays.equals(one, two);
}
```

3. Counting Characters

```cs
private boolean areAnagrams(String first, String second) {
    if (first.length() != second.length()) return false;
    for (int i = 0; i < first.length(); i++) {
        char currCh = first.charAt(i);
        if (numCopiesOf(currCh, first) != numCopiesOf(currCh, second)) 
            return false;
    }
    return true;
}
private int numCopiesOf(char ch, String str) {
    int result = 0;
    for (int i = 0; i < str.length(); i++) {
        if (str.charAt(i) == ch) 
            result++;
    }
    return result;
}
```

```cs
private boolean areAnagrams(String first, String second) {
    for (char ch = 'a'; ch <= 'z'; ch++) {
        if (numCopiesOf(ch, first) != numCopiesOf(ch, second)) {
            return false;
    }
}
return true;
}
private int numCopiesOf(char ch, String str) {
    int result = 0;
    for (int i = 0; i < str.length(); i++) {
        if (str.charAt(i) == ch) 
        result++;
    }
return result;
}
```

4. Histogramming O(n) time  O(1) space

Building a frequency histogram of the characters in each string and checking whether those histograms are the same

```cs
private boolean areAnagrams(String first, String second) {
    if (first.length() != second.length()) return false;
    int[] frequencies = new int[26];
    for (int i = 0; i < first.length(); i++) 
        frequencies[first.charAt(i) – 'a']++;    
    for (int i = 0; i < second.length(); i++) {
        if (frequencies[second.charAt(i)] == 0) 
            return false;
        frequencies[second.charAt(i)]--;
    }
    return true;
}
```
Plausible approaches to determine if two strings are anagrams:

Sorting both strings should produce the same resulting string. This takes O(nlgn) time and O(lgn) space.
If we map each character to a prime number and we multiply each mapped number together, anagrams should have the same multiple (prime factor decomposition). This takes O(n) time and O(1) space.
Frequency counting of characters will help to determine if two strings are anagrams. This also takes O(n) time and O(1) space.

|||
|---|---|
|O(n)  |  Sort and Compare|
|      |  Count and Compare|
|O(n²) |  Checking Off|
|n!    |  All possibilities |
|n=5   |  120|
|n=10  |  3,628,800|
|n=20  |  2,432,902,008,176,640,000|



```cs
function anagramCheckingOff (string1, string2) {
  if (string1.length !== string2.length) return false

  const string2ToCheckOff = string2.split('')

  for (let i = 0; i < string1.length; i++) {
    let letterFound = false
    for (let j = 0; j < string2ToCheckOff.length; j++) {
      if (string1[i] === string2ToCheckOff[j]) {
        string2ToCheckOff[j] = null
        letterFound = true
        break
      }
    }
    if (!letterFound) return false
  }

  return true
}

assert.equal(true, anagramCheckingOff('abcd', 'dcba'))
assert.equal(false, anagramCheckingOff('abcd', 'abcc'))
```

## More    
- https://bradfieldcs.com/algos/analysis/an-anagram-detection-example/
    
    
