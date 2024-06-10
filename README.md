# schrodinger-1d

Ce code est un petit code Python que j'ai créé pour m'amuser lorsque j'aidais mon père pour son devoir d'analyse numérique de son Master 1 d'astrophysique (oui, il a repris ses études OKLM à 70 ans avec un master d'astrophysique). Il s'agit d'un solveur de l'équation de Schrödinger dans le cas uni-dimensionnel. Le solveur prends en compte la position de la particule ainsi que le temps, et renvoie toutes les valeurs de la fonction d'onde au cours du temps et à travers l'espace considéré.

Je n'aurai pas la prétention de dire que je maîtrise les concepts d'astro-physique suite à ce code. En effet, je me suis **FORTEMENT** aidé de ChatGPT-4o, qui m'a expliqué, avec une infinie patience, les rudiments de l'équation de Schrödinger dans le cas unidimensionnel. Il m'a aussi évidemment fourni le code de discrétisation de l'équation, que j'ai adapté à ma sauce. Enfin, je suis bien incapable d'implémenter quoi que ce soit dans le cas multi-dimensionnel, et encore moins d'expliquer quoi que ce soit, multi-dimensionnel ou non, à propos de l'équation de Schrödinger. Et je n'ai qu'une très (très) vague idée de ce qu'est une fonction d'onde. D'ailleurs, pour les plus calés en physique d'entre vous, il suffit de voir les potentiels d'exemples que je définis dans le script [utilities.py](utilities.py) pour vous rendre compte de mon niveau en physique... :-)

Tout de même : ce code est le résultat d'une soirée seulement (3 ou 4 heures) consacrée à son implémentation, précédée de plusieurs discussions avec mon père autour du problème. Et il réponds complètement à ce qui était demandé pour son projet numérique, projet qu'il avait plusieurs mois pour faire. Grâce à ChatGPT 4o, j'ai pu réaliser en une soirée ce qui auraît dû prendre un mois ou deux à des étudiants en master 1 sans l'aide de ces outils. Je tenais donc à partager ce projet, afin de montrer à quel point les IAs Génératives pouvait accélerer le processus de développement quand on sait les utiliser.

Evidemment, je ne pars pas de rien : j'ai un doctorat en Mathématiques Appliquées, cela fait maintenant 7 ans que je travaille avec Python et bientôt 2 ans que je me spécialise dans les IAs Génératives (à l'heure où j'écris ces lignes). Cependant, je n'ai jamais fait de Mécanique Quantique, et je ne connais l'équation de Schrödinger que de nom. Ainsi, le "potentiel" pour implémenter correctement un tel solveur est présent (parcours scientifique, expérience soutenue en programmation et connaissance poussée des IAs Génératives) mais pas "le moment" (je n'ai jamais fait de Mécanique Quantique dans ma vie). Sans ces outils, il m'aurait fallu au moins plusieurs soirées pour arriver à un tel programme.

Bref, bonne lecture à toutes et à tous. Et utilisez les IAs avec sagesse : bien qu'elles soient très puissantes, elles peuvent se tromper (ce qui est arrivé plus d'une fois en écrivant ce code ^^) !

## Utilisation

Clonez ce dépôt sur votre système puis installez les dépendances via `pip` avec la commande suivante :

```shell
python -m pip install -r requirements.txt
```

Il vous suffit ensuite d'exécuter le script [main.py](main.py) avec l'environnement python ci-dessus pour effectuer une simulation :

```shell
python main.py
```

Une fois le calcul terminé, vous verrez apparaître deux images dans ce dossier qui représenteront respectivement les distributions initiales et finales de la densité de probabilité de la fonction d'onde ainsi que la surface représentant la distribution de cette dernière à travers le temps et l'espace.

Les paramètres de la simulation sont définis au début de [main.py](main.py). Il vous suffit d'ouvrir le script avec n'importe quel éditeur de texte et de les modifier à votre convenance.
