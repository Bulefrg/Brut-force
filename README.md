**Password Cracker README**

This repository contains a Python script for cracking passwords using various techniques, including brute-force attacks and dictionary-based approaches. Below is an overview of the functionalities and usage of the script.

### Features

1. **Common Password Check:** The script checks if the provided password matches with common passwords and first names stored in datasets.
2. **Brute-Force with Digits:** It attempts to crack the password by trying all possible combinations of digits.
3. **Brute-Force with Digits and Lowercase Letters:** If not successful with digits only, it extends the search to include lowercase letters.
4. **Brute-Force with Various Characters:** If the password remains elusive, it resorts to an exhaustive brute-force attack with digits, lowercase and uppercase letters, and punctuation characters.
5. **Hash-Based Attack:** Additionally, the script provides a method for cracking hashed passwords using a brute-force approach with SHA-256 hashing.

### Usage

1. **Installation:**
   - Clone this repository to your local machine.
   - Ensure you have Python installed.

2. **Dependencies:**
   - This script requires `numpy`, which can be installed via pip:
     ```
     pip install numpy
     ```

3. **Execution:**
   - Run the script `password_cracker.py`.
   - Enter the password you want to crack when prompted.

4. **Output:**
   - The script will attempt to crack the provided password using various methods.
   - If successful, it will display the cracked password.
   - If unsuccessful, it will indicate the failure after exhausting all methods.

### Note

- This script is for educational and ethical testing purposes only. Ensure you have proper authorization before attempting to crack passwords.
- Use strong, unique passwords to protect your accounts and systems from unauthorized access.

### Contributors

- **[Your Name]** - *Initial work* - [GitHub Profile](https://github.com/Bulefrg)

### License

