# NARv

**NARv**, short for **N**etwork **A**bstraction-**R**efinement for
**v**erification, is a structure-oriented CEGAR (Counterexample-Guided
Abstraction Refinement) based neural network verification tool.


## Build and Dependencies

NARv is implemented based on the tool provided in [1], which uses
[Marabou](https://github.com/NeuralNetworkVerification/Marabou)'s
Python API as the network file parser. We need install Marabou first.


#### Marabou's Python API Installation

To clone Marabou to local, run:

```
git clone https://github.com/NeuralNetworkVerification/Marabou.git
```

To build both Marabou and Maraboupy using CMake, run:

```
cd path/to/marabou/repo/folder
mkdir build 
cd build
cmake .. -DBUILD_PYTHON=ON
cmake --build .
```

After building, add the Marabou root directory to your PYTHONPATH
environmental variable. You can run:

```
export PYTHONPATH=/path/to/marabou/root/
```

## Getting Started

Now, Marabou is available as the back-end engine.

Run an example in the folder *tests/*:

```
sh test_example.sh
```

### References

[1] Yizhak Yisrael Elboher, Justin Gottschlich, Guy Katz: [An
Abstraction-Based Framework for Neural Network
Verification](https://doi.org/10.1007/978-3-030-53288-8_3). CAV (1)
2020: 43-65