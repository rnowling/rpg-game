# rpg-game
Trying to vibe code a roguelike, text-based RPG game using
AI-assisted programming.

The prompts I'm using are in the [prompts.md](prompts.md) file.
I'm using Google Gemini 2.5 Pro as the AI.

## Design Decisions
Summary of the design decisions generated from the code generation prompts.

* **Text-Based RPG:** The game is a role-playing game that uses text characters for its interface and graphics.
* **Player Control:** The user controls a character, represented by an '@' symbol, on a 2D map.
* **Movement System:** The character can be moved one space at a time using the **W** (up), **S** (down), **A** (left), and **D** (right) keys. The user can also quit the game by pressing **Q**.
* **Scrolling Viewport:** The game displays an 80x25 portion of a potentially larger map. As the player moves, this viewport scrolls to keep the player character in the center.
* **Collision Detection:** The player character is unable to move through walls or outside the map's boundaries.
* **Map Structure:** The world is divided into **rooms** connected by **hallways**. Each room is designed to have one or two entryways.
