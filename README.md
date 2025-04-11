# BTCGEN Bitcoin Puzzle Scanner

## Overview
BTCGEN is a Bitcoin puzzle scanner designed to generate and search for private keys in a specified hexadecimal range. This program leverages multithreading to enhance performance while searching for addresses that match a target Bitcoin address.

### Developer Information
- **Name:** Amin Solhi
- **Email:** [amin.solhi@gmail.com](mailto:amin.solhi@gmail.com)
- **Phone:** +9891111842779

## Prerequisites
- Python 3.x
- Required libraries: `bitcoin`, `ecdsa`

You can install the required libraries using pip:

```bash
pip install bitcoin ecdsa
```

## Usage
To run the BTCGEN Bitcoin Puzzle Scanner, you need to provide several command-line arguments for configuration. Below are the descriptions and usage patterns of the available arguments:

### Command-Line Arguments

- `-s`, `--start_hex`  
  **Description:** Starting hexadecimal private key.  
  **Example:** `-s 40000000000000000`

- `-e`, `--end_hex`  
  **Description:** Ending hexadecimal private key.  
  **Example:** `-e 80000000000000000`

- `-o`, `--output_file`  
  **Description:** Output file to save results.  
  **Default:** `data.txt`  
  **Example:** `-o results.txt`

- `-a`, `--target_address`  
  **Description:** Target Bitcoin address to search for.  
  **Default:** `1BY8GQbnueYofwSuFAT3USAhGjPrkxDdW9`  
  **Example:** `-a 1ABC...XYZ`

- `-t`, `--Thread`  
  **Description:** Number of threads to use for the search.  
  **Default:** `1`  
  **Example:** `-t 4`

- `-r`, `--Random_per`  
  **Description:** Enable random mode and specify the number of keys to generate (in Kilo Key Space).  
  **Example:** `-r 1000`

### Example Command
Here’s an example of how to run the program:

```bash
python btcgen.py -s 40000000000000000 -e 80000000000000000 -o results.txt -a 1BY8GQbnueYofwSuFAT3USAhGjPrkxDdW9 -t 4 -r 100
```

## Functionality
- **Private Key Generation:** The program generates private keys within the specified range, or in random mode based on user preference.
- **Address Comparison:** For each generated private key, it checks if the corresponding Bitcoin address matches the target address.
- **Multithreading:** The scanner can run multiple threads to speed up the scanning process.
- **Output:** Found private keys are recorded in the specified output file.

## Note
- The program may run for extended periods based on the size of the key range and the target address's randomness. Please ensure to monitor the process and manage resources accordingly.

## License
This project is open-source and available for personal use. For commercial use, please contact the developer.

## Support
For any questions, issues, or feature requests, feel free to reach out via email.

---

This README should help users get started with the BTCGEN Bitcoin Puzzle Scanner effectively. If you need further clarification or additional information, feel free to ask!
