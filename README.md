# WaveFunctionCollapse
This repo uses the wave function collapse algorithm to generate pixel images, such as mazes and abstract art. It utilizes two different strategies, a crude strategy using side propagation (which was used more as an introduction into the topic), and the more advanced entropy propagation. Read more about both of these strategies in the code comments inside the respective files.


Entropy Propagation can generate intricate pixel art patterns and mazes. It first reads an input image, and breaks it into 2x2 pixel "tiles". Using a dictionary, it takes note of each neighbor from all 4 directions. Using this, the second half of the program (the part that actually generates the images) uses the wave function collapse algorithm on lower entropy tiles until the canvas is filled.

## Mazes
**Here is an example of it in action:**

![maze-out](https://github.com/Abdullah25Mohammad/WaveFunctionCollapse/assets/147211478/ec8dc61a-89b8-412a-9cde-f7f736926232)
![maze-out-1](https://github.com/Abdullah25Mohammad/WaveFunctionCollapse/assets/147211478/64ee452c-d13a-4e8d-8cca-23fc440e3b8c)


The output above were created using the following image as input:

![maze_resized](https://github.com/Abdullah25Mohammad/WaveFunctionCollapse/assets/147211478/b7806f8b-bf59-49f9-a10a-8277fcaf4d91)


## Pixel Art
**Here is an example of it in action:**

![out-input2](https://github.com/Abdullah25Mohammad/WaveFunctionCollapse/assets/147211478/d88c5c3b-1e8c-493b-8318-bc5353855197)
![out-input2-1](https://github.com/Abdullah25Mohammad/WaveFunctionCollapse/assets/147211478/e84a5b32-ea75-462e-863c-7d1487a19663)

The output above were created using the following image as input:

![input2_resized](https://github.com/Abdullah25Mohammad/WaveFunctionCollapse/assets/147211478/902856e6-0ee2-4d66-9e7d-1f8080367ae1)




