Some History of CV

1959 Hubel & Wiesel, Optical Development in Kittens 小猫光学发育


**1958 $\color{violet}\text{Perceptron}$(one of the linear classifiers)**: Could learn to recognize letters of the alphabet


1963 Larry Roberts, Machine Perception of Three-Dimensional Solids
- photograph of solid objs --> line drawing --> 3D representation --> display at any point of view


1969 Minsky and Papert.  $\color{violet}\text{Perceptrons could not learn the XOR function.}$ Caused a lot of disillusionment in the field


1970s David Marr.
- input img --> primal sketch -->  2 ½-D Sketch --> 3-D Model representation
- 2 ½-D Sketch:
    - we don't actually see all 3 dimensions surrounding us but we construct the 3 dimensions in our mind and project them onto the objects surrounding us.
    - The key to perceiving three dimensions is that we have two retinae. 

1970s Recognition via parts:  Generalized Cylinders, pictorial structures
1980s 
   - Recognition via edge detection
   - 1980 Neocognitron: Interleaved simple cells (convolution) and complex cells (pooling). Nopractical training algorithm
   - 1986 Backpropagation: computing gradients in NN. $\color{violet}\text{Trained perceptrons with multiple layers.}$

1990s 
   - Recognition via grouping
   - Convolutional Networks. LeCun et al. Applied backprop algorithm to a Neocognitron-like architecture.


2000s 
   - Recognition via matching. e.g. match the "stop" sign to a different angle stop sign img.
   - Face detection
   - PASCAL visual obj challenge, IMAGENET large scale visual recognition challenge
   - 2012 Alexnet. (DL)

Drawbacks of CV: Stereotypes...

Lecture 4 is pytorch tutorial slides, no notes.
References
1. https://www.princeton.edu/~freshman/science/marr/2_D.html