# rpg-game
Trying to vibe code a roguelike, text-based RPG game using
AI-assisted programming.

## Design Decisions
Summary of the design decisions generated from the code generation prompts.
("Please summarize the following prompts into bullet points of game features.")

* **Text-Based RPG:** The game is a classic text-based role-playing adventure. 📜
* **Player Character & Movement:** You control a character represented by an `@` symbol. Movement is handled with the `w` (up), `s` (down), `a` (left), and `d` (right) keys.
* **Dynamic Map & Viewport:** The game world can be much larger than the screen. The display shows an 80x25 "camera" view of the map that stays centered on your character as you move.
* **Boundaries:** The map is enclosed by borders, displayed as stars (`*`), which your character cannot cross.
* **Quit Functionality:** You can exit the game at any time by pressing the `q` key.
