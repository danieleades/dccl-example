# Acoustic Encoding

## Getting Started

*adapted from https://libdccl.org/*

1. build and install `dccl`
   - install system dependencies

            sudo apt install cmake libboost-dev libprotobuf-dev libprotoc-dev protobuf-compiler

   - build project

            cd dccl
            ./build.sh

    - install

            cd build
            sudo make install

2. set up python project
    - install dependencies
  
            cd ../../python
            poetry install

    - run code-gen

            poetry run code-gen

3. run example

        poetry run python example.py