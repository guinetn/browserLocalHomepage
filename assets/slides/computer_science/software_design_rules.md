# SOFTWARE DESIGN RULES

### OOP (OBJECT ORIENTED PROGRAMMING) PRINCIPLES
Pillars: Encapsulation, Inheritance, Polymorphism

### Case styles conventions: combine words

Be consistent with the convention used, and in a team, to come to an agreement on the convention.

* PascalCaseIsLikeThis: BackColor
First letter in the identifier and the first letter of each subsequent concatenated word are capitalized
To combine words to form a single concept
Convention in declaring classes
* camelCaseIsLikeThis: backColor
First letter of an identifier is lowercase and the first letter of each subsequent concatenated word is capitalized
To combine words to form a single concept
* Uppercase
All letters in the identifier are capitalized. For identifiers that consist of two or fewer letters
* snake_case: user_login_name or USER_LOGIN_NAME
Replacing each space with an underscore (_)
All caps version, all letters are capitalized:
Snake Case: user_login              Declaring database field names
Snake Case (All Caps): USER_LOGIN   Often used as a convention in declaring constants
* kebab-case: user-login-name
Replacing each space with a dash (-)

### Namespace Naming Guidelines

http://msdn.microsoft.com/en-us/library/893ke618(v=vs.71).aspx
use Pascal case (BackColor) for namespaces, and separate logical components with periods
use plurals when appropriate

    <Company>.(<Product>|<Technology>)[.<Feature>][.<Subnamespace>]
    CompanyName.TechnologyName[.Feature][.Design]
    Microsoft.Media.Design
    Microsoft.WindowsMobile.DirectX

    CompanyName.TechnicalDomain.AppName.FunctionalArea.Class
    CompanyName.TechnicalDomain.Common.FunctionalArea.Class
    CompanyName.Common.FunctionalArea.Class
    
### KISS (KEEP IT SIMPLE STUPID)
Most systems work best if they are kept simple rather than made complex.
Simplicity should be a key goal in design and unnecessary complex should be avoided.

### DRY PRINCIPLE (DON’T REPEAT YOURSELF)
Not any repetition of the functionality in your system.
There should be single representation for any of knowledge in the system.

### TELL, DON’T ASK
You should tell what the object should do rather than asking the state of object and taking decisions.
This avoids tight coupling between classes and encourages responsibility assignments.

### YAGNI (YOU AIN’T GONNA NEED IT)
This principle states you should include the functionality the application needs.
Put off other features you may think the application may need.

### SOC (SEPARATION OF CONCERNS)
you should dissect a piece of software in to separate modules that encapsulate unique behavior.
SoC encourages code maintainability reusability and testability.

### SOLID
- S = SINGLE RESPONSIBILITY PRINCIPLE
"A class should have one and only one responsibility".
Each responsibility is an axis of change.
Code becomes coupled if classes have more than one responsibility.
- O = OPENED CLOSED PRINCIPLE
"Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification."
- L = LISKOV SUBSTITUTION PRINCIPLE
"Subtypes must be substitutable for their base types."
This is polymorphism. just a way of ensuring that inheritance is used correctly.
- I = INTERFACE SEGREGATION PRINCIPLE
"Clients should not be forced to depend upon interfaces that they do not use."
A class don't have to implement not needed methods from an interface to implement: Share functionality among many interfaces.
If a class wants to implement the interface, it has to implement all of the methods, some of which may not be needed by that
class at all. So, doing this also introduces unnecessary complexity, and reduces maintainability or robustness in the system.
The Interface Segregation principle ensures that Interfaces are developed so that each of them have their own responsibility
and thus they are specific, easily understandable, and re-usable.
- D = DEPENDENCY INVERSION PRINCIPLE
Depend on abstractions, not on concrete objects
High level modules should not depend upon low level modules

    BAD
       
        Employee class 
            // Have to persist to XML and a database
            ToXML() Break single responsibility principle
            ToDB()  Break single responsibility principle
            To(saveMethod)  Hard-coding a set of devices = Break Open Closed principle

    GOOD
       
        DataWriter abstract class 
            |___ class XMLDataWriter
            |___ class DbDataWriter

        class EmployeeWriter  
            Save(DataWriter)
                    |___ Output method depend upon abstractions not concrete classes
                        The dependencies have been inverted. 
                        Now we can create new types of ways for Employee data to be written                        

### ACID (DataBases): Atomic Coherent Isolation Durable
The 4 ACID properties garantee a transaction execution reliability
Transaction: operations modifying data
* Atomic
Operations sequence is not divisible: one (or system) fails, all rollback. Change all or nothing
* Coherent
Transaction will respect data integrity constrainst: debit if credit
* Isolated
optimist transaction: rollback if r/w order interference
pessimist transaction: locked resources to avoid r/w interference. Perf ↓
* Durable
Succedded transactions are not lost by system faiure. They are permanent.   
Simple disk write is unsufficient: The DBMS must write in logs the changes made.

### GTD (Getting Things Done) - organise for success
* Harvesting
* Processing 
* Organise 
* Revision 
* Action

### CleanCode

code which is easy to read and understand as well as easy for any developer to maintain and modify. 
It means that assigned names are meaningful but not too long. No parts of code should be repeated, and almost everything should be consistent.

How to write clean code?
"Don't repeat yourself" (DRY), "abstraction," and "keep it simple, stupid" (KISS) principles are the most useful best practices in writing clean code. Consistency and readability should be ensured, and style guides and conventions must be followed.

### Ockham razor

Philosophical principle that emphasized that the simpler solution is the best one given that all other things are same.

Simpler explanations are more likely to be true than complicated ones. This is the essence of Occam’s Razor, a classic principle of logic and problem-solving. Instead of wasting your time trying to disprove complex scenarios, you can make decisions more confidently by basing them on the explanation that has the fewest moving parts.

« Les multiples ne doivent pas être utilisés sans nécessité»
« les hypothèses suffisantes les plus simples sont les plus vraisemblables» 
« Pourquoi faire compliqué quand on peut faire simple ?»


# LOD (The law of demeter) 

Principle of Least Knowledge
Not applicable to every real world problem (Surgeon to know about Patient as well as his Heart)
Minimize coupling within the application
• Design guideline for developing software using Object Orientation
• Formally LoD for functions requires that a method ‘m’ of an object ‘obj’ may only invoke the methods of the following kinds of objects:

```c++
class A {
    void m() {
        KINDS OF OBJECTS THAT m() CAN CALL
        – A itself
        – m's parameters
        - Any object instancied within m
        – A global variable (public static var), accessible by A, in the scope of m
        – obj's direct component objects: A cannot invoke C.methods
    }
}
```

One of the commonest examples is not exposing List<T> as properties, but IEnumerable<T> and providing methods to Add and Remove from the underlying list.        


download.md(assets/slides/web/css_bem.md)

### Software Experience Lessons 

***On Requirements***
<mark>If you don’t get the requirements right</mark>, it doesn’t matter how well you execute the rest of the project. <mark>You will fail</mark>.
Nowhere more than in the requirements process do the interests of all the project stakeholders intersect.
Without high-quality requirements, stakeholders might be surprised at what is delivered. Software surprises are almost always bad news.

When exploring requirements, think beyond the hands-on users. Your customer once removed is still your customer.
Requirements elicitation is a process of exploration, collaboration, discovery, and invention, not a simple collection process. 
The purpose of requirements elicitation is to bring the voice of the customer — the VOC — as close as possible to the ear of the developer — the EOD. The business analyst facilitates bridging that communication gap.
Two commonly used requirements elicitation practices are telepathy and clairvoyance. They don’t work.