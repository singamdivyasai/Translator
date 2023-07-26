from translate import Translator

def select_lang():
    print('''Available Languages:
    as: Assamese
    bn: Bengali
    gu: Gujarati
    hi: Hindi
    kn: Kannada
    ml: Malayalam
    mr: Marathi
    ne: Nepali
    or: Oriya
    pa: Punjabi
    ta: Tamil
    te: Telugu
    ur: Urdu
    en: English
    ------------------
    ar: Arabic
    de: German
    es: Spanish
    fr: French
    it: Italian
    ja: Japanese
    ko: Korean
    pt: Portuguese
    ru: Russian
    zh-CN: Chinese (Simplified)''')

def translate_text(text, src_lang, dest_lang):
    translator = Translator(from_lang=src_lang, to_lang=dest_lang)
    try:
        translated_text = translator.translate(text)
        return translated_text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    select_lang()
    source_language = input("Enter the source language code: ")
    destination_language = input("Enter the destination language code: ")
    text_to_translate = input("Enter the text to translate: ")

    translated_text = translate_text(text_to_translate, source_language, destination_language)
    print(f"Translated Text: {translated_text}")
