# YAML (Ain´t Markup Language)

YAML: for simple configuration

a human friendly data serialization language
a human friendly data serialization standard for all programming languages.

Libraries (C/C++/Net...)
http://yaml.org/

SYNTAX
http://nodeca.github.io/js-yaml/
http://www.yaml.org/spec/1.2/spec.html 
http://lzone.de/cheat-sheet/YAML

YAML stands for: it’s “yet another markup language”, which is designed for representing hierarchical data in a way that’s easy for humans to read and write.

JSON’s foremost design goal is simplicity and universality. Thus, JSON is trivial to generate and parse, at the cost of reduced human readability.
YAML’s foremost design goals are human readability and support for serializing arbitrary native data structures. Thus, YAML allows for extremely readable files, but is more complex to generate and parse:  a natural superset of JSON



.js  https://github.com/nodeca/js-yaml
  npm install js-yaml      for node.js
  npm install -g js-yaml   cli executable

.Net http://yaml-net-parser.sourceforge.net/
using Yaml;
Node node = Node.FromFile ("testRead.yaml");    Read from file
Node node = Node.Parse ("- item1\n- item2\n");    Read from string
Console.WriteLine (node);
node.ToFile ("testWrite.yaml");

- "item1"
- "item2" 




YAML is a human-friendly, cross language, Unicode based data serialization language designed around the common native data types of agile programming languages. It is broadly useful for programming needs ranging from configuration files to Internet messaging to object persistence to data auditing.

A YAML file may contain zero or more YAML documents, separated by document markers. 
A YAML document contains one root DataItem. 
There are three types of DataItems: Scalar, Sequence, and Mapping. DataItems may be nested to form structured data.

http://nodeca.github.io/js-yaml/
http://www.codeproject.com/Articles/28720/YAML-Parser-in-C


  string: 'abcd',
  timestamp: 
   { canonical: Sat Dec 15 2001 03:59:43 GMT+0100 (Romance Standard Time),
     'valid iso8601': Sat Dec 15 2001 03:59:43 GMT+0100 (Romance Standard Time),
     'space separated': Sat Dec 15 2001 03:59:43 GMT+0100 (Romance Standard Time),
     'no time zone (Z)': Sat Dec 15 2001 03:59:43 GMT+0100 (Romance Standard Time),
     'date (00:00:00Z)': Sat Dec 14 2002 01:00:00 GMT+0100 (Romance Standard Time) },
  regexp: { simple: /foobar/, modifiers: /foobar/im },
  undefined: undefined,
  function: [Function],
  foobar: [ 'sexy bunny', 'sexy chocolate' ] }

  → 

  string: abcd

http://yaml.org/type/timestamp.html -----------------------------------------#

timestamp:
  canonical:        2001-12-15T02:59:43.1Z
  valid iso8601:    2001-12-14t21:59:43.10-05:00
  space separated:  2001-12-14 21:59:43.10 -5
  no time zone (Z): 2001-12-15 2:59:43.10
  date (00:00:00Z): 2002-12-14


regexp:
  simple: !!js/regexp      foobar
  modifiers: !!js/regexp   /foobar/mi

https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/undefined

undefined: !!js/undefined ~

https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Function

function: !!js/function >
  function foobar() {
    return 'Wow! JS-YAML Rocks!';
  }

foobar: !sexy
  - bunny
  - chocolate











https://betterprogramming.pub/yaml-tutorial-get-started-with-yaml-in-5-minutes-549d462972d8