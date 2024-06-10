# schrodinger-1d

Ce projet est un solveur Python pour l'équation de Schrödinger en une dimension, développé initialement pour aider mon père dans son devoir d'analyse numérique pour son Master 1 d'astrophysique. Malgré ses 70 ans, il a décidé de reprendre ses études et je suis ravi de l'avoir aidé dans cette aventure.

Ce code résout l'équation de Schrödinger en tenant compte de la position de la particule et du temps, fournissant ainsi les valeurs de la fonction d'onde au fil du temps et de l'espace.

Je dois admettre que mes connaissances en astrophysique et en mécanique quantique sont limitées. ChatGPT-4 m'a grandement aidé, en expliquant les concepts fondamentaux et en fournissant un code de discrétisation que j'ai adapté. Pour ceux qui sont familiers avec ces sujets, les exemples de potentiels dans [utilities.py](utilities.py) illustreront mon niveau en physique. 😄

Ce projet a été réalisé en une soirée (3-4 heures) après plusieurs discussions avec mon père. Il répond parfaitement aux exigences de son projet numérique, qui aurait normalement pris plusieurs mois pour des étudiants de Master 1 sans l'aide d'outils comme ChatGPT. Je partage ce projet pour démontrer la puissance des IA génératives dans l'accélération du développement.

Bien que je possède un doctorat en Mathématiques Appliquées et une expérience de 7 ans en Python, ainsi qu'une spécialisation en IA générative depuis 2 ans, je n'avais jamais étudié la mécanique quantique avant cela. Ainsi, le "potentiel" pour implémenter correctement un tel solveur est présent (parcours scientifique, expérience soutenue en programmation et connaissance poussée des IA génératives) mais pas "le moment" (je n'ai jamais fait de mécanique quantique dans ma vie). Sans ces outils, il m'aurait au moins fallu plusieurs soirées pour arriver à un tel programme.

Je conclus par un petit message de précaution : bien que j'encourage l'utilisation des IAs Génératives via ce code, je vous invite à les utiliser avec discernement : elles sont puissantes mais peuvent se tromper (comme cela m'est arrivé plus d'une fois en écrivant ce code).

## Utilisation

Clonez ce dépôt sur votre système puis installez les dépendances via `pip` avec la commande suivante :

```shell
python -m pip install -r requirements.txt
```

Exécutez ensuite le script [main.py](main.py) lancer une simulation :

```shell
python main.py
```

Après le calcul, deux images seront générées dans le dossier, représentant respectivement les distributions initiale et finale de la densité de probabilité de la fonction d'onde, ainsi que la surface de sa distribution au fil du temps et de l'espace.

Les paramètres de la simulation sont définis au début de [main.py](main.py). Modifiez-les selon vos besoins en ouvrant le script avec n'importe quel éditeur de texte.
