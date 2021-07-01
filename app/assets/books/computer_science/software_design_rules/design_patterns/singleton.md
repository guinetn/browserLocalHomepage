## singleton 

CREATIONAL PATTERN

A class of which only a single instance can exist
Ensure a class only has one instance, and provide a global point of access to it.
Cacher l'accès au constructeur et maintenir un nombre limité d'instances.

Ensure a class has only one instance and provide a global point of access to it.

Intention
Assure q'une seule classe n'a qu'une seule instance et fournit un point d'accès vers cette instance.
Motivationunique instanceOn utilise le Singleton lorsque :• il n'y a qu'une unique instance d'une classe et qu'elle doit être accessible de manière connue • une instance unique peut être sous-classée et que les clients peuvent référencer cette extension sans avoir à modifier leur code
Solution
La classe contient le code assurant les 2 contraintes
![](assets/books/computer_science/software_design_rules/design_patterns/singleton.png)


```js
public class ButtonRenderer {

    private static ButtonRenderer instance;
    private ButtonRenderer() {
    ...
    }

    // singleton access
    public static ButtonRenderer getInsance() {
        if ( instance == null ) 
        instance = new ButtonRenderer();
        return instance;
    }

}
```


```js
let dbInstance = null

function getDBConn () {
    if (!dbInstance) {
        dbInstance = new DB() // Creating an instance of DB class and storing it in the global variable dbInstance
    }
    return dbInstance
}

function useDBConn () {
    let dbObj = getDBConn()
    /* --- */
}

function f1 () {
    let dbObj = getDBConn()
    /* --- */
}

function f2 () {
    let dbObj = getDBConn()
    /* --- */
}

```
Better: don't pollute the global scope:
```js
let a = singletonWrapper.getInstance()
a.getRandomNumber()
a.getRandomNumber() // idem

let singletonWrapper = (function () {
let dbInstance = null

  function init () {
        let randomNumber = Math.random()

        return {
            getRandomNumber: function () {
                return randomNumber
            }
        }
    }
 /* The IIFE returns an object with getInstance as one of the methods and abstracts all other details */
    return {
        getInstance: function () {
            if (!instance) {
                instance = init()
            }
            return instance
        }
    }
})()
```