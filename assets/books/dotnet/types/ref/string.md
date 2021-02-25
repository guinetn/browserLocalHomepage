# string

String instances unambiguously hold data in any supported language
Historically storing the string as a sequence of 8-bit C-style chars (LPSTR), leaving their intepretation up to the active [Windows code pages](https://docs.microsoft.com/fr-fr/windows/win32/intl/code-pages)
***.NET uses UTF-16 for its string representation***, removing the reliance on code pages.
New Windows applications should use [Unicode](https://docs.microsoft.com/fr-fr/windows/win32/intl/unicode) to avoid the inconsistencies of varied code pages and for ease of localization.

Most applications written today handle character data primarily as Unicode, using the UTF-16 encoding. However, many legacy applications continue to use character sets based on code pages. Even new applications sometimes have to work with code pages, often for one of the following reasons:
- To communicate with legacy applications
- To communicate with older mail and news servers, which might not always support Unicode
- To communicate with the Windows Console

.NET Framework APIs which search for 
- one substring within another string or which compare two strings ***use the thread's current culture*** (StringComparison.CurrentCulture) by default
>string.IndexOf(string)
>tring.CompareTo(string)...
- individual chars within a string ***use ordinal** (StringComparison.Ordinal) searching by default
>string.IndexOf(char)
>string.StartsWith(char)

string.Contains is the exception to this rule. It was introduced in .NET Framework 2.0 - after the other string APIs - and does not follow the same convention. For string.Contains, both the string-based and the char-based overloads use ordinal behavior by default.


## Sort a string
string s= "zacb";
var s2 = new string (str.OrderBy(c => c).ToArray());
var s2 = String.Concat(s.OrderBy(c => c)); // abcz
var s2 = String.Concat(s.OrderBy(c => c).Distinct()); // remove duplicates

//  3 times faster than using OrderBy
static string SortString(string input)
{ 
    char[] characters = input.ToArray();
    Array.Sort(characters);
    return new string(characters);
}

char[] charS = s.ToCharArray();
Array.Sort(charS);


string.Concat(Range(0, 6).Select(i => $"{start+16*i, 3} : {Text(start+16*i), -6}")