# string

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