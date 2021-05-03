## state

BEHAVIOURAL PATTERN

Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.


Définit un contexte
Décrit comment un objet peut modifier son comportement quand son état change.
Alter an object's behavior when its state changes
Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.
Obtenir des traitements en fonction de l'état courant.

Intention
On utilise State lorsque :
• Le comportement d'un objet dépend de son état, qui change à l'exécution
• Les opérations sont constituées de partie conditionnelles de grande taille (case)
Motivation
Solution

![](assets/books/computer_science/software_design_rules/design_patterns/state.png)


```js
public interface TCPState {
        public void open();
        public void close();
        public void listen();       
}

public interface TCPOpen extends TCPState {
}

public interface TCPListen extends TCPState {
}

public interface TCPClose extends TCPState {
}

public class TCPHandler {

        public void open() {
    state.open();  
        }

        public void close() {
    state.close();
        }

        public void listen() {
    state.listen();
        }

        public void setState( TCPState state ) {
    this.state = state;
        }

        public TCPState state;
}
```

https://www.codeproject.com/Articles/1275479/State-Machine-Design-in-C