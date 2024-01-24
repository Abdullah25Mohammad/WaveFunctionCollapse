# WaveFunctionCollapse
This repo uses the wave function collapse algorithm to generate pixel images, such as mazes and abstract art. It utilizes two different strategies, a crude strategy using side propagation, and the more advanced entropy propagation.


Entropy Propagation can generate intricate pixel art patterns and mazes. It first reads an input image, and breaks it into 2x2 pixel "tiles". Using a dictionary, it takes note of each neighbor from all 4 directions. Using this, the second half of the program (the part that actually generates the images) uses the wave function collapse algorithm to lower entropy until the canvas is filled.

## Mazes
**Here is an example of it in action:**

![out](https://github.com/Abdullah25Mohammad/WaveFunctionCollapse/assets/147211478/ff6c42b1-52eb-43f5-a02d-434012a2e645)
![out-1](https://github.com/Abdullah25Mohammad/WaveFunctionCollapse/assets/147211478/7f2ed317-d65d-406d-92cc-1866a90664a4)

The above animations were trained on the following image:



