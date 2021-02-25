## Standard delegates

***Action delegates***
To encapsulate a method returning void and having 0-16 parameters
Action<int> HelloInst = (param1) => { MessageBox.Show("Hello" + param1.ToString());};
Action<int><int><string> MyAction = (p1,p2,p3) =>

***Func delegates***
To encapsulate a method returning something and having 0-16 parameters
Func<int,int> HelloInst = (param1) => { return param+1; }