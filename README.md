# NARv Tool and Experimental Data

## About

This repository contains the source code of NARv, the benchmarks and
the experimental data for the ASPLOS'23 Fall submission #426 entitled
"**Abstraction and Refinement: Towards Scalable and Exact Verification
of Neural Networks**".

The evaluation is performed on three widely-used benchmarks and datasets:
- ACAS Xu
- MNIST
- CIFAR-10


## File Tree

The repository is organized in four directories. The file tree is
shown as follows.

```
root
├── README.md
├── tool
├── ACASXu
│   ├── networks/
│   ├── inputs/
│   └── results/
├── MNIST
│   ├── networks/
│   ├── inputs/
│   └── results/
└── CIFAR-10
    ├── networks/
    ├── inputs/
    └── results/
```

## tool

The **tool/** directory contains all the source code of the tool
implementation NARv with a README inside.


## ACAS Xu

ACAS Xu contains 45 DNNs and is used for Performance Evaluation
comparing NARv with CEGAR-NN.

- **networks/** contains the 45 DNNs in the nnet format.

- **inputs/** contains 4 files representing the inputs for 4 different
     perturbation thresholds ranging from 0.01 to 0.04.  Each file
     includes 20 inputs for that corresponding perturbation threshold.

- **results/** contains experimental results for Figures 5 and 7 and
    Table 2 in the submission, organized w.r.t. the perturbation
    thresholds.

    Each csv file named by the tool (e.g. NARv.csv) contains the
    experimental data for that tool. The columns are as follows.

    - *network_id*:  network ID
    
    - *property_id*:  input ID
    
    - *abstract_time*:  time (in seconds) for building the initial abstraction

    - *total_time*: verification time (in seconds)

    - *size*: total size of the (abstract) network when the
       verification succeeds

## MNIST

The DNN trained by MNIST dataset is used for Effectiveness Evaluation
comparing NARv[M] (resp., NARv[P]) with Marabou (resp., Planet).

- **networks/** contains the DNN trained by MNIST dataset in the nnet
    format.

- **inputs/** contains 25 inputs. They are used for each perturbation
    threshold, which ranges from 0.02 to 0.05.

- **results/** contains experimental results for Table 1 and Figure 6
    in the submission, organized w.r.t. the perturbation thresholds.

    Each csv file named by the two tools (e.g. NARv[M]_vs_Marabou.csv)
    contains the experimental data for the comparison between those
    two tools. The columns are as follows.

    - *property_id*:  input ID used for robustness verification
    
    - *{toolname}_time*: verification time (in seconds) spent by the
       tool {toolname}



## CIFAR-10

The two DNNs trained by CIFAR-10 dataset, with hidden neurons 4 x 100
and 6 x 100 respectively, are used for Effectiveness Evaluation
comparing NARv[M] (resp., NARv[P]) with Marabou (resp., Planet).

- **networks/** contains the two DNN trained by CIFAR-10 dataset in
    the nnet format.

- **inputs/** contains 48 inputs. There are 12 inputs for each
perturbation threshold, which ranges from 0.001 to 0.004.

- **results/** contains experimental results for Figures 4 and 8,
     Tables 1 and 3 in the submission, organized w.r.t. the networks
     (4x100 and 6x100, respectively) and then the perturbation
     thresholds.

    Each csv file named by the two tools (e.g. NARv[M]_vs_Marabou.csv)
    contains the experimental data for the comparison between those
    two tools. The columns are as follows.

    - *property_id*:  input ID used for robustness verification
    
    - *{toolname}_time*: verification time (in seconds) spent by the
       tool {toolname}

