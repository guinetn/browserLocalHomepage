# FUNCTIONAL PROGRAMMING WITH PYTHON

  https://blog.feabhas.com/2019/05/python-3-file-paths

if __name__ == '__main__':
  run()
  

  * IF STATEMENTS 
  -----------------------------------------------------------------------
  PROCEDURAL                            FUNCTIONAL
  -----------------------------------------------------------------------
  def a(i):                        a=lambda  x:x
    if i = 1:                       b = lambda x:(x==1 and a("One")) \
      return "One"                    or (x==2 and a("Two")) \
    elif i = 2:                       or (a("Three"))
      return "Two" 
    else:                           print b(1) # One 
      return "Three"                print b(2) # Two 
                                    print b(3) # Three 
  print a(1) # One 
  print a(2) # Two 
  print a(3) Three 


  *FOR STATEMENTS
  grocery_list = ['apples', 'bananas', 'oranges', 'milk']
  -----------------------------------------------------------------------
  PROCEDURAL                            FUNCTIONAL
  -----------------------------------------------------------------------
  for grocery in grocery_list:            def grocery(list): 
    print grocery                           print list 
                                          map(grocery, grocery_list) 

  * WHILE STATEMENTS 
  -----------------------------------------------------------------------
  PROCEDURAL                            FUNCTIONAL
  -----------------------------------------------------------------------
  count = O                             def func(n): 
  white count < 5:                          print The count is:', n 
    print 'The count is:', count        a = lambda count: [func(i) for i in range(count)) 
    count = count + 1                   a(5)


  * FUNCTIOOS 
  -----------------------------------------------------------------------
  PROCEDURAL                            FUNCTIONAL
  -----------------------------------------------------------------------
  def f(x):                             a=lambda x:x*x 
    return x*x                          print a(4) 
  a=f(4)
  print a 


  ----
  def a(i): 							a = lambda x:x
  	if i==1: 						b= lambda x: ( x==1 and a(1))
  		return "one" 				or ( x==2 and a(2))
  	else if i==2: 					or ( x==3 and a(3))
  		return "two" 
  	else if i==3:					print b(1)
  		return "three"		 		print b(2)

  print a(1)		
  print a(2)		
  print a(3)		

  ----
  grocery_list=['apple', milk] 		grocery_list=['apple', milk] 		
  for g in grocery_list: 				def printg(list):
  	print g 							print list
  									map(printg, grocery_list)
  ----
  count=0 							def func(n):
  while count<5:							print 'c=',n
  	print 'c=',count 				a=lambda count:[func(i) for i in range(count)]	
  	count = count+1 				a(5)




python/conda: find package

  conda list conda list | findstr ""