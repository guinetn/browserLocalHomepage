# ALGORITHMS OPTIMIZATION

Divide & Conquer

download.page(computer_science/algorithms/recursion.md)

## Memoization

An optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again

caching technique for function call
Making long recursive/iterative functions run much faster.
Memoization is another good use case for curry function.

Dynamic Programming store the solution to a problem so we do not need to recalculate it. Memoisation is the act of storing a solution.

```js
//We can beef up our module by adding functions later
var Memoizer = (function(){
    //Private data
    var cache = {};
    //named functions are awesome!
    function cacher(func){
        return function(){
        var key = JSON.stringify(arguments);
        if(cache[key]){
            return cache[key];
        }
        else{
            val = func.apply(this, arguments);
            cache[key] = val;
            return val;
        }
    }
    }    
    //Public data
    return{
        memo: function(func){
        return cacher(func);
        }
    }
})()


var fib = Memoizer.memo(function(n){
    if (n < 2){
        return 1;
    }else{
        return fib(n-2) + fib(n-1);
    }
});

fib(10); ...........
fib(10); 89   // Doesn't have to recalculate anything
fib(7);  21   // Doesn't have to recalculate anything
fib(11); ...loading... 144  // already cached fib(1-10) so faster
```

* Fibonacci sequence

```python
def F(n):
	if n == 0 or n == 1:
		return n
	else:
		return F(n-1)+F(n-2)
```

```python
# Fibonacci sequence with memoization
def fibonacciVal(n):
	memo[0], memo[1] = 0, 1
	for i in range(2, n+1):
		memo[i] = memo[i-1] + memo[i-2]
	return memo[n]
```



