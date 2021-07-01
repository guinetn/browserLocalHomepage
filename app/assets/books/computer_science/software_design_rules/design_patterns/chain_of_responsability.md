## chain of responsability 

BEHAVIOURAL PATTERN

To pass request through a chain of handlers (process+next or reject=stop propagating) = sequential checks on incoming req. (ordering system)

consider a simple example of an express server. The incoming requests are intercepted by middleware; the middleware processes the request and passes it onto the next middleware in chain.
any of the middleware can also reject the request and stop propagating it through the chain if the request is deemed invalid

Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request.
Chain the receiving objects and pass the request along the chain until an object handles it.
  
La requête est transmise jusqu'a ce que l'un des objets chargé de la traiter la traite
A way of passing a request between a chain of objects

Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request.
Chain the receiving objects and pass the request along the chain until an object handles it.

Définir une arborescence de traitement.
Ex: Une info-bulle est affichée sur certains boutons, sinon c'est l'info-bulle du conteneur qui est affiché.

Intention
On utilise Chain of Responsibility lorsque :
• plus d'un objet peut traiter une requète, et il n'est pas connu a priori
• l'ensemble des objets pouvant traiter une requète est construit dynamiquement

Motivation
Solution
![](assets/books/computer_science/software_design_rules/design_patterns/chain_of_responsability.png)


```js
// Decide to handle
public interface Handler {
        public boolean handle( Context context );
        public void handler();
}

// List of handlers
public void HandlerManager {

        public void addHandler( Handler handler ) {}

        public void handle() {
    // search the first handler and launch it
        }
}
```