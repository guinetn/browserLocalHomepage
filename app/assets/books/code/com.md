# COM

COM Componenant

Historic

1989: Excel developers implemented DDE protocole to allow applications to speak with Excel.
1992: word team create OLE to integrate applications in Word
All these protocoles were based on Windows messages.

PowerPoint team improve OLE specifications: OLE2 based on pointers and not based on Windows messages. This is COM

Then DCOM, ACTIVEX (COM + Internet), ATL library, MTS → COM+,
        
Definition 

COM component:  « un fournisseur de service logiciel qui permet à une application de s'affranchir de certaines opérations déjà modélisées et réalisées ». En simplifié, COM est un fournisseur d’objets pré-compilés, qui grâce à une bibliothèque de type qui lui était associée, pouvait être utilisé dans de nombreux langages dont les types n’étaient pas forcément compatibles. Cette librairie contient la définition des interfaces publiées par le composant (interface mentionnant les méthodes et fonctions pouvant être utilisées par le logiciel client).

Même si selon toute vraisemblance, les composants COM sont voués à la disparition avec la multiplication des composants .NET,  ils existent et présentent encore beaucoup d’intérêt.

Automation Word

Préparation

Le composant d’automation OLE de Word (de même que tous ceux de la suite Office) n’offre aucune interface visuelle. Ce composant permet donc, sans jamais avoir à faire apparaître Word  à l’écran ainsi que dans la barre des tâches, de le piloter à partir d’un autre programme.

Pour l’utiliser, dotNET doit installer ce qui est appelé un RCW (Run Time Callable Wrapper) qui est une couche logicielle faisait la liaison entre le COM et dotNET.
Pour générer ce Wrapper, vous pouvez utiliser :

l’utilitaire en ligne de commande TLBIMP (Type LiBrary IMPorter).
VisualStudio en allant dans Projet > Ajouter une référence > Onglet COM.

Nous utiliserons d’ailleurs VisualStudio pour tout le reste de cet article.  

Sélectionnez le composant COM de WORD (nommé : « Microsoft Word 10.0 Object Library » 