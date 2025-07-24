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
    # 1. Fill the whole map with wall tiles
    game_map = [['#' for _ in range(map_width)] for _ in range(map_height)]
    
    rooms = []
    player_start_pos = (0, 0)

    for _ in range(max_rooms):
        w = random.randint(min_room_size, max_room_size)
        h = random.randint(min_room_size, max_room_size)
        # Prevent rooms from touching the map edge
        x = random.randint(1, map_width - w - 2)
        y = random.randint(1, map_height - h - 2)

        new_room = Rect(x, y, w, h)

        # Check if the new room intersects with any existing rooms
        if any(new_room.intersects(other_room) for other_room in rooms):
            continue

        # --- Carve out the room ---
        for ry in range(new_room.y1, new_room.y2):
            for rx in range(new_room.x1, new_room.x2):
                game_map[ry][rx] = '.'

        (new_x, new_y) = new_room.center()

        if not rooms:
            # This is the first room, place the player here
            player_start_pos = (new_x, new_y)
        else:
            # --- Carve hallways to connect to the previous room ---
            (prev_x, prev_y) = rooms[-1].center()

            # Randomly decide to start with a horizontal or vertical tunnel
            if random.randint(0, 1) == 1:
                # Horizontal first, then vertical
                for hx in range(min(prev_x, new_x), max(prev_x, new_x) + 1):
                    game_map[prev_y][hx] = '.'
                for vy in range(min(prev_y, new_y), max(prev_y, new_y) + 1):
                    game_map[vy][new_x] = '.'
            else:
                # Vertical first, then horizontal
                for vy in range(min(prev_y, new_y), max(prev_y, new_y) + 1):
                    game_map[vy][prev_x] = '.'
                for hx in range(min(prev_x, new_x), max(prev_x, new_x) + 1):
                    game_map[new_y][hx] = '.'
        
        rooms.append(new_room)

    return game_map, player_start_pos


# --- Game Settings ---
MAP_WIDTH = 100
MAP_HEIGHT = 40
VIEW_WIDTH = 80
VIEW_HEIGHT = 25

# --- Dungeon Settings ---
MAX_ROOMS = 15
MIN_ROOM_SIZE = 6
MAX_ROOM_SIZE = 10

# --- Generate the Map ---
game_map, (player_x, player_y) = generate_dungeon(
    MAP_WIDTH, MAP_HEIGHT, MAX_ROOMS, MIN_ROOM_SIZE, MAX_ROOM_SIZE
)

# --- Main Game Loop ---
while True:
    # --- Camera Logic ---
    camera_x = player_x - (VIEW_WIDTH // 2)
    camera_y = player_y - (VIEW_HEIGHT // 2)
    camera_x = max(0, min(camera_x, MAP_WIDTH - VIEW_WIDTH))
    camera_y = max(0, min(camera_y, MAP_HEIGHT - VIEW_HEIGHT))

    # --- Drawing Logic ---
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Roguelike Dungeon ---")
    print(f"Player Position: ({player_x}, {player_y}) | Use w/a/s/d to move, 'q' to quit.")
    
    for screen_y in range(VIEW_HEIGHT):
        row = []
        for screen_x in range(VIEW_WIDTH):
            map_x = camera_x + screen_x
            map_y = camera_y + screen_y

            if map_x == player_x and map_y == player_y:
                row.append('@')
            else:
                row.append(game_map[map_y][map_x])
        print(''.join(row))

    # --- Handle Player Input & Movement ---
    move = input("Your move: ").lower()

    if move == 'q':
        break

    next_x, next_y = player_x, player_y
    if move == 'w':
        next_y -= 1
    elif move == 's':
        next_y += 1
    elif move == 'a':
        next_x -= 1
    elif move == 'd':
        next_x += 1

    # --- Collision Detection ---
    # Check if the destination tile is a wall
    if game_map[next_y][next_x] != '#':
        player_x, player_y = next_x, next_y

# --- Runs after the loop breaks ---
print("\nThanks for playing! Goodbye. 👋\n")
