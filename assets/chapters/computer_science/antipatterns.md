# ANTI-PATTERNS

Describe a bad solution to a particular problem which resulted in a bad situation occurring
Describe how to get out of said situation and how to go from there to a good solution
Describes how NOT to solve recurring problems in your code. Anti-patterns are considered bad software design, and are usually ineffective or obscure fixes.  

They generally also add "technical debt" - which is code you have to come back and fix properly later.

In any large codebase there is a constant balance between managing technical debt, starting new development, and managing a queue of bugs for your product.

### Spaghetti Code
  code with little to zero structure.  
  Nothing is modularised.  

### Golden Hammer
  "I suppose it is tempting, if the only tool you have is a hammer, to treat everything as if it were a nail." Abraham Maslow  
  You start to apply an architectural approach that doesn't quite fit what you need but gets the job done.   
  Pick the right language for your problem. Think about the architecture, and push out your comfort zone. Research and investigate new tools and new ways of approaching the problems you face.

### Boat Anchor
  programmers leave code in the codebase because they might need it later.  
  it is heavy to carry (adds technical debt) but doesn't do anything (quite literally, the code serves no purpose, it doesn't work).

### Dead Code
   look at code written by someone who doesn't work at your company any longer? There's a function that doesn't look like it is doing anything. But it is called from everywhere!    You ask around and no-one else is quite sure what it's doing, but everyone's too worried to delete it.  

### Proliferation of Code  
  when you have objects in your codebase that only exist to invoke another more important object. Its purpose is only as a middleman.  
  This adds an unnecessary level of abstraction (adds something that you have to remember) and serves no purpose, other than to confuse people who need to understand the flow and execution of your codebase.    
  A simple fix here is to just remove it. Move the responsibility of invoking the object you really want to the calling object.

### God Object
  If everywhere in your codebase needs access to one object, it might be a God object.
  God objects do too much. They are responsible for the user id, the transaction id, the customer's first and last name, the total sum of the transaction, the item/s the user is purchasing...you get the picture.  
  It is sometimes called the Swiss Army Knife anti-pattern  
  often compare this problem to asking for a banana, but receiving a gorilla holding a banana. You got what you asked for, but more than what you need.

