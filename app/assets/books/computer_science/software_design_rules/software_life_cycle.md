## SOFTWARE LIFECYCLE
 
### Basic model

Specifications/Requirements
Design
Implementation
Testing
Maintenance

### SDLC Phases
planning, creating, developing, testing, deploying an application
 
 
 
* Analyse des besoins et faisabilitÃ©
c'est-Ã -dire l'expression, le recueil et la formalisation des besoins du demandeur (le client) et de l'ensemble des contraintes, puis l'estimation de la faisabilitÃ© de ces besoins
* SpÃ©cifications ou conception gÃ©nÃ©rale
il s'agit de l'Ã©laboration des spÃ©cifications de l'architecture gÃ©nÃ©rale du logiciel
* Conception dÃ©taillÃ©e
cette Ã©tape consiste Ã  dÃ©finir prÃ©cisÃ©ment chaque sous-ensemble du logiciel
* Codage (ImplÃ©mentation ou programmation)
c'est la traduction dans un langage de programmation des fonctionnalitÃ©s dÃ©finies lors de phases de conception Interfaces...
* Tests unitaires
ils permettent de vÃ©rifier individuellement que chaque sous-ensemble du logiciel est implÃ©mentÃ© conformÃ©ment aux spÃ©cifications
* IntÃ©gration
l'objectif est de s'assurer de l'interfaÃ§age des diffÃ©rents Ã©lÃ©ments (modules) du logiciel. Elle fait l'objet de tests d'intÃ©gration consignÃ©s dans un document
* Qualification (ou recette)
c'est-Ã -dire la vÃ©rification de la conformitÃ© du logiciel aux spÃ©cifications initiales
* Documentation
elle vise Ã  produire les informations nÃ©cessaires pour l'utilisation du logiciel et pour des dÃ©veloppements ultÃ©rieurs
* Mise en production
c'est le dÃ©ploiement sur site du logiciel
* Maintenance
elle comprend toutes les actions correctives (maintenance corrective) et Ã©volutives (maintenance Ã©volutive) sur le logiciel.
 
L'origine de ce dÃ©coupage provient du constat que les erreurs ont un coÃ»t d'autant plus Ã©levÃ© qu'elles sont dÃ©tectÃ©es tardivement dans le processus de rÃ©alisation. Le cycle de vie permet de dÃ©tecter les erreurs au plus tÃ´t et ainsi de maÃ®triser la qualitÃ© du logiciel, les dÃ©lais de sa rÃ©alisation et les coÃ»ts associÃ©s.

 
### WATERFALL MODEL - 1970's
Easy to manage and a sequential approach. 
Testing activities are carried out after the development activities are over:it not a continuous process
 
Cons: vÃ©rification du bon fonctionnement du systÃ¨me est rÃ©alisÃ©e trop tardivement : lors de la phase d'intÃ©gration, ou pire, lors de la mise en production.

    Specifications
        â†“     â†‘ validation
    Detailed conception 
        â†“     â†‘ unit test
      Coding
       â†“  â†‘ integration
    Integration
        â†“ â†‘ validation  
    Production
        â†“ â†‘ validation
    Maintenance
    
chaque phase se termine Ã  une date prÃ©cise par la production de certains documents ou logiciels. Les rÃ©sultats sont dÃ©finis sur la base des interactions entre Ã©tapes, ils sont soumis Ã  une revue approfondie et on ne passe Ã  la phase suivante que s'ils sont jugÃ©s satisfaisants.

Le modÃ¨le original ne comportait pas de possibilitÃ© de retour en arriÃ¨re. Celle-ci a Ã©tÃ© rajoutÃ©e ultÃ©rieurement sur la base qu'une Ã©tape ne remet en cause que l'Ã©tape prÃ©cÃ©dente, ce qui, dans la pratique, s'avÃ¨re insuffisant.    

### V-shaped model
a simultaneous process (dev/deploy/test)
modÃ¨le en cascade dans lequel le dÃ©veloppement des tests et du logiciel sont effectuÃ©s de maniÃ¨re synchrone
Le principe de ce modÃ¨le est qu'avec toute dÃ©composition doit Ãªtre dÃ©crite la recomposition et que toute description d'un composant est accompagnÃ©e de tests qui permettront de s'assurer qu'il correspond Ã  sa description.

Ceci rend explicite la prÃ©paration des derniÃ¨res phases (validation-vÃ©rification) par les premiÃ¨res (construction du logiciel), et permet ainsi d'Ã©viter un Ã©cueil bien connu de la spÃ©cification du logiciel : Ã©noncer une propriÃ©tÃ© qu'il est impossible de vÃ©rifier objectivement aprÃ¨s la rÃ©alisation.

Cependant, ce modÃ¨le souffre toujours du problÃ¨me de la vÃ©rification trop tardive du bon fonctionnement du systÃ¨me.
   
  Specifications       <-- validated by -->      Validation
        \                                          /
         \                                        /
    Detailed conception <-- validated by ->   Unit tests
             \                                  /
              \                                /
            Coding         <--- ---->    Qualification
                \                            /
                 \                          /
                  \                        /
                          Integration
    
### Scrum
Product focused, Business oriented.
Planifications, mÃªlÃ©es, revues, rÃ©trosâ€¦
  
### Agile
Flexible and allows to make changes in any phase. 
Project requirements can change frequently.

