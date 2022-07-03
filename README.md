# causal-inference
 <p align="center">![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTt9lRs-eKOVgnS9GKyb0ekY_RWTu6c49cbiA&usqp=CAU) </p>

Table of content 
- [Overview](##overview)
- [Data](##data)
- [Project Structure](##Project-Structure)
- [Requirements](##requirements)
- [installation](##Installation-guide)
- [LICENCE](##LICENCE)

## Overview
A common frustration in the industry, especially when it comes to getting business insights from tabular data, is that the most interesting questions (from their perspective) are often not answerable with observational data alone.

In this spirit, We   are expected to attempt the following tasks:
* Perform a causal inference task using Pearl’s framework;
* Infer the causal graph from observational data and then validate the graph;
* Merge machine learning with causal inference;

## data
You can extract the data from kaggle or from UCI Machine Learning Repository. In the latter you can find even more data that you may explore further. To understand more about the data, and how it is collected we highly recommend reading this paper: (PDF) Breast Cancer Diagnosis and Prognosis Via Linear Programming (researchgate.net).

Features in the data are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass.

1. ID number
2. Diagnosis (M = malignant, B = benign)
3. The remaining (3-32)
Ten real-valued features are computed for each cell nucleus:

a. radius (mean of distances from center to points on the perimeter)

b. texture (standard deviation of gray-scale values)
Perimeter
c. Area

d. smoothness (local variation in radius lengths)
e. compactness (perimeter^2 / area - 1.0)

f. concavity (severity of concave portions of the contour)

g.concave points (number of concave portions of the contour)

h. Symmetry

j. fractal dimension ("coastline approximation" - 1)

## Project-Structure

### Data 
 folder where the dataset files are stored.

### notebooks
jupyter notebook for EDA and modeling

### scripts

modularized python files found

## tests

unit test for the scripts

## Installation-guide

```
conda create --name causality python==3.8
conda activate causality
```
then, 

```
git clone https://github.com/dagmawiii03/causal-Inference.git

cd causal-Inference
sudo python3 setup.py install
```

## requirements
* causalnex
* graphiz
* python >3.5 and <3.8
## License
[MIT](https://choosealicense.com/licenses/mit/)




