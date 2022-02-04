# Terrain Classification via Deep Neural Networks

**Date:** 01.05.2019 

**Note:** This work was done at the begining of my PhD, and at the beginning of my python journey. My ability to code and visualize data has improved significantly since then. Please see my publications or other projects for more recent example.

**Abstract:** In this work, I trained a deep neural network for recognizing the terrain or land use based on pixel level information. This project was undertaken, by the author, to get a first-hand experience in the world of machine learning. In addition, the project was inspired with the prospects of using satellite imagery to identify land use and eventually biotic components on land and find their distinctiong from abiotic life components. 

A more formal and detailed description of this work is available via the "terrain classification" [document (link)](/terrain_classification_compressed.pdf) present in this repository. For any questions or comments, please feel free to contact me. 

## Acknowledgements:
The inspiration to do this project came from the following people:
1. Prof. Dr. Yann Alibert, University of Bern (my PhD superviser)
2. Prof. Dr. Brice Demory, University of Bern
3. Prof. Dr. Raphael Sznitman, University of Bern

## Results:
Example of augmented dataset for creating a more challenging problem. Here, I took images from different terrains and constructed new images which contained many more terrains on a single image. This increases complexity and posed a more difficult problem for the network.
![](/images/compositeimages.png)

Example of some predictions made by the trained neural network:
- images in the left are the actual image seen by the network
- middle panel shows a pixel-level color coded **ground truth**
- right panel shows the predictions from the network

![](/images/predict3.png)
