# CodingWeeks2-jeeth  
  
## Name of the game : Sprint  The Game
  
### Description:   
Our game is inspired by the games ActiveNeurons2 and Color Switch. The character is a square navigating a 2D plane made up of walls of different colors. When a directional key is pressed, the character moves in the corresponding direction until it reaches an obstacle (it's impossible to stop before encountering such an obstacle). An obstacle is considered to be a wall that is not the same color as the player (the player can pass through walls of their own color). 'Color switchers' are placed on the plane: when the player encounters them, their color changes to that of the color switcher (the player can pass through color switchers). The goal is to find the right path to reach the endpoint.

# Structure of the project

The ambition of the project led us to envision an interesting and adaptable structure from the outset, one that would allow us to work together without getting into incessant conflicts. Here is what we proposed:

```markdown
├── assets
| 	├── fonts 	# contains fonts downloaded on internet
│   ├── sounds 	# contains sounds created by Emmanuel
|	├── images 	# contains images created by Emmanuel
|	├── levels	# contains JSON format of each level
├── level	# a package full of module
├── render	# a package full of module
├── effects	# a package full of module
├── editor	# a package full of module
├── game.py
├── main_menu.py
├── sound.py
├── tests.py
├── *main.py*
└── .gitignore
```
### The 'level' package
```markdown
├── level	
|	├── obstacle.py
|	├── grid.py
|	├── level.py
|	├── player.py
|	├── level_loader.py
└── 
```
Each of the modules within the **'level'** package serves to represent an element of the game. Firstly, in the module obstacle.py, there is a representation of what an obstacle is: that is, a color, and what it does to the player (whether it's a starting point, an endpoint, or a **color_switcher**).

This description is depicted within a Obstacle class, which will then be instantiated multiple times to populate an **np.array** of obstacles found in the Grid object from the 'grid.py' module. This grid also contains another attribute, **'size'**, which is a tuple representing the number of squares in length and width of the grid.

Independently, we have created a **'Player'** class in the player.py module, responsible for handling a player who possesses a position, a color, and a destination. This object can then be manipulated by various functions:

```
player.move_up (grid) # move the player up the grid
player.move_down () #...
player.move_right () #...
player.move_left () #...
...
player.update (delta_time) # A function called 'n' times per second (main loop) that dynamically and smoothly moves the player toward its destination de manière dynamique et smooth
```
Finally, the object that encompasses the aforementioned elements to create the game is the **Level** object, which has its own **Grid** as an attribute along with a list of **Player** objects that the user will manipulate. Everything is updated using the 'update' method of the **Level** class, which, among other tasks, checks if the user is in a winning position to trigger the game's victory screen.

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
Each of these modules enables the display of the game within a **Pygame** window. The Surface object encapsulates the Surface object provided natively by PyGame to simplify certain functions, particularly in window creation. The box.py module contains three functions for easily drawing boxes in the color scheme of our game. This module is intended to be used within the modules draw_main_menu.py and draw_end_menu.py, responsible for displaying and managing menus, respectively.

Similar to the above, for the **Level** module, there exist objects such as **LevelRender** and **GridRender** which handle the visual rendering of the level using a render function.

```
level_render.render (surface)
```
It was important to separate the rendering aspect from the logical part so that we could intelligently distribute the work without stepping on each other's toes.

## The Game object and the main.py module

With what we've seen above, we have access to two packages that both represent a level in Python and display it in a **Pygame** window. Thus, we need to assemble them to create our game. The module main.py contains the main function of our program, which needs to be executed to launch our Python program (See the launch instructions following the project structure).

An object 'game' of the **Game** class loads the various levels present in the game, saved in JSON format and loaded using a build_level function in the **level/level_loader.py** module. It then handles updating, displaying, and managing keyboard inputs for a specified level (thanks to the main menu, for example). Alongside displaying the level, the 'game' object also manages the game interface, including the timer, level name, the player's current score, and the maximum score recorded for the level.

The main function will then create all the necessary objects: a **Surface** and a **Game**, and create the **main loop**.

## Effects

As you can see in the game demo, there are numerous effects present in **Sprint The Game**, both in terms of sound and visuals. All of these are managed within a package called effects and a module named sound.py, which enable manipulation of a **LightSystem** object, a **ParticleSystem** object, as well as functions like sound_collision. These various elements are intelligently utilized within the Level and Player classes.

# Tests

The unit testing management focused on the grid and player movements within the grid. For this purpose, we created a module tests.py containing various test functions with assert functions to observe the correct behavior of a player in a 3x3 grid. Additionally, there are different functions to ensure that adding obstacles to the level functions correctly.

# Launch the game
Firstly, we would like to inform you that this README pertains to the final version of the game. If you wish to view and launch the associated MVP (Minimum Viable Product) of this project along with user notes, please proceed to the **MVP-demo** branch : [branch MVP-demo](https://gitlab-student.centralesupelec.fr/enzo.le-van/codingweeks2-jeeth/-/tree/MVP-demo?ref_type=heads)

Instructions for launching the final game are similar to those of the MVP :

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
Everything is achievable directly within the graphical interface, eliminating the need to switch between the terminal and the game window.

# Work distribution

We proceeded with organization in different sprints, where each of us was able to work on various aspects of the game. However, here is an overview of the different topics we covered:

Emmanuel: Main loop, sound management, design choices, timer handling, menu display, main menu management, in-game interface, sorting levels by difficulty.

Henrik: Level creation, testing, next_level button, particle effects.

Thomas: Level creation, Surface encapsulation, hit counter, display of special tiles.

Juliette: Obstacle implementation, grid display, color switcher display, victory menu, in-game interface, level loader, and level editor.

Enzo: Game structure planning, player display, player movement and destination management, player effects, light effects, particle effects.
