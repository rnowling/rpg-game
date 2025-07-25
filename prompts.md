# Prompts
This file stores the prompts used to develop the game.

## Create initial game

> I want to create a text-based role-playing game. Please generate a Python program that generates a map with borders displayed on the screen with stars and the user’s character displayed with an “@“ symbol. The user should be able to move the character up, down, left, or right one space at a time by entering the letters w, s, a, and d. The character should not be able to cross the map’s borders. The map should be no larger than 80 by 25 characters. 

## Make map larger than display window

> Please change the game logic so that the map can be larger than 80 by 25. The game should only show a 80 by 25 region of the map on the console with the user’s character in the center. When the user moves, the displayed region of the map should be updated. 

## Add a quit option

> Please modify the program so that if the user can quit the game by entering the character 'q'. 

## Summarizing game features

> Please summarize the following prompts into bullet points of game features. 
> 
> Prompt 1:
> ...
>
> Prompt 2:
> ...

## Adding rooms and hallways

> Please divide the map into rooms. Each room should have 1 or 2 entryways. The rooms should be connected by hallways.

## Add character energy attribute

> Add a quantitative attribute to the player's character called energy. It's minimum value is 0, while it's maximum value is 100. When the game starts, the character's energy should be initialized to 100. After every turn, the energy should go down by 1 point. If the character's energy reaches 0, the game is over, and the character has lost. 

## Add batteries to give the player energy

>  Add objects called batteries to the game. The battery objects should be displayed using the character "b". The game should start with 20 battery objects. The batteries should should be randomly distributed across the map inside the rooms. When the character's position matches the position of a battery object, the character's energy should be increased by 10 points and the battery object should be removed from the game. 
