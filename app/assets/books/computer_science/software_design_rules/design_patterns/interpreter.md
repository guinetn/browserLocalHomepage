## interpreter 

BEHAVIOURAL PATTERN

Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.

Stucture de classes permettant, à partir d'un langage et d'une représentation de sa grammaire de pouvoir interpréter des phrases écrites dans
ce langage
A way to include language elements in a program

Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the languag

Offrir un mini - interpréteur syntaxique et permettre l'utilisation de commandes avec un language adapté.

Ex : Expressions régulières (^a|(b?c*)) pour a b bcccc... cccc...

L'idée est d'accocier à une grammaire une classe et de construire par des instances l'arbre de syntaxe abstrait (premier arbre produit par la compilation). Ces instances sont ensuite parcourues pour valider / exécuter la commande.

Pour des grammaires complexes les outils de conversion automatiques sont indispensables (équivallent lex/yacc javacc).

Intention
On utilise Interpreter lorsqu'il faut interpréter un langage et que :
• la grammaire est simple
• l'efficacité n'est pas un paramètre critique
Motivation
Solution
![](assets/books/computer_science/software_design_rules/design_patterns/interpreter.png)


```js
lettre ::= 'a', 'b', 'c'
lettres ::= {} | lettre lettres
expression ::= '(' expression ')' | lettres

// Letter rule
public class Letter implements Interpretable {
        public void interpret( Context context ) throws Exception {
    char c = context.nextInput();
    if ( c == 'a' | c == 'b' | c == 'c' )
           letter = c;
      else
        throws Exception( "Invalid input :" + c );
        }
        private char letter;
}

// Letters rule
public class Letters implements Interpretable {
        public void interpret( Context context ) throws Exception {
    for ( int i = 0; i < letters.size(); i++ ) {
     ( (Letter)( letters.elementAt( i ) ) ).interpret(
     context );
    }  
        }
        // Add a new letters
        public void addLetter( Letter letter ) {
    letters.addElement( letter );
        }
        private Vector letters = new Vector();
}

// Expression rule
public class Expression implements Interpretable {
        public void interpret( Context context ) throws Exception {
    char c = context.nextInput();
    if ( expression != null ) {
           if ( c == '(' ) {
     expression.interpret( context );
     if ( context.nextInput() != ')' )
throws Exception( "Invalid parenthesis" );
           }
    } else
    letters.interpret( context );
        }

        public void setLetters( Letters letters ) {
    this.letters = letters;
        }

        public void setExpression( Expression expression ) {
    expression = expression;
        }

        private Letters letters;
        private Expression expression;
}
// Instance to interpret (ab)
Letter a = new Letter( 'a' );
Letter b = new Letter( 'b' );
Letters l = new Letters();
l.addLetter( a );
l.addLetter( b );
Expression e1 = new Expression();
e1.setLetters( l );
Expression e2 = new Expression();
e2.setExpression( e1 );          
e2.interpret( new Context( "(ab)" ) );
```