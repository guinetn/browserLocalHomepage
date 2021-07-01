## bridge 

STRUCTURAL PATTERN


Decouple an abstraction from its implementation so that the two can vary independently.

pont entre une classe et son implémentation. (changements futur de l'implémentation prévus, donc
Decouple an abstraction from its implementation so that the two can vary independently
Pouvoir faire évoluer des classes d'abstraction (ex: une fenêtre) sans toucher au niveau implémentation (ex: une fenêtre pour window).

Separates an object's interface from its implementation

Intention

pour lier une abstraction à une implantation
On utilise Bridge lorsque :
• on veut éviter un lien permanent entre l'abstraction et l'implantation (ex: l'implantation est choisie à l'exécution)
• l'abstraction et l'implantation sont toutes les deux susceptibles d'être raffinées
• les modifications subies par l'implantation ou l'abstraction ne doivent pas avoir d'impacts sur le client (pas de recompilation)

![](assets/books/computer_science/software_design_rules/design_patterns/bridge.png)

```js
// Abstract class
public class Canvas {
        // Set the canvas implementation for (Windows, Motif...)
        public void setCanvas( CanvasPeer canvas ) {  this.canvas = canvas;   }
        protected CanvasPeer canvas;        
        public void draw() { canvas.draw(); }
}

// Abstraction inheritance
public class ExtendedButton extends Canvas {
        public void draw() {  canvas.drawText( "push me" );   ...   }
}
```