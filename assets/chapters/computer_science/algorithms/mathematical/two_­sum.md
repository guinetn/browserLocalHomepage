##  Two ­Sum Problem

Given an array A[] of n numbers and another number s
Determines whether or not there exist two elements in A whose sum is exactly s. 

Examples: 
Input: arr[] = {0, -1, 2, -3, 1}
        sum = -2  
Output: -3, 1 (1 + (-3) = -2)

Input: arr[] = {1, -2, 1, 0, 5}
       sum = 0
Output: -1. No valid pair exists

[1, 3, 7] and k = 8 answer is "yes" 
given k = 6 the answer is "no"

1. Brute Force

Takes O(n²) time in the worst­ case. Not considered a "good" solution because better options exist
Uses only O(1) space (no auxiliary structures created)


```cs
using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

namespace Test {
    
    public class Program {

        public static void Main() {            
            var a = new int[] {1, 3, 7};
            Console.WriteLine(sumsToTarget(a , 8));               
            Console.WriteLine(sumsToTarget(a , 6));               
        }

        public static bool sumsToTarget(int[] arr, int k) {            
            for (int i = 0; i < arr.Count(); i++) {
                for (int j = i + 1; j < arr.Count(); j++) {
                   if (arr[i] + arr[j] == k) 
                        return true;
                }
            }
            return false;
        }
  }
}
```

2. HashSet

Insert all the elements into an hash table. Scan over it and check for each element A[i], whether there's another element A[j] in the array where A[j] = k – A[i]. 
Solution must handles duplicated elements case (doesn pair an element with itself)
Expected running time O(n): n insertions + n lookups in a hash table takes expected time O(n)
Uses space O(n)

```cs
using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;


namespace Test {
    
    public class Program {

        public static void Main() {            
            var a = new int[] {1, 3, 7};
            Console.WriteLine(sumsToTarget(a , 8));               
            Console.WriteLine(sumsToTarget(a , 6));               
        }

        public static bool sumsToTarget(int[] arr, int k) {
            
            var values = new HashSet<int>();            
            for (int i = 0; i < arr.Count(); i++) {
                if (values.Contains(k - arr[i])) 
                   return true;
                values.Add(arr[i]);
            }

            return false;
        }
    }        
}
```

3. Sorting + Binary Search

~ hashing approach except we sort the array elements and use binary search to test if a pair appears.
Runs in O(n log n): it takes O(n log n) time for a standard sort + cost of n binary searches is O(n log n)
Space usage: depends on sorting algorithm used. Quicksort take O(log n) space, heap sort uses O(1) space. "Pretty good solution": speed up  using a better sorting algorithm and a different observation about the sorted array

```cs
using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

namespace Test {
    
    public class Program {

        public static void Main() {            
            var a = new int[] {1, 3, 7};
            Console.WriteLine(sumsToTarget(a , 8));               
            Console.WriteLine(sumsToTarget(a , 6));               
        }

        public static bool sumsToTarget(int[] arr, int k) {   
            
            Array.Sort(arr);
            for (int i = 0; i < arr.Count(); i++) {
                int siblingIndex = Array.BinarySearch(arr, k - arr[i]);
                    if (siblingIndex >= 0) { // Found it!
                        /* 
                        If this points at us, then the pair exists only if there is another copy of the element. Look ahead of us and behind us */
                        if (siblingIndex != i  // It must not points to us
                            // Points to us ? Then the pair exists only if there is another copy of the element (As the array is sorted, just before of after). Look ahead of us and behind us
                            || (i > 0 && arr[i-1] == arr[i]) 
                            || (i < arr.Count() - 1 && arr[i+1] == arr[i])) {
                            return true;
                        }
                 }
            }         
            return false;
        }
  }
}
```

4. Sorting and Walking Inward

Sort the array then walk two pointers inward from the ends of the array
At each point looking at their sum
If it's exactly k, then we're done. 
If it exceeds k, then any sum using the larger element is too large, so we walk that pointer inwards. 
If it's less than  k, then any sum using the lower element is too small, so we walk that pointer inwards.
Runtime depends on the sorting algorithm. Standard sort takes O(n log n). Radix sort takes time O(n log U), where U is the largest element of the array, because of the cost of the sort. 
Takes space O(log n) if quicksort or radix sort and O(1) if you use heapsort. 
"Good solution": faster than the sort­ and ­binary­search approach using a regular sort and is likely to be faster asymptotically if you use radix sort.

```cs
using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

namespace Test {
    
    public class Program {

        public static void Main() {            
            var a = new int[] {1, 3, 7};
            Console.WriteLine(sumsToTarget(a , 8));               
            Console.WriteLine(sumsToTarget(a , 6));               
        }

        public static bool sumsToTarget(int[] arr, int k) {   
            
            Array.Sort(arr);
            int lhs = 0, rhs = arr.Count() - 1;
            while (lhs < rhs) {
                int sum = arr[lhs] + arr[rhs];
                if (sum == k) 
                    return true;
                else if (sum < k) 
                    lhs++;
                else 
                    rhs--;
            }
            return false;
        }
  }
}
```
