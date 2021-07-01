## memento 

BEHAVIOURAL PATTERN

Without violating encapsulation, capture and externalize an object's internal state so that the object can be restored to this state later.

Mécanisme de capture/restitution de l'état d'un objet (SnapShot, Undo/Redo)
Capture and restore an object's internal state
Without violating encapsulation, capture and externalize an object's internal state so that the object can be restored to this state later.
Pouvoir stocker/restaurer l'état d'un objet.

Ex : Swing avec sérialization XML (transformation swing->xml / xml->swing).

Intention
On utilise Memento lorsque :
• on veut sauvegarder tout ou partie de l'état d'un objet pour éventuellement pouvoir le restaurer, et
• une interface directe pour obtenir l'état de l'objet briserait l'encapsulation
Motivation
Solution

![](assets/books/computer_science/software_design_rules/design_patterns/memento.png)


```js
public class BooleanState {
        public BooleanState( boolean state ) {
    this.state = state;
        }

        public boolean isActive() {
    return state;
        }

        boolean state;
}

public class Boolean {
        public void setState( BooleanState state ) {
    value = state.isActive;
        }

        public void getState() {
    return new BooleanState( state );
        }

        boolean value;       
}
```