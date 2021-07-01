## constructor 

Called whenever we create an object of a class
The class represents an entity: something like Car, Person…
The constructor method does the work of assigning values to the instance variables of the class to create a new object.

![](assets/books/computer_science/software_design_rules/design_patterns/constructor.png)


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
```

See Prototype Design Pattern
