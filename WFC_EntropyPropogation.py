import cv2
import random
import numpy as np
from PIL import Image

def read_image(path):
    im = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return im

def get_tiles(image):
    tiles = []
    for i in range(0, image.shape[0], 2):
        for j in range(0, image.shape[1], 2):
            tiles.append(image[i:i+2, j:j+2])
    return tiles

def tile_to_string(tile):
    l = tile.reshape(4)
    s = ""
    for i in range(4):
        if l[i] == 0:
            s += "0"
        else:
            s += "1"
    return s

def image_to_string_list(image):
    image_list = []
    for i in range(0, image.shape[0], 2):
        row = []
        for j in range(0, image.shape[1], 2):
            row.append(tile_to_string(image[i:i+2, j:j+2]))
        image_list.append(row)
    return image_list

def add_tile_to_dict(image_list):
    data = {}
    for i in range(len(image_list)):
        row = image_list[i]
        for j in range(len(row)):
            tile = row[j]
            if tile not in data:
                data[tile] = {
                    "up": [],
                    "left": [],
                    "down": [],
                    "right": []
                }
            tile_info = data[tile]

            if i > 0:
                top = image_list[i-1][j]
                tile_info["up"].append(top)
            if j > 0:
                left = image_list[i][j-1]
                tile_info["left"].append(left)
            if i < len(image_list) - 1:
                down = image_list[i+1][j]
                tile_info["down"].append(down)
            if j < len(row) - 1:
                right = image_list[i][j+1]
                tile_info["right"].append(right)
            
            data[tile] = tile_info
    return data


"""
The previous part is about converting the image to a dictionary. 
This part is about using that dictionary to make an image (Wave Function Collapse)
"""

class Tile:
    def __init__(self, x, y, tile_dict, tile_type=None):
        self.x = x
        self.y = y

        self.tile_dict = tile_dict

        self.tile_type = tile_type
        if self.tile_type is None:
            self.possibilities = []
        else:
            self.possibilities = [self.tile_type]
        
        self.up = None
        self.left = None
        self.down = None
        self.right = None

        self.collapsed = False
    
    def collapse(self):
        if len(self.possibilities) == 0:
            # print(f"No possibilities for tile at {str(self.x)}, {str(self.y)}")
            self.possibilities = list(self.tile_dict.keys()) # Reset possibilities
        
        self.tile_type = random.choice(self.possibilities)
        self.possibilities = [self.tile_type]

        self.collapsed = True


        if (self.up != None) and (self.up.collapsed == False):
            self.up.possibilities = find_overlap(self.up.possibilities, self.tile_dict[self.tile_type]["up"])
        
        if (self.left != None) and (self.left.collapsed == False):
            self.left.possibilities = find_overlap(self.left.possibilities, self.tile_dict[self.tile_type]["left"])
        
        if (self.down != None) and (self.down.collapsed == False):
            self.down.possibilities = find_overlap(self.down.possibilities, self.tile_dict[self.tile_type]["down"])

        if (self.right != None) and (self.right.collapsed == False):
            self.right.possibilities = find_overlap(self.right.possibilities, self.tile_dict[self.tile_type]["right"])


    def remove_possibility(self, possibility):
        for i in range(len(self.possibilities)): # Remove all instances of possibility
            if self.possibilities[i] == possibility:
                self.possibilities.pop(i)

    def add_neighbor(self, neighbor, direction):
        if direction == "up":
            self.up = neighbor
        elif direction == "left":
            self.left = neighbor
        elif direction == "down":
            self.down = neighbor
        elif direction == "right":
            self.right = neighbor
        else:
            raise Exception("Invaltype direction: " + direction)
        
    def get_neighbors(self, direction):
        if direction == "up":
            return self.up
        elif direction == "left":
            return self.left
        elif direction == "down":
            return self.down
        elif direction == "right":
            return self.right
        else:
            raise Exception("Invaltype direction: " + direction)

def find_overlap(list1, list2):
    """
    Find the overlap between two lists
    """
    overlap = []
    for item in list1:
        if item in list2:
            overlap.append(item)
    return overlap

class Canvas:
    def __init__(self, width, height, tile_dict, possible_tiles=[]):
        """
        NOTE: Dimensions are in tiles, not pixels
        """
        self.width = width
        self.height = height

        self.tile_dict = tile_dict

        self.possible_tiles = possible_tiles

        self.tiles = []
        self.init_empty()

        self.uncollapsed_tiles = [self.tiles[y][x] for y in range(self.height) for x in range(self.width)]

    def init_empty(self):
        self.tiles = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                
                t = Tile(x=x, y=y, tile_dict=self.tile_dict, tile_type=None)
                t.possibilities = self.possible_tiles

                if y > 0:
                    t.add_neighbor(self.tiles[y-1][x], "up")
                    self.tiles[y-1][x].add_neighbor(t, "down")
                if x > 0:
                    t.add_neighbor(row[x-1], "left")
                    row[x-1].add_neighbor(t, "right")

                row.append(t)
            self.tiles.append(row)


    def get_tile_with_lowest_entropy(self):
        # Get the tile with lowest entropy (least possibilities)
        lowest_entropy_tile = None
        for y in range(self.height):
            for x in range(self.width):
                t = self.tiles[y][x]
                if t.collapsed == False:
                    if lowest_entropy_tile is None:
                        lowest_entropy_tile = t
                    elif len(t.possibilities) < len(lowest_entropy_tile.possibilities):
                        lowest_entropy_tile = t
        
        return lowest_entropy_tile

    def collapse(self, starting_tile):
        """
        Collapse the canvas
        """

        starting_tile.collapse()
        self.uncollapsed_tiles.remove(starting_tile)

        i = 0
        while True:
            i += 1
            lowest_entropy_tile = self.get_tile_with_lowest_entropy()


            if lowest_entropy_tile is None:
                lowest_entropy_tile = random.choice(self.uncollapsed_tiles)

            lowest_entropy_tile.collapse()
            self.uncollapsed_tiles.remove(lowest_entropy_tile)

            if len(self.uncollapsed_tiles) == 0:
                break
            
            if i % 100 == 0:
                print("Done with {}/{} tiles".format(self.width*self.height - len(self.uncollapsed_tiles) - 1, self.width*self.height))

def string_to_tile(s):
    """
    Convert the string to a tile

    :param s: the string of the tile
    :return: the tile's matrix
    """
    tile = np.zeros((2, 2), dtype=np.uint8)
    for i in range(4):
        if s[i] == "1":
            tile[i//2, i%2] = 255
    return tile

def generate_image(canvas, seed_x=0, seed_y=0, output_path="output.png"):
    """
    Make an image from the canvas
    """
    canvas.collapse(canvas.tiles[seed_y][seed_x])

    image = Image.new("L", (canvas.width*2, canvas.height*2))

    for y in range(canvas.height):
        for x in range(canvas.width):
            tile = string_to_tile(canvas.tiles[y][x].tile_type)
            image.paste(Image.fromarray(tile), (x*2, y*2))

    image.save(output_path)

def main(input_path):
    image = read_image(input_path)
    tiles = get_tiles(image)
    image_list = image_to_string_list(image)
    tile_dict = add_tile_to_dict(image_list)
    return tile_dict


if __name__ == "__main__":
    SIZE = 64
    tile_dict = main("maze.png")

    canvas = Canvas(
        width=SIZE, 
        height=SIZE, 
        tile_dict=tile_dict, 
        possible_tiles=list(tile_dict.keys())
        )
        
    generate_image(canvas=canvas, seed_x=SIZE//2, seed_y=SIZE//2, output_path="output_entropy.png")
