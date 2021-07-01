## prototype
 
CREATIONAL PATTERN
 
Clonage d'une instance existance qui sert de modèle
A fully initialized instance to be copied or cloned
Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

Specify the kind of objects to create using a prototypical instance, and create new objects by copying this prototype.


ntroduction problem
Original GoF pattern can not be introduced to the existing program without modifying the source code. (This problem is mentioned at p.120, line.37-39 in the GoF book.)
Used programming technique(s)

Abstract method addition of "copy()" method to the existing classes.

Consequences

(+) Prototype pattern can be introduced into existing classes.

Intention

des prototypes variés existent qui sont copiés et assemblésOn utilise le Prototype lorsque :• un système doit être indépendant de la façon dont ses produits sont créés, assemblés, représentés• quand la classe n'est connue qu'à l'exécution• pour éviter une hiérarchie de Factory parallèle à une hiérarchie de produits
Motivation
Solution
 
![](assets/books/computer_science/software_design_rules/design_patterns/prototype.png)


To create clones of the existing objects. This is similar to the prototypal inheritance in JavaScript. All of the properties and methods of an object can be made available on any other object by leveraging the power of the __proto__ property

Used to implement inheritance in JavaScript: It add the properties of the parent to the child objects. Inherited properties are present on the __proto__ key.

```js
class Pokemon {
    name: string
    baseExperience: number
    abilities: string[]

    constructor(name: string, baseExperience: number, abilities: string[]) {
        this.name = name
        this.baseExperience = generation
        this.abilities = [...abilities]
    }

    addAbility(ability: string) {
        /* Method to add new abilities */
    }    
}

let bulbasaurObj = new Pokemon("bulbasaur", 64, ["chlorophyll"])
let obj = Object.create(Pokemon.prototype)
```

```js
let shapePrototype = {
    width: 10,
    height: 10,
    draw: function (shape) {  }
}

function Rectangle () {}

/* The prototype of Rectangle is shapePrototype, which means Rectangle should be cloned as shapePrototype */
Rectangle.prototype = shapePrototype

let rectObj = new Rectangle()

/* draw method is present on the rectObj as shapePrototype is attached to it __proto__ property */
rectObj.draw('rectangle')
```