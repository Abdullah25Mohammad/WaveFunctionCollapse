# WaveFunctionCollapse
This repo uses the wave function collapse algorithm to generate pixel images, such as mazes and abstract art. It utilizes two different strategies, a crude strategy using side propagation, and the more advanced entropy propagation.


Entropy Propagation can generate intricate pixel art patterns and mazes. It first reads an input image, and breaks it into 2x2 pixel "tiles". Using a dictionary, it takes note of each neighbor from all 4 directions. Using this, the second half of the program (the part that actually generates the images) uses the wave function collapse algorithm to lower entropy until the canvas is filled.

## Mazes
**Here is an example of it in action:**

![out](https://github.com/Abdullah25Mohammad/WaveFunctionCollapse/assets/147211478/ff6c42b1-52eb-43f5-a02d-434012a2e645)
![out-1](https://github.com/Abdullah25Mohammad/WaveFunctionCollapse/assets/147211478/7f2ed317-d65d-406d-92cc-1866a90664a4)

The output above were created using the following image as input:

![maze_resized](https://github.com/Abdullah25Mohammad/WaveFunctionCollapse/assets/147211478/b7806f8b-bf59-49f9-a10a-8277fcaf4d91)


## Pixel Art
**Here is an example of it in action:**

![out-input2](https://github.com/Abdullah25Mohammad/WaveFunctionCollapse/assets/147211478/d88c5c3b-1e8c-493b-8318-bc5353855197)
![out-input2-1](https://github.com/Abdullah25Mohammad/WaveFunctionCollapse/assets/147211478/e84a5b32-ea75-462e-863c-7d1487a19663)

The output above were created using the following image as input:

![input2_resized](https://github.com/Abdullah25Mohammad/WaveFunctionCollapse/assets/147211478/902856e6-0ee2-4d66-9e7d-1f8080367ae1)




