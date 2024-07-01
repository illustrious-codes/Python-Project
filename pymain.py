from google.cloud import translate_v2 as translate
from google.api_core.exceptions import BadRequest

def translate_text(text, target_language):
    try:
        translate_client = translate.Client()

        result = translate_client.translate(text, target_language=target_language)

        return result['translatedText']

    except BadRequest as e:
        print(f"Bad request error: {e.message}")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    print("Welcome to Text Translator using Google Cloud Translation API!")
    while True:
        try:
            text = input("Enter the text to translate: ")
            target_language = input("Enter the target language code (e.g., 'es' for Spanish, 'fr' for French): ")

            translated_text = translate_text(text, target_language)
            if translated_text:
                print(f"Translated text: {translated_text}")
            else:
                print("Translation failed. Please check your input.")

        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        choice = input("\nDo you want to perform another translation? (yes/no): ").lower()
        if choice != 'yes':
            break

    print("Thank you for using the Text Translator!")

if __name__ == "__main__":
    main()
