# ENCODING

## ASCII

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

## MS-DOS

“L’expérience   é = E9

Windows-1252 (CP1252)

Use page 850 (DOS latin-1)

## UNICODE
To have an unlimited quantity of characters (asiatics on 4 octets...)
Réunit tous les caractères de tous les encodages dans une seule et même table de caractères.
Versions: bytes per character is fixed or dynamic, bytes read order...
UTF-8, UTF-16...

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
   
## UTF-8
efficacité en terme taille mémoire et du fait de sa rétrocompatibilité avec l’ASCII. En effet, rien ne distingue un vieux fichier ASCII d’un fichier UTF-8. C’est seulement lorsqu’on utilise des caractères spéciaux que le fichier UTF-8 va se distinguer de l’ASCII.

Les caractères spéciaux en UTF-8 seront stockés en hexadécimal sur 2 à 4 octets en respectant tout simplement la table de caractères UTF-8. Quelque part, c’est toujours aussi simple qu’avant : A un “code” correspond toujours un seul caractère dans la table.

Les caractères spéciaux occidentaux sont tous codés sur deux octets

## More
- https://www.rapidtables.com/code/text/alt-codes.html
- https://www.rapidtables.com/code/text/unicode-characters.html