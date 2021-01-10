# include <iostream.h>

void Hanoi (int n, char a, char b, char c)
// move n disks from tower a to tower b, using tower c
{
	if (n == 1)
               {
		// can move smallest disk directly
		cout << "move disk from tower " << a << " to " << b << endl;
		}
	else {
		// first move all but last disk to tower c
		Hanoi (n-1, a, c, b);
		// then move one disk from a to b
		cout << "move disk from tower " << a << " to " << b << endl;
		// then move all disks from c back to b
		Hanoi (n-1, c, b, a);
		}
}

void main()
{
 Hanoi(5, 'a', 'b', 'c');
}


/*
<pre>
3 Discs

        /1\                                                 
       //2\\                                                
      ///3\\\                                               
         A                   B                   C          

Move disk 1 from tower A to tower C

                                                            
       //2\\                                                
      ///3\\\                                   /1\         
         A                   B                   C          

Move disk 2 from tower A to tower B

                                                            
                                                            
      ///3\\\              //2\\                /1\         
         A                   B                   C          

Move disk 1 from tower C to tower B

                                                            
                            /1\                             
      ///3\\\              //2\\                            
         A                   B                   C          

Move disk 3 from tower A to tower C

                                                            
                            /1\                             
                           //2\\              ///3\\\       
         A                   B                   C          

Move disk 1 from tower B to tower A

                                                            
                                                            
        /1\                //2\\              ///3\\\       
         A                   B                   C          

Move disk 2 from tower B to tower C

                                                            
                                               //2\\        
        /1\                                   ///3\\\       
         A                   B                   C          

Move disk 1 from tower A to tower C

                                                /1\         
                                               //2\\        
                                              ///3\\\       
         A                   B                   C          

Total Moves: 7
</pre>
*/    