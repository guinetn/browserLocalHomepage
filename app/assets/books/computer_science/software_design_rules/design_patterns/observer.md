## observer 

BEHAVIOURAL PATTERN

Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

subscription mechanisms so that objects can communicate the changes happening in one part of the system to the rest of the world.

Mécanisme de notification sur plusieurs objets
A way of notifying change to a number of classes
Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
Informer un objet d'un changement dans un autre sans créer de liaison explicite.

Ex : Une feuille excel est mise à jour, différents graphes se rafraîchissent.
Intention
On utilise Observer lorsque :
• Une abstraction a plusieurs aspects, dépendant l'un de l'autre. Encapsuler ces aspects indépendament permet de les réutiliser séparément.
• Quand le changement d'un objet se répercute vers d'autres.• Quand un objet doit prévenir d'autres objets sans pour autant les connaitre.
Motivation
Solution

![](assets/books/computer_science/software_design_rules/design_patterns/observer.png)


```js
// Observable button that notify observer for click
public class ButtonObservable {

    public ButtonObservable() {
        super();
        addActionListener( this );
    }

    public void addObserver( Observer observer ) {
        observable.addObserver( observer );
    }

    public void actionPerformed( ActionEvent evt ) {
        observable.notifyObservers();  
    }

    Observable observable = new Observable();
}
```

```js

let s = new Subject()
let o1 = new Observer(1)
let o2 = new Observer(2)

s.addObserver(o1)
s.addObserver(o2)

/* Changing the critical information */
s.changeCriticalNumber()


class Subject {
    constructor () {
        this.criticalNumber = 0
        this.observers = []
    }

    addObserver (observer) {
        this.observers.push(observer)
    }

    removeObserver (observer) {
        let index = this.observers.findIndex(o => o === observer)
        if (index !== -1) {
            this.observers.splice(index, 1)
        }
    }

    notify () {
        console.log('Notifying observers about some important information')
        this.observers.forEach (observer => {
            observer.update(this.criticalNumber)
        })
    }

    changeCriticalNumber () {
        /* Changing the critical information */
        this.criticalNumber = 42
        /* Notifying the observers about this change */
        this.notify()
    }
}

class Observer {
    constructor (id) {
        this.id = id
    }

    update (criticalNumber) {
        console.log(`Observer ${this.id} - Received an update from the subject ${criticalNumber}`)
    }
}
```