## template 

BEHAVIOURAL PATTERN

Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.


Définit comment mettre en place un algorithme dont les étapes sont figées mais dont la réalisation de ces dernière peut-être déléguée à
d'autres objets offrant des variations de traitement.
Trame d'un traitement immuable mais chaque étape est laissée à d'autres intervenants du système
Ex: ExportData: OuvrirDestination, EcrireEntete, EcrireCorps, EcrirePied, FermerDestination
Defer the exact steps of an algorithm to a subclass

Définir le squelette d'un algorithme et déléguer certaines actions aux sous-classes.

Ex : Trier une liste d'objet. L'algorithme de tri délègue la comparaison des objets.

intention
On utilise TemplateMethod :
• pour implanter une partie invariante d'un algorithme.
• pour partager des comportements communs d'une hiérarchie de classes.
• pour contrôler des extensions de sous-classe.
Motivation
Solution

![](assets/books/computer_science/software_design_rules/design_patterns/template.png)


```js
public abstract class Sorter {

       // Template method
       public void sort( Object[] data ) {
        for ( int i = 0; i < data.length; i++ ) {
        int min = i;
        for ( int j = 1; j < data.length; j++ ) {
         if ( isSmallerThan( data[ min ], data[ j ] ) )
         min = j;
        }
        Object tmp = data[ i ];
        data[ i ] = data[ min ];
        data[ min ] = tmp;
        }   
       }

       public abstract boolean isSmallerThan( Object data1, Object data2 );
}
```