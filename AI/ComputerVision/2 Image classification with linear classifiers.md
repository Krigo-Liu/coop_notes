## 1. Image Classification
problems:
- semantic gap: To computers, images are tensors of integers range from [0,255]
- illumination: light
- background clutter (crowd sth. untidily)
- occlusion: blockage
- deformation: different postures of cats
- interclass variation: a picture with many cats
- context (circumstances): a dog with a shadows of a fence may be recognized as a tiger.

$\color{blue}\text{M: 两个人争吵，打翻了油灯，火花蔓延烟雾出现（身边的易爆物被点燃了），他们发现有好的掩体，蜷缩进去。救援人在飞机高处看到他们紧挨一起，伺机而动。}$

## 2. Two data-driven approach for this task
### 2.1 K-nearest neighbor
### 2.2 Linear classifier