import cv2
import numpy as np
from PIL import Image
import time
import random

def read_image(path):
    """
    Read the image from the path
    :param path: the path of the image
    
    :return: the image's matrix
    
    NOTE: this is in black and white (no transparency)
    """
    im = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return im

def get_tiles(image):
    """
    Get the tiles from the image

    :param image: the image's matrix
    :return: the tiles' matrix
    """
    tiles = []
    for i in range(0, image.shape[0], 2):
        for j in range(0, image.shape[1], 2):
            tiles.append(image[i:i+2, j:j+2])
    return tiles

def tile_to_string(tile):
    """
    Convert the tile to a string 

    :param tile: the tile's matrix
    :return: the string of the tile
    """
    l = tile.reshape(4)
    s = ""

    for i in range(4):
        if l[i] == 0:
            s += "0"
        else:
            s += "1"
    
    return s

def image_to_string_list(image):
    """
    Convert the image to a list of strings

    :param image: the image's matrix
    :return: 2d list of strings
    """
    image_list = []
    for i in range(0, image.shape[0], 2):
        row = []
        for j in range(0, image.shape[1], 2):
            row.append(tile_to_string(image[i:i+2, j:j+2]))
        image_list.append(row)
    return image_list

def string_to_tile(s):
    tile = np.zeros((2, 2), dtype=np.uint8)
    for i in range(4):
        if s[i] == "1":
            tile[i//2, i%2] = 255
    return tile

def wave_function_collapse(starting_tile, width, height, tiles):
    output = []
    for y in range(height):
        start_time = time.time()
        row = []
        for x in range(width):
            if y == 0 and x == 0:
                row.append(starting_tile)
            elif y == 0: 
                left_tile = row[x-1]
                possible_tiles = tiles[left_tile]["right"]
                if len(possible_tiles) == 0:
                    possible_tiles = list(tiles.keys())
                row.append(random.choice(possible_tiles))
            elif x == 0:
                up_tile = output[y-1][x]
                possible_tiles = tiles[up_tile]["down"]
                if len(possible_tiles) == 0:
                    possible_tiles = list(tiles.keys())
                row.append(random.choice(possible_tiles))
            else:
                left_tile = row[x-1]
                up_tile = output[y-1][x]
                left_tile_right = tiles[left_tile]["right"]
                up_tile_down = tiles[up_tile]["down"]
                possible_tiles = []
                for i in range(len(left_tile_right)):
                    for j in range(len(up_tile_down)):
                        if left_tile_right[i] == up_tile_down[j]:
                            possible_tiles.append(left_tile_right[i])
                if len(possible_tiles) == 0:
                    possible_tiles = left_tile_right + up_tile_down
                row.append(random.choice(possible_tiles))
        output.append(row)
        end_time = time.time()
        time_elapsed = end_time - start_time
        print("Done with row {} out of {} (took {:.4f} seconds)".format(y+1, height, time_elapsed))
    return output

def add_tile_to_dict(image_list):
    """
    Iterate through the image and add the tiles (and their neighbors) to the dictionary

    :param image_list: the image's matrix
    :return: dictionary with tile information
    """

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


def generate_image(width, height, tiles, out_path=None):
    if out_path is None:
        out_path = "output.png"
    starting_tile = list(tiles.keys())[0]
    output = wave_function_collapse(starting_tile, width, height, tiles)
    image = Image.new("L", (width*2, height*2))
    for i in range(height):
        for j in range(width):
            tile = string_to_tile(output[i][j])
            image.paste(Image.fromarray(tile), (j*2, i*2))
    image.save(out_path)

def main(input_path, width, height, out_path=None):
    image = read_image(input_path)
    tiles = get_tiles(image)
    image_list = image_to_string_list(image)
    tile_dict = add_tile_to_dict(image_list)
    generate_image(width, height, tile_dict, out_path)
    print("done")

if __name__ == "__main__":
    main("input2.png", 128, 128, "output_side.png")