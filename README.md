# DictionaryGenerator

**Version**: 1.01  
**Author**: 👨🏾‍💻 
**Status**: Actively Maintained 

## ✨ Features

- 🧠 Generates thousands of unique password combinations
- 🔢 Supports custom base words and numeric patterns
- ⚡ Applies leetspeak transformations (e.g., `a → @, 4, ^, /\, æ`)
- 💫 Adds symbols in strategic positions (prefix, suffix, between segments)
- 🎚️ Adjustable limit on leet combinations per word
- � Clean terminal display with formatted user prompts
- 💾 Output stored in plaintext file for tool integration

## 🛠️ Installation
Run the following commands
```bash
git clone https://github.com/ke-lagat/DictionaryGenerator.git
cd DictionaryGenerator
pip install -r requirements.txt
```
## 🧑‍💻 How to Use

### Interactive Mode
1. Navigate to the project folder in your terminal.
2. Run the script:
    ```bash
    python main.py
    ```
3. Provide the required inputs:
    - **Base words** (comma-separated)
    - **Numeric patterns** (comma-separated)
    - **Output filename** (or press Enter for default `password_dictionary.txt`)
    - **Maximum leet variations per word** (optional)
4. Wait for the script to generate your password dictionary and save it in the specified output file.

## ⚙️ Configuration

The script allows you to configure various options for password generation:
- **Words**: Base words you want to generate variations for.
- **Numbers**: Numbers or number patterns (e.g., `1`, `2`, `3`).
- **Symbols**: The script automatically applies a set of symbols like `!`, `@`, `$`, and others.
- **Max Leet Variations**: Set a maximum number of leet variations per word (default is `10000`).

## 📁 Output

After running the tool, a `.txt` file will be generated with all the generated combinations.

## 📊 Use Cases
✅ Ethical hacking/pentesting exercises

🔓 Password strength analysis

🛡️ Security policy testing

🎓 CTF challenge creation

🔬 Credential stuffing research

## ⚠️ Disclaimer
This tool is intended for legal security research and authorized testing only. Any unauthorized use against systems without explicit permission is strictly prohibited. The developer assumes no liability for misuse.

## 🤖 Contributions

We welcome contributions! If you’d like to improve the tool or fix a bug, feel free to fork the repository and submit a pull request. When contributing, please ensure your changes maintain compatibility with the existing features and adhere to the established coding standards.
##
**Stay safe and secure your passwords!**
