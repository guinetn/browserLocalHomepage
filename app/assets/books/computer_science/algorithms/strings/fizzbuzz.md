## Fizz-Buzz

A test of programming ability
Write a program that prints the numbers from 1 to 100, but
* for multiples of three print "Fizz" instead of the number 
* for the multiples of five print "Buzz"
* for numbers which are multiples of both three and five print "FizzBuzz"

why is hard ?
The structure of the if statements is tricky, there are two tests for the same condition 

for(int x = 1; x <= 100; x++) {
	string output = "";
	if(x%3 == 0) output += "Fizz";
	if(x%5 == 0) output += "Buzz";
	if(output == "") output = x.ToString();
	Console.WriteLine(output);
}