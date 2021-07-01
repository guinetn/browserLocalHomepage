## PROXY 

Provide a surrogate or placeholder for another object to control access to it.

Définit comment un objet en contrôle un autre. Comment accéder à un objet
An object representing another object
Objet supplémentaire jouant le rôle d'un autre objet. Types de proxy :
Remote proxy, (stub rmi, corba...)
Virtual proxy, (extension d'un objet dynamique)
Protection proxy, (contrôle de l'accès à un objet)
Smart proxy. (instance avec compteur pour le garbage collector)

Intention
un objet en masque un autre

On utilise le Proxy lorsqu'on veut référencer un objet par un moyen plus complexe qu'un pointeur...
• remote proxy : ambassadeur
• protection proxy : contrôle d'accès
• référence intelligente
– persistence
– comptage de référence
– …


Motivation
Solution

![](assets/books/computer_science/software_design_rules/design_patterns/proxy.png)


```js
// Share interface client/server
public interface Action {
        public void doAction();
}

// Remote action (on server)
public class ConcreteAction implements Action {
        public void doAction() {
    ...
        }
}

// Client proxy
public class ActionStub implements Action {
        public void doAction() {
          // Send Tcp/Ip order for calling remote doAction
        }
}
```

The bind method lets us substitute the original object (window or global object) to the proxy object pokemon. 
```js
let pokemon = {
    name: "butterfree",
    attack: function () {
        console.log(`${this.name} is all set to attack!`)
    }
}
setTimeout(pokemon.attack, 100) // Prints undefined is all set to attack

// The value of this is no longer valid in the setTimeout callback function. We’ll have to change this to:
setTimeout(pokemon.attack.bind(pokemon), 100) // Prints butterfree is all set to attack
```