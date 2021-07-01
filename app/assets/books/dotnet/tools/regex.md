# REGEX


[Generating regular expressions from user-provided test cases](https://github.com/pemistahl/grex)

Regex ex1 = new Regex(@"ISBN:\s\d");
Match  m = ex1.Match(@"ISBN: 978-1871962406")
m.Success
m.index     position of the match in the search string
m.Match     returns the first match to the regular expression 
            m.NextMatch method which returns another Match object

Alternatives
    @"ISBN:|ISBN-13:"
    @"ISBN:|ISBN-13:\s*\d"
    @"(ISBN:|ISBN-13:)\s*\d"

Capture 
    @"(<div>)(</div>)"
    GroupCollection Grps = ex2.Match(@"<div></div><div></div><div></div>").Groups;
    CaptureCollection Caps=Groups[0].Captures;
        Caps[0].Index.ToString() + " " + Caps[0].Length.ToString() + " " + Caps[0].ToString());
    
    Regex ex2=new Regex(@"((<div>)(</div>))*");   

Back references
    Regex ex2= new Regex(@"<(div)></\1");
    Regex ex2= new Regex(@"<(div|pr|span|script)></\1>");
    
Reduction
    Regex ex3 = new Regex(@"^(?<COUNT>A)+(?<-COUNT>B)+");   matches any number of As followed by the same number of Bs. But accept AABBB       
    Regex ex3 = new Regex(@"^(?<COUNT>A)+(?<-COUNT>B)+$");  fails on AABBB but it matches AAABB
    
*            zero or more
+           one or more
?           zero or one
{n}        exactly n times
{n,}       n or more times
{n,m}    at least n at most m times

.           (i.e. a single dot) matches any character.
\d         digit
\s         white-space
\w        any “word” character including digits
There is also the convention that capital letters match the inverse set of characters:

\D       any non-digit
\S       any non-white space
\W      any word character

^          start of string
$          end of string
\b         word boundary – i.e. between a \w and \W
\B        anywhere but a word boundary