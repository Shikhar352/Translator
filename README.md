# Translator Project

## Overview
The **Translator** project is a multi-language translation tool built using the Facebook NLLB-200 distilled model. It enables seamless translation between various languages, focusing on accuracy and efficiency. The project leverages advanced machine learning techniques and is implemented in Python.

## Features
- Supports multiple languages.
- Utilizes the NLLB-200-distilled-600M model for high-quality translations.
- Easy to extend and integrate into other applications.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Shikhar352/Translator.git
   cd Translator
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Add your text to the `language.json` file.
2. Run the `multi_lang_trans.py` script:
   ```bash
   python multi_lang_trans.py
   ```
3. Translations will be generated based on the input text and saved accordingly.

## Project Structure
- `language.json`: Contains the input text to be translated.
- `multi_lang_trans.py`: Main script for running the translation.
- `models--facebook--nllb-200-distilled-600M/`: Directory containing the model snapshots.

## Contribution
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
- [Facebook NLLB-200 Model](https://github.com/facebookresearch/flores) for providing the backbone for translations.
