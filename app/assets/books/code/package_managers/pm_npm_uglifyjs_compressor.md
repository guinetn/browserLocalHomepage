# UglifyJS - JavaScript parser/compressor/beautifier

JavaScript parser / mangler / compressor / beautifier library for NodeJS 

https://github.com/mishoo/UglifyJS


UglifyJS is a JavaScript compressor/minifier written in JavaScript. It also contains tools that allow one to automate working with JavaScript code:
http://lisperator.net/uglifyjs/

A parser which produces an abstract syntax tree (AST) from JavaScript code.
A code generator which outputs JavaScript code from an AST, also providing the option to get a source map.
A compressor (optimizer) — it uses the transformer API to optimize an AST into a smaller one.
A mangler — reduce names of local variables to (usually) single-letters.
A scope analyzer, which is a tool that augments the AST with information about where variables are defined/referenced etc.
A tree walker — a simple API allowing you to do something on every node in the AST.
A tree transformer — another API intended to transform the tree.



