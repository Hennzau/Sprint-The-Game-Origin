# CodingWeeks2-jeeth  
  
## Nom du jeu : Sprint  The Game
  
### Description :   
Notre jeu est inspiré des jeux activeneurons2 et color switch.  
Le personnage est un carré qui évolue sur un plan en 2D composé de murs de différentes couleurs. Lorsqu'une touche directionnelle est pressée, le personnage se déplace dans la direction correspondante jusqu'à atteindre un obstacle (impossible de s'arrêter avant de rencontrer un tel obstacle). Est considéré comme un obstacle un mur qui n'est pas de la même couleur que le joueur (le joueur passe à travers les murs de sa couleur). Des "color switchers" sont disposés sur le plan : quand le joueur les rencontre, sa couleur devient celle du color switcher (le joueur passe à travers les color switcher). Le but est de trouver le bon chemin pour atteindre le point d'arrivée.

# Structuration du projet

L'ambition du projet a fait que nous devions dès le début imaginer une structure intéressante et modulable sur laquelle nous pouvions travailler à plusieurs sans rentrer dans d'incessants conflits. Voici ce que nous avons proposé :

```markdown
├── assets
| 	├── fonts 	# contient les fonts récupérées sur internet
│   ├── sounds 	# contient les sons créés par Emmanuel
|	├── images 	# contient les illustrations créées par Emmanuel
|	├── levels	# contient la liste des niveaux au format JSON
├── level	# un package contenant des modules
├── render	# un package contenant des modules
├── effects	# un package contenant des modules
├── editor	# un package contenant des modules
├── game.py
├── main_menu.py
├── sound.py
├── tests.py
├── *main.py*
└── .gitignore
```
### Le package 'level'
```markdown
├── level	
|	├── obstacle.py
|	├── grid.py
|	├── level.py
|	├── player.py
|	├── level_loader.py
└── 
```
Chacun des modules présents dans le package **'level'** permet de représenter un élément du jeu. D'abord ce qu'est un obstacle dans le module obstacle.py: c'est à dire une couleur, et ce qu'il fait au joueur (est ce que c'est une case de départ, de fin, est-ce que c'est un **color_switcher** ?). 

Cette description est représentée dans une class **Obstacle** qui sera ensuite instanciées plusieurs fois afin de remplir un **np.array** obstacles présent dans l'objet **Grid** dumodule 'grid.py'. Cette grille contient aussi un autre attribut **'size'** qui est un tupple représentant le nombre de cases en longueur et en largeur de la grille.

De manière indépendante nous avons créé une class **'Player'** dans le module player.py. qui se charge de manipuler un joueur qui a une **position**, une **couleur** et une **destination**. Cet objet est alors manipulable par différente fonctions :
```
player.move_up (grid) # bouge le joueur vers le haut dans la grille 'grid'
player.move_down () #...
player.move_right () #...
player.move_left () #...
...
player.update (delta_time) # fonction appelée n fois par secondes 
# (main loop) qui vient déplacer le joueur vers sa destination 
# de manière dynamique et smooth
```
Enfin l'objet qui vient englober les précécents afin de faire le jeu est l'objet **Level** qui possède sa propre **Grid** en attribut ainsi qu'il liste de **Player** que l'utilisateur manipulera. Tout est mis à jour grâce à la méthode 'update' de la class **Level** qui s'occupe entre autre de vérifier si l'utilisateur est en position gagnante pour lancer l'écran de victoire du jeu.

### Le package 'render'
```markdown
├── render
|	├── surface.py
|	├── grid render.py
|	├── level render.py
|	├── draw player.py
|	├── draw main menu.py
|	├── draw end menu.py
|	├── box.py
└── 
```
Chacun de ses modules permet l'affichage du jeu dans une fenêtre **Pygame**, l'object **Surface** encapsule l'objet Surface proposé nativement par PyGame afin de faciliter certaines fonctions, surtout au niveau de la création de la fenêtre. Le module **box.py** contient 3 fonctions permettant de dessiner des boîtes simplement dans la gamme de couleur de notre jeu, ce module est destiné à être utilisé dans les modules draw_main_menu.py et draw_end_menu.py, qui permettent d'afficher un menu et de les gérer. de même pour le **Level** sont présents un objet **LevelRender**, et **GridRender** qui gère l'affichage du niveau grâce à une fonction render
```
level_render.render (surface)
```
Il a été important de séparer la partie rendu de la partie logique afin que l'on puisse se répartir le travail intélligemment sans se marcher sur les pieds.

## L'objet game et le module main.py

Avec ce que nous avons vu plus haut nous avons accès à deux packages permettant à la fois de représenter un niveau en python et de l'afficher dans une fenêtre pygame. Il faut donc les assembler afin de créer notre jeu. Le module main.py contient la fonction **main** de notre programme, qui doit être éxécutée pour lancer notre programme python (Voir les indications de lancement qui suivront la structuration du projet). 

Un objet game de la class **Game** charge en mémoire les différents niveaux présents dans le jeu, enregistrés au format JSON et chargées grâce à une fonction **build_level** dans le module **level/level_loader.py**. Il s'occupe alors de mettre à jour, d'afficher et de gérer les entrées claviers pour un niveau que nous pouvons lui spécifier (grâce au main menu par exemple). En même temps que d'afficher le niveau, l'objet game s'occupe également d'afficher l'interface du jeu, c'est à dire le timer, le nom du niveau, le score actuel du joueur et le score max enregistré sur le niveau.

La fonction **main** va alors créer tous les objets dont nous avons besoin : c'est à dire une **Surface** et un **Game** et créer la boucle principale (c'est à dire la main_loop)

## Les effets

Comme vous pouvez le voir sur la démo du jeu, il y'a de nombreux effets présents dans Sprint The Game, que ce soit au niveau sonore ou au niveau visuel. Tout ceci est fait dans un package **effects** et un module **sound.py** qui permettent de manipuler un objet **LightSystem**, un objet **ParticleSystem** ainsi que des fonctions comme **sound_collision**. Ces différents éléments sont utilisés intelligemment dans les class **Level et Player**. 

# Les tests unitaires

La gestion des tests unitaires a concerné la grille et les déplacements du joueur dans la grille. Pour cela nous avons créé un module **tests.py** qui contient différentes fonctions de test avec des fonctions `assert` pour observer le bon comportement d'un joueur dans une grille 3x3, ou encore différentes fonctions pour être sur que l'ajout d'obstacles dans le niveau fonctionne

# Lancer le jeu
D'abord nous tenons à vous informer que le présent README concerne la version finale du jeu, si vous souhaitez voir et lancer le MVP associé à ce projet ainsi que les notes à l'utilisateur, merci de vous rendre dans la branch **MVP-demo** : [branch MVP-demo](https://gitlab-student.centralesupelec.fr/enzo.le-van/codingweeks2-jeeth/-/tree/MVP-demo?ref_type=heads)

Les instructions de lancement du jeu final sont similaire à celle du MVP :

Here's what you need to do:
- Clone this branch from our repository to your computer:
```
git clone https://gitlab-student.centralesupelec.fr/enzo.le-van/codingweeks2-jeeth.git
```
- The game has been developed under Python 3.11.5, but it should be compatible with any version of Python >3.11 on both MacOS and Windows. Therefore, make sure you have such a version with the following command. If not, you can download and update your Python using the following link:
```
python --version
```
https://www.python.org/downloads/release/python-3115/
- Next, you need to install the libraries used in this project, which are two in number and specified in the 'requirements.txt' file. However, to avoid compromising your global Python installation, we suggest working with a virtual environment. This means having a separate Python and pip integrated directly into the project. Open a terminal in the cloned folder:
```
python -m venv venv
.\venv\Scripts\pip install -r requirements.txt
```
- You can then launch the game by executing:
```
.\venv\Scripts\python main.py
```
Tout est alors faisable directement dans l'interface graphique, plus besoin de switcher entre terminal et fenêtre du jeu.

# Répartition du travail

Nous avons procédé à une organisation en différents Sprints, où nous avons tous pu toucher à toutes les parties du jeu. Néanmoins voici en globalité les différents sujets que nous avons abordé :

- Emmanuel : main loop, gestion des sons, choix du design, gestion du timer, affichage des menus, gestion du menu principal, interface ingame, trie des niveaux par difficultés

- Henrik : la création des niveaux, les tests, le bouton next_level, des effets de particules

- Thomas : la création des niveaux, l'encapsulation Surface, hit counter, affichage des cases spéciales

- Juliette : Obstacle, affichage de la grille, des color switcher, menu de victoire, interface ingame, level loader et level editor

- Enzo : Penser la structure du jeu, affichage du joueur, gestion des déplacements et destinations du joueur. Effets sur le joueur, Effets de lumière, de particules
