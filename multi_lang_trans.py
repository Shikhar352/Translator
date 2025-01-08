import torch
import gradio as gr
import json
from transformers import pipeline

# Load model
model_path = r"D:\Gen_AI project\Translator\models--facebook--nllb-200-distilled-600M\snapshots\f8d333a098d19b4fd9a8b18f94170487ad3f821d"
text_translator = pipeline(task="translation", model=model_path, torch_dtype=torch.bfloat16)

# Load language data
try:
    with open('language.json', 'r') as file:
        language_data = json.load(file)
        print(language_data)  # Debugging: Inspect JSON structure
except (FileNotFoundError, json.JSONDecodeError) as e:
    language_data = []
    print(f"Error loading language.json: {e}")

def get_FLORES_code_from_language(language):
    for entry in language_data:
        if entry.get('Language', '').lower() == language.lower():
            return entry.get('FLORES-200 code')  # Safely get the value
    return None

def translate_text(text, destination_language):
    dest_code = get_FLORES_code_from_language(destination_language)
    if not dest_code:
        return "Destination language not supported or FLORES code not found."
    translation = text_translator(text, src_lang="eng_Latn", tgt_lang=dest_code)
    return translation[0]["translation_text"]

# Dynamic dropdown
language_choices = [entry.get('Language') for entry in language_data if 'Language' in entry]

# Gradio Interface
gr.close_all()
demo = gr.Interface(
    fn=translate_text,
    inputs=[gr.Textbox(label="Input text to translate", lines=6), gr.Dropdown(language_choices, label="Select Destination Language")],
    outputs=[gr.Textbox(label="Translated text", lines=4)],
    title="Multi-Language Translator",
    description="This application will translate English text into multiple languages."
)
demo.launch(share=True)
