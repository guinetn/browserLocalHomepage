## MEDIATOR 

BEHAVIOURAL PATTERN

Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction

Reduces the tight coupling between a set of interacting objects allowing to change objects functionality independently
Objects don’t call other objects directly but delegate their interaction to a mediator object. This mediator object then handles the communication and interactions between objects.

Réduit le couplage entre objets. Encapsule la communication entre les objets
Gère le fonctionnement d'un objet qui gère les interactions entre d'autres objets.
Defines simplified communication between classes

Lorsque trop d'intéraction existent entre objets, les stocker dans un contrôleur spécifique.

Ex : Une liste avec un champ texte. Lorsque un caractère est entré dans le champ texte, la liste se met à jour, lorsque une sélection est faite dans la liste, le champ texte se met à jour.

Intention
On utilise Mediator lorsque :
• quand de nombreux objets doivent communiquer ensemble
• la réutilisation d'un objet est délicate car il référence et communique avec de nombreux autres objets
Motivation
Solution

![](assets/books/computer_science/software_design_rules/design_patterns/mediator.png)


```js
// Interaction between two buttons
public class Mediator implements ActionListener {
    public void setButton1( Button button1 ) {
        this.button1 = button1;
        button1.addActionListener( this );
    }       

    public void setButton2( Button button2 ) {
      this.button2 = button2;  
      button2.addActionListener( this );
    }

    public void actionPerformed( ActionEvent evt ) {
        if ( evt.getSource() == button1 ) {
           button2.setText( button1.getText() );
        } else
        button1.setText( button2.getText() );
    }

    private Button button1, button2;
}
```


# More 

- https://www.ezzylearning.net/tutorial/mediator-design-pattern-in-asp-net-core
- https://github.com/jbogard/MediatR.Extensions.Microsoft.DependencyInjection