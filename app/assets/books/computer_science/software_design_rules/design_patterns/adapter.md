## adapter 

STRUCTURAL PATTERN

Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.

It allows two objects of different shapes (format or structure) to work together through a common interface (ex: a charting lib works with json data but apis are xml or json. Use an adpater to convert to json)

Match interfaces of different classes
Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.

Permettre le support d'une nouvelle interface

Permet de faire passer une classe pour une autre (cas d'évolution) en la faisant ressembler du point de vue de son interface
Classe A (A.Meth1, A.Meth2) abandonnée pour B.
Pour ne pas perturber en attendant de réécrire, on écrit un adapter se présentant comme A.
Intentionrendre un objet conformant à un autreOn utilise l'Adapter lorsque on veut utiliser :• une classe existante dont l'interface ne convient pas• plusieurs sous-classes mais il est est coûteux de redéfinir l'interface de chaque sous-classe en les sous-classant. Un adapter peut adapter l'interface au niveau du parent.Motivation
Solution

![](assets/books/computer_science/software_design_rules/design_patterns/adapter.png)

```js
public interface Runnable() {
        public void run();
}

public class Process implements Runnable() {
        public void run() {
    ...
        }
}

public interface Schedulable {
        public void run( long delay );
}

public class ProcessAdapter implements Schedulable extends Process {

        public void setProcess( Process process ) {
    this.process = process;
        }

        public void run() {
    process.run();
        }

        public void run( long delay ) {
    wait( delay );
    run();
        }

        private Process process;
}
```