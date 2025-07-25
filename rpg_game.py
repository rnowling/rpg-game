import os
import random

# --- Game Class for Rectangular Rooms ---
class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        """Returns the center coordinate of the room."""
        center_x = (self.x1 + self.x2) // 2
        center_y = (self.y1 + self.y2) // 2
        return (center_x, center_y)

    def intersects(self, other):
        """Returns true if this rectangle intersects with another one."""
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)

# --- Dungeon Generation ---
def generate_dungeon(map_width, map_height, max_rooms, min_room_size, max_room_size):
    """Generates a new dungeon map."""
    game_map = [['#' for _ in range(map_width)] for _ in range(map_height)]
    rooms = []
    player_start_pos = (0, 0)

    for _ in range(max_rooms):
        w = random.randint(min_room_size, max_room_size)
        h = random.randint(min_room_size, max_room_size)
        x = random.randint(1, map_width - w - 2)
        y = random.randint(1, map_height - h - 2)
        new_room = Rect(x, y, w, h)

        if any(new_room.intersects(other_room) for other_room in rooms):
            continue

        # Carve out the room's floor
        for ry in range(new_room.y1, new_room.y2):
            for rx in range(new_room.x1, new_room.x2):
                game_map[ry][rx] = '.'

        (new_x, new_y) = new_room.center()

        if not rooms:
            player_start_pos = (new_x, new_y)
        else:
            (prev_x, prev_y) = rooms[-1].center()
            # Carve L-shaped hallways
            if random.randint(0, 1) == 1:
                for hx in range(min(prev_x, new_x), max(prev_x, new_x) + 1):
                    game_map[prev_y][hx] = '.'
                for vy in range(min(prev_y, new_y), max(prev_y, new_y) + 1):
                    game_map[vy][new_x] = '.'
            else:
                for vy in range(min(prev_y, new_y), max(prev_y, new_y) + 1):
                    game_map[vy][prev_x] = '.'
                for hx in range(min(prev_x, new_x), max(prev_x, new_x) + 1):
                    game_map[new_y][hx] = '.'
        
        rooms.append(new_room)
    return game_map, player_start_pos, rooms

# --- Game Settings ---
MAP_WIDTH = 100
MAP_HEIGHT = 40
VIEW_WIDTH = 80
VIEW_HEIGHT = 25
NUM_APPLES = 20

# --- Dungeon Settings ---
MAX_ROOMS = 15
MIN_ROOM_SIZE = 6
MAX_ROOM_SIZE = 10

# --- Initialize Game ---
game_map, (player_x, player_y), room_list = generate_dungeon(
    MAP_WIDTH, MAP_HEIGHT, MAX_ROOMS, MIN_ROOM_SIZE, MAX_ROOM_SIZE
)

# Initialize player energy
MAX_ENERGY = 100
player_energy = MAX_ENERGY
ENERGY_PER_APPLE = 5

# Place apples
apples = []
floor_tiles_in_rooms = []
for room in room_list:
    for y in range(room.y1, room.y2):
        for x in range(room.x1, room.x2):
            if (x, y) != (player_x, player_y):
                floor_tiles_in_rooms.append((x, y))

if len(floor_tiles_in_rooms) >= NUM_APPLES:
    apples = random.sample(floor_tiles_in_rooms, NUM_APPLES)

status_message = ""

# --- Main Game Loop ---
while True:
    # --- Drawing Logic ---
    os.system('cls' if os.name == 'nt' else 'clear')
    
    camera_x = max(0, min(player_x - (VIEW_WIDTH // 2), MAP_WIDTH - VIEW_WIDTH))
    camera_y = max(0, min(player_y - (VIEW_HEIGHT // 2), MAP_HEIGHT - VIEW_HEIGHT))

    print("--- Roguelike Dungeon ---")
    status_line = f"Position: ({player_x}, {player_y}) | Energy: {player_energy}/{MAX_ENERGY}"
    print(status_line)
    if status_message:
        print(status_message)

    for screen_y in range(VIEW_HEIGHT):
        row = []
        for screen_x in range(VIEW_WIDTH):
            map_x, map_y = camera_x + screen_x, camera_y + screen_y
            
            if map_x == player_x and map_y == player_y:
                row.append('@')
            elif (map_x, map_y) in apples:
                row.append('a')
            else:
                row.append(game_map[map_y][map_x])
        print(''.join(row))

    # --- Game Over Check ---
    if player_energy <= 0:
        print("\nYou ran out of energy! Game Over. 💀")
        break

    # --- Handle Player Input ---
    status_message = "" # Clear message each turn
    prompt = "Your move (w/a/s/d) or 'q' to quit: "
    move = input(prompt).lower()

    if move == 'q':
        break
    
    if move in ['w', 'a', 's', 'd']:
        player_energy -= 1

        next_x, next_y = player_x, player_y
        if move == 'w':
            next_y -= 1
        elif move == 's':
            next_y += 1
        elif move == 'a':
            next_x -= 1
        elif move == 'd':
            next_x += 1

        if game_map[next_y][next_x] != '#':
            player_x, player_y = next_x, next_y
            
            # --- Check for apple consumption ---
            if (player_x, player_y) in apples:
                player_energy = min(MAX_ENERGY, player_energy + ENERGY_PER_APPLE)
                apples.remove((player_x, player_y))
                status_message = f"You found an apple! +{ENERGY_PER_APPLE} energy."

# --- Runs after the loop breaks ---
print("\nThanks for playing! Goodbye. 👋\n")
