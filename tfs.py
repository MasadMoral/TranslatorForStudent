import os
from googletrans import Translator

def translate_and_save(text, file_path):
    translator = Translator()
    
    translations = []
    words = text.split(',')
    for i, word in enumerate(words, 1):
        translated_text = translator.translate(word.strip(), dest="bn")  # Target language is always Bengali
        translations.append((i, word.strip(), translated_text.text))
    
    with open(file_path, 'a', encoding='utf-8') as file:
        for index, original, translated in translations:
            file.write(f"{index}. {original} - {translated}\n")
    
    # Print the translations without index numbers
    for index, original, translated in translations:
        print(f"{index}. {original} - {translated}")

def main():
    download_folder = os.path.expanduser("~/Downloads")  # Get the path to the Downloads folder
    file_path = os.path.join(download_folder, "translated_texts.txt")  # Path to the text file in Downloads folder
    
    while True:
        text_to_translate = input("Enter the words or phrases to translate (separated by commas), or type 'exit' to quit: ")
        
        if text_to_translate.lower() == 'exit':
            print("Exiting...")
            break
        
        translate_and_save(text_to_translate, file_path)

if __name__ == "__main__":
    main() 
