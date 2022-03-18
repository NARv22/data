# Boosting Neural Network Verification by Abstraction-Refinement Techniques

## About

This is a novel abstraction-refinement approach to boost DNN verification by reducing network sizes. We implement our approach using two precise and promising tools Marabou and Planet as the underlying verification engines, and evaluate on benchmarks ACAS Xu, MNIST and CIFAR-10. 

This repository contains three folders named with the corresponding benchmarks. 

- ACAS Xu
- MNIST
- CIFAR-10

Each folder contains the neural network required for verification along with the input properties and output properties. Specifically, for the MNIST, a input property consists of a input image and a perturbation value, and the output property is robustness over input range. For the ACASXu and CIFAR-10, input range is given directly for each property, and the target output is also labeled.

## File Tree

The file tree of our dataset can be shown as follows.  

```
root
├── ACASXu
│   ├── network_inputs
│   ├── 0.01 ~ 0.04     # the results of different perturbation value
│   └── networks
├── CIFAR-10
│   ├── network_inputs
│   ├── 0.001 ~ 0.004     
│   └── networks
└── MNIST
    ├── network_inputs
    ├── 0.02 ~ 0.05     
    └── networks


```

The experimental results are recorded in the form of .csv files.
