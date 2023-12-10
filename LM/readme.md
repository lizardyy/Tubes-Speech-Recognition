# Language Model

This directory is dedicated to building a language model. The dataset, located in `sentences.txt`, comprises approximately 10,000 sentences sourced from [here](https://wortschatz.uni-leipzig.de/en/download/Indonesian).

## How to Build

The language model was constructed using KenLM. Follow these steps for installation and building:

1. Clone the KenLM repository:
    ```bash
    git clone https://github.com/kpu/kenlm
    ```

2. Install necessary dependencies:
    ```bash
    sudo apt-get install libboost-all-dev libeigen3-dev
    ```

3. Navigate to the KenLM directory:
    ```bash
    cd kenlm
    mkdir build
    cd build
    ```

4. Build KenLM:
    ```bash
    cmake ..
    make -j 4
    sudo make install
    ```

To build the model, execute the following command:
```bash
lmplz -o <n> < sentences.txt > output_model.lm
```

Replace <n> with your desired value for the n-gram model.
