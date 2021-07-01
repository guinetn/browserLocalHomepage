# most_common_words.py
import sys

def add(a,b):
	return a+b

if __name__ == "__main__":

    # pass in numbers argument
    try:
    	print(add(*[1,2])
        num_words = int(sys.argv[1])
    except:
        print("usage: add(1,2)")
        sys.exit(1)   # non-zero exit code indicates error

    

# __name__

Built-in variable that evaluates the name of the current module
This variable decides whether you want to run the script or you want to import the functions defined in the script.
There is no main() function in Python. If the source file is executed as the main program, the interpreter sets the __name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will be set to the module’s name.


__name__ = "__main__" Dans le module principal
Si l'on se trouve dans un autre module importé, alors sa valeur sera égale au nom du module principal.   

if (__name__ == __main__) 
fait la distinction entre les deux cas. Cette condition est utilisée pour développer un module pouvant à la fois être exécuté directement mais aussi être importé par un autre module pour apporter ses fonctions. Vous pouvez insérer dans ce bloc de code des instructions destinées au cas où le module est directement exécuté. Le python est un langage qui n'a pas de méthode main(), comme c'est le cas dans le langage C. Lorsque l'on charge un module, le code exécuté est celui situé directement au plus haut niveau. Cette condition permet donc de regrouper les instructions que l'on veut utiliser dans le cas d'une exécution directe du module.

#monScript.py
if __name__ == __main__:
 print(mon script est exécuté directement)
else
 print(mon script est importé par un autre module)

#monAutreScript.py
import monScript    




variable automatiquement créée disponible dans tous les scripts.
		contient le nom du script courant si on importe le script. Ainsi, dans n’importe quel code, on peut vérifier où on est.
		Si le script est le script principal, alors __name__ = "__main__", pas le nom du script