# Financial Maths

Modélisation, quantification et la compréhension des phénomènes régissant les marchés financiers

L'observation empirique du cours des actifs financiers montre que ceux-ci ne sont pas déterminés de façon certaine par leur histoire. En effet, les nombreuses opérations d'achat ou de vente ne sont pas prévisibles, font fréquemment intervenir des éléments n'appartenant pas à l'historique et modifient le cours de l'actif. Ce dernier est par conséquent fréquemment représenté par un processus chaotique. Benoit Mandelbrot a établi par des considérations statistiques qu'un modèle aléatoire ordinaire, par exemple gaussien, ne pouvait convenir. L'aléa reste cependant fréquemment modélisé par un mouvement brownien[1], quoique des modèles plus élaborés (par exemple, le modèle de Bates) tiennent compte de la non-continuité des cours (présence de sauts dus à des chocs boursiers), ou de la non-symétrie des mouvements à la baisse ainsi qu'à la hausse.

### Efficient-market hypothesis

Un marché est efficient si les prix intègrent à tout moment l'ensemble de l'information disponible

"Asset prices reflect all available information". A direct implication is that it is impossible to "beat the market" consistently on a risk-adjusted basis since market prices should only react to new information (breaking news)
Everbody has the same information

concept central de la théorie financière moderne. Si les marchés sont efficients, cela signifie qu'aucune stratégie d'investissement ne peut permettre de dégager, pour un niveau de risque donné, un profit anormal. Pour le dire plus simplement, cela signifie qu'il est impossible de "battre le marché" sur le long terme !

Il existe trois formes d'efficience pour définir le concept "d'information disponible": 
1. Efficience faible 
l'information contenue dans les prix de marché passés est complètement reflétée par les prix des actifs
2. Efficience semi-forte 
toutes les informations publiques sont complètement prises en compte par les prix
3. Efficience forte 
toutes les informations disponibles, publiques et privées, sont prises en compte par les prix.

### OUTILS

- actualisation
- théorie des probabilités
- calcul stochastique
- statistiques
- calcul différentiel


### Evaluation des produits dérivés 
Pricing ou, à tort, valorisation

 se ramène fréquemment au calcul du prix actuellement d'un actif dont on ne connaît le prix qu'à une date future. Il se ramène par conséquent au calcul d'une espérance conditionelle. Le modèle Black-Scholes est un exemple de solution analytique au problème d'évaluation des options d'achat (call) ou de vente (put) d'un actif sous jacent. Dans le cas d'un call, le problème s'écrit :

C(t) = EˆQ\left(\leftà{-\int_{t}ˆT r(s)ds}\cdot(S_T - K)_+\right| F_{t}\right),

où St est le cours de l'actif, K est le prix d'exercice (ou Strike), r (s) est le taux d'intérêt instantané sans risque à la date s, t est la date «d'aujourd'hui», T est la maturité de l'option, c'est-à-dire la date à laquelle la décision d'exercice peut être prise.

La formule de Black et Scholes est un exemple de solution analytique à ce problème, sous des hypothèses restrictives sur la dynamique du sous-jacent. Voir aussi option.

Une obligation convertible peut s'évaluer comme un lot comprenant une option d'achat et une obligation classique.

### black-scholes
http://www.fifrance.com/modele_black-scholes.php

### More

- [Simple Interest](https://www.youtube.com/watch?v=qO1SYFZVmhY)
- [Compound Interest](https://www.youtube.com/watch?v=rRgW04Sxe6Q)
- http://www.fifrance.com/mathematiques_financieres.php

- http://www.fifrance.com/louis_bachelier.php
précurseur de la théorie moderne des probabilités et comme le fondateur des mathématiques financières. Dans sa thèse intitulée Théorie de la spéculation, soutenue le 29 mars 1900, il a introduit l'utilisation en finance du mouvement brownien (découvert par Brown, biologiste), qui est à la base de la majorité des modèles de prix en finance, surtout la formule de Black-Scholes (1973).