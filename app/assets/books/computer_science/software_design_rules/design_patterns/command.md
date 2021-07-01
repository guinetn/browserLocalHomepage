## command 

BEHAVIOURAL PATTERN
Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

Pour gérer de nombreuses commandes qui peuvent être mise en attente/annulée
Encapsulate a command request as an object

Intention
On utilise Command lorsque :
• spécifier, stocker et exécuter des actions à des moments différents.
• on veut pouvoir "défaire". Les commandes exécutées peuvent être stockées ainsi que les états des objets affectés...
• on veut implanter des transactions ; actions de "hautniveau".

Motivation
Solution

![](assets/books/computer_science/software_design_rules/design_patterns/command.png)


```js
Déléguer un traitement sur une autre classe.
myButton.addActionListener( myControleur );
```