# Blockchain and IPFS Video Upload Simulation

This documentation outlines a local demo simulation designed to mimic the process of uploading video files to IPFS and interacting with a smart contract for storing and retrieving IPFS hashes. This simulation is intended for demonstration purposes, to showcase the concept without requiring actual blockchain or IPFS network interactions.

## Overview

The demo consists of two main parts:

1. **IPFS Simulation**: A Python script (`IPFS_simulate.py`) that simulates the uploading of a video file to IPFS by generating a unique hash for the file, mimicking the IPFS CID (Content Identifier).

2. **Smart Contract Simulation**: A Python script (`SmartContract_Simulate.py`) that simulates storing and retrieving the generated IPFS hash, acting as a mock smart contract.

These simulations provide a simplified model of how videos can be uploaded to IPFS and their references (hashes) stored on the blockchain without incurring transaction costs or requiring network connectivity.

## IPFS Simulation (`IPFS_simulate.py`)

### Purpose

Simulates the process of uploading a video file to the InterPlanetary File System (IPFS) and generating a hash that uniquely identifies the file, similar to an IPFS CID.

### Implementation

The script reads the specified video file, generates a SHA-256 hash to simulate an IPFS CID, and prints the simulated hash.

## Smart Contract Simulation (`SmartContract_Simulate.py`)

### Purpose

Simulates a smart contract's functionality to store and retrieve IPFS hashes associated with user addresses. This acts as a mock-up for how a smart contract on the Ethereum blockchain might interact with IPFS hashes.

### Implementation

The script defines a simple Python class that mimics the functionality of a smart contract by using a dictionary to store user addresses and their corresponding IPFS video hashes. It includes methods for storing and retrieving hashes.

## Combined Demo Workflow

1. **Prepare the Video File**: Ensure that the `demo.mp4` file is located in an accessible path.
2. **Run the IPFS Simulation**: Execute the `IPFS_simulate.py` script to generate and print a simulated IPFS hash for `demo.mp4`.
3. **Store the Hash**: Use the output hash as input for the `SmartContract_Simulate.py` script to simulate storing the hash in the smart contract.
4. **Retrieve and Verify**: Execute the retrieval function in the smart contract simulation to demonstrate obtaining the stored IPFS hash.

## Conclusion

This simulation demonstrates the concept of uploading video files to IPFS and storing their hashes on a blockchain via smart contracts, all in a local environment. While this demo does not interact with actual blockchain or IPFS networks, it provides a conceptual and visual tool for understanding and presenting the process.
