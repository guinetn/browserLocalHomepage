## iterator 

BEHAVIOURAL PATTERN

Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

lets you traverse elements of a collection (Arrays, LinkedList, Trees, Graphs, etc.) without exposing its underlying implementation.

Permet d'acceder séquentiellement à tous les objets d'une liste sans exposer le conteneur
Sequentially access the elements of a collection

Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

Pouvoir accéder au contenu séquentiel d'une collection sans connaître le système de stockage.

Ex : Enumeration sur Vector / Hashtable

Intention
On utilise Iterator lorsque :
• pour accéder à un objet composé dont on ne veut pas exposer la structure interne
• pour offrir plusieurs manières de parcourir une structure composée
• pour offrir une interface uniforme pour parcourir différentes structures
Motivation
Solution

![](assets/books/computer_science/software_design_rules/design_patterns/iterator.png)


```js
// Client iterator
public interface Iterator {
        public Object first();
        public Object next();
        public boolean hasMoreElements();
e
}

// Data structure with object array
public ArrayData {
        public ArrayIterator( Object[] array ) {
    this.array = array;
        }

        public Iterator getIterator() {
    return new Iterator() {
public boolean hasMoreElements() {
       return i < array.length;
}

public Object first() { return array[ i = 0 ]; }
public Object next() { return array[ i++ ]; }
int i;
    };
        }

        private Object[] array;
}
```