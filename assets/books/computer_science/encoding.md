# ENCODING

Mapping numeric values and characters
ASCII (8 bits = 256 chars) 
↓
isn't enough to represent all of the characters used in the world
↓
Solution #1
    Reuse the same 256 numeric codes and associate them with different sets of characters
    On the Internet: ISO 8859-n [n:1→16]
    Each value of n maps a different set of characters onto the 0 to 255 values that a byte can represent. ISO 8859-1 → Latin-1 Western European
    ISO-8859-2 → Latin-2 Central European (Bosnian, Polish, Croatian...)

    Tells the browser what encoding is in use:
    Header stating the character set in use: Content-Type: text/html; charset=ISO-8859-1
    <script src="/./myProgram.js" charset="ISO-8859-1">

    Because the character sets in ISO-8859 were limited in size, and not compatible in multilingual environments, the Unicode Consortium developed the Unicode Standard that covers (almost) all the characters, punctuations, and symbols in the world


## ASCII

127:  0111 1111
256:  1111 1111

Us 8 bits to represent 256 characters
Encodes a limited range of characters by using the lower seven bits of a byte. Because this encoding only supports character values from U+0000 through U+007F, in most cases it is inadequate for internationalized applications.

Defines 127 alphanumeric characters: 
- A-Z
- a-z
- 0-9
- Command characters (carriage return, backspace...)
- Special characters

ASCII was the first character set (encoding standard)

ASCII 48: 0
ASCII 58: 9
ASCII 65: A
ASCII 97: a

<div id='asciiTable'>
<style type="text/css" scoped>
#asciiTable {
    display: flex; 
    flex-direction: row;
    flex-wrap: wrap;    
    align-items: center;
}   
#asciiTable div { background-color:#000; border:solid 1px grey; margin: 8px; padding: 10px; font-family: Arial; color: #fff; border-radius: 8px; 
position:relative; width: 95px; height: 30px; text-align:center;}
#asciiTable .ctrl, #asciiTable .char, #asciiTable .digit { font-size: 1.4em; }
#asciiTable .digit { color: #fbff00; background-color: red; }
#asciiTable .char { color: #fff; background-color: #2546fd; }
#asciiTable .ctrl { color: ##827b7b; background-color: grey; }
#asciiTable .asciisup { position:absolute; top:10px; left: 3px; font-size: small;}
</style>
</div>

download.exec(assets/books/computer_science/assets/show_ascii_table.js)

Both ISO-8859-1 (default in HTML 4.01) and UTF-8 (default in HTML5), are built on ASCII.

## ANSI/ISO encoding

"ANSI Code Pages" was used in Windows to refer to non-DOS character sets.

Support for a variety of code pages
Windows: code pages are used to support a specific language or group of languages. For a table that lists the code pages supported by .NET, see the Encoding class. You can retrieve an encoding object for a particular code page by calling the Encoding.GetEncoding(Int32) method. 
A code page contains 256 code points (zero-based). In most code pages, code points 0 through 127 represent the ASCII character set, and code points 128 through 255 differ significantly between code pages. 
Code page 1252: provides characters for Latin writing systems (English, German, French). The last 128 code points in code page 1252 contain the accent characters. 
Code page 1253: provides character codes required in the Greek writing system. The last 128 code points in code page 1253 contain the Greek characters. 

As a result, an application that relies on ANSI code pages cannot store Greek and German in the same text stream unless it includes an identifier that indicates the referenced code page.
## MS-DOS

“L’expérience   é = E9

Windows-1252 (CP1252)

Use page 850 (DOS latin-1)

## WINDOWS CODE PAGE

Called "ANSI code pages"
Code pages for which non-ASCII values (values greater than 127) represent international characters.
Each code page is represented by a code page identifier, for example, 1252, and is handled by the Unicode and character set API functions.

[code-page-identifiers](https://docs.microsoft.com/fr-fr/windows/win32/intl/code-page-identifiers)
...
1200	utf-16	Unicode UTF-16, little endian byte order (BMP of ISO 10646); available only to managed applications
1201	unicodeFFFE	Unicode UTF-16, big endian byte order; available only to managed applications
...
1252	windows-1252	ANSI Latin 1; Western European (Windows)
...

ANSI code pages can be different on different computers, or can be changed for a single computer, leading to data corruption. For the most consistent results, applications should use Unicode, such as UTF-8 or UTF-16, instead of a specific code page.

## UNICODE

https://www.unicode.org/standard/standard.html
https://docs.microsoft.com/fr-fr/windows/win32/intl/unicode       utf16: 16 bits
https://docs.microsoft.com/fr-fr/windows/win32/intl/code-pages    old: 8 bits "C" style LPCSTR

A list of characters indexed by a 32-bit value called the character's code point. 
There are enough characters in Unicode to represent every language in use and some that aren't. 
To have an unlimited quantity of characters (asiatics on 4 octets = 32 bits...)
Réunit tous les caractères de tous les encodages dans une seule et même table de caractères.
Versions: bytes per character is fixed or dynamic, bytes read order...
Unicode defines the characters, but it doesn't say how the code point should be represented. The simplest is to use a 32-bit index for every character. This is UTF-32 and it is simple, but very inefficient. It is roughly four times bigger than ASCII. In practice we use more efficient encodings: UTF-8, UTF-16...

First 128 characters of Unicode (correspond one-to-one with ASCII) are encoded using a single octet with the same binary value as ASCII, making valid ASCII text valid UTF-8-encoded Unicode as well


BOM (Byte Mark Order)
. Not mandatory
UTF-8 = EF BB BF
UTF-16 Big Endian = FE FF
UTF-16 Little Endian = FF FE
UTF-32 Big Endian = 00 00 FE FF
UTF-32 Little Endian = FF FE 00 00

ï»¿ = EF BB BF = code for Unicode UTF-8 format file.
PS>Fhx test.txt
Linux>file -bi test.txt or xxd test.txt


## UTF-7	

127:  0111 1111
256:  1111 1111

Represents characters as sequences of 7-bit ASCII characters. Non-ASCII Unicode characters are represented by an escape sequence of ASCII characters. UTF-7 supports protocols such as email and newsgroup. 
Not secure/robust: changing one bit can radically alter the interpretation of an entire UTF-7 string
In other cases, different UTF-7 strings can encode the same text. For sequences that include non-ASCII characters, UTF-7 requires more space than UTF-8, and encoding/decoding is slower. Consequently, you should use UTF-8 instead of UTF-7 if possible.
   
## UTF-8
1,112,064 characters
UTF-8 is a variable length code that uses up to four bytes to represent a character. 
The number of bytes are used to code a character is indicated by the most significant bits of the first byte. 
0xxxxxxx   one byte 
110xxxxx   two bytes
1110xxxx   three bytes
11110xxx   four bytes

Represents each Unicode code point as a sequence of one to four bytes. UTF-8 supports 8-bit data sizes and works well with many existing operating systems. 
For the ASCII range of characters, UTF-8 is identical to ASCII encoding and allows a broader set of characters. 
For Chinese-Japanese-Korean (CJK) scripts, UTF-8 can require three bytes for each character, and can cause larger data sizes than UTF-16. Sometimes the amount of ASCII data, such as HTML tags, justifies the increased size for the CJK range.

Unicode is a character set. UTF-8 is encoding

>Encoding translates numbers into binary
>Character sets translates characters to numbers.

A character in UTF8 can be from 1 to 4 bytes long. UTF-8 can represent any character in the Unicode standard. UTF-8 is backwards compatible with ASCII. UTF-8 is the preferred encoding for e-mail and web pages

First 128 characters of UTF-8 are the same as ASCII
Unicode characters U+0000 to U+007F can be represented in a single byte
 
The default character encoding in HTML-5 is UTF-8
<meta charset="utf-8">
<meta charset="ISO-8859-1">   To use a different character set than UTF-8
Modern browsers work in UTF-8 internally and any other encoding is converted to UTF-8 when the page or file is read in. This means that web pages and scripts have to be created using UTF-8 encoded files

Efficacité en terme taille mémoire et du fait de sa rétrocompatibilité avec l’ASCII. En effet, rien ne distingue un vieux fichier ASCII d’un fichier UTF-8. C’est seulement lorsqu’on utilise des caractères spéciaux que le fichier UTF-8 va se distinguer de l’ASCII.

Les caractères spéciaux en UTF-8 seront stockés en hexadécimal sur 2 à 4 octets en respectant tout simplement la table de caractères UTF-8. Quelque part, c’est toujours aussi simple qu’avant : A un “code” correspond toujours un seul caractère dans la table.

Les caractères spéciaux occidentaux sont tous codés sur deux octets

To include a UTF-8 character in HTML that is outside the usual range (one you cannot type using the default keyboard=
&#decimal;
&#xhex;  
&#x2211;  ∑

## UTF-16

16-bit Unicode Transformation Format 
A variable-length character encoding for Unicode, capable of encoding the entire Unicode repertoire. 
UTF-16 is used in major operating systems and environments, like Microsoft Windows, Java and .NET (strings)

Represents each Unicode code point as a sequence of one or two 16-bit integers. Most common Unicode characters require only one UTF-16 code point, although Unicode supplementary characters (U+10000 and greater) require two UTF-16 surrogate code points. Both little-endian and big-endian byte orders are supported. UTF-16 encoding is used by the common language runtime to represent Char and String values, and it is used by the Windows operating system to represent WCHAR values.
## UTF-32	
Represents each Unicode code point as a 32-bit integer. Both little-endian and big-endian byte orders are supported. UTF-32 encoding is used when applications want to avoid the surrogate code point behavior of UTF-16 encoding on operating systems for which encoded space is too important. Single glyphs rendered on a display can still be encoded with more than one UTF-32 character.


# Common text encodings

Name	How To Create	Description
UTF-8	Encoding.UTF8	The most common multi-byte representation, where ASCII characters are always represented as single bytes, but other characters can take more,up to 3 bytes for a character within the BMP. This is usually the encoding used by .NET if you don't specify one (for instance, when creating a StreamReader). When in doubt, UTF-8 is a good choice of encoding.
System default	Encoding.Default	This is the default encoding for your operating system,which is not the same as it being the default for .NET APIs! It's typically a Windows code page,1252 is the most common value for Western Europe and the US, for example.

UTF-16	Encoding.Unicode, Encoding. BigEndianUnicode	UTF-16 represents each character in a .NET string as 2 bytes, whatever its value. Encoding. Unicode is little-endian, as opposed to Encoding. BigEndianUnicode.

ASCII	Encoding.ASCII	ASCII contains Unicode values 0-127. It does not include any accented or "special" characters. "Extended ASCII" is an ambiguous term usually used to describe one of the Windows code pages.

Windows code page	Encoding. GetEncoding(page)	If you need a Windows code page encoding other than the default, use Encoding. GetEncoding(Int32).

ISO-8859-1 ISO-Latin-1	Encoding. GetEncoding( 28591)	Windows code page 28591 is also known as ISO-Latin-1 or ISO-8859-1, which is reasonably common outside Windows.

UTF-7	Encoding.UTF7	This is almost solely used in email, and you're unlikely to need to use it. I only mention it because many people think they've got UTF7-encoded text when it's actually a different encoding entirely.


## More
- https://www.rapidtables.com/code/text/alt-codes.html
- https://www.rapidtables.com/code/text/unicode-characters.html
- https://github.com/dotnet/runtime/issues/43956

- https://www.i-programmer.info/programming/javascript/14257-javascript-canvas-unicode.html
- https://docs.microsoft.com/en-us/dotnet/standard/base-types/character-encoding