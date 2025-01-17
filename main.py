def main():
    text_path = "books/frankenstein.txt"
    text = get_text(text_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    make_report(text_path, word_count, character_count)

def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)
    
def count_characters(text):
    characters = {}
    lower_text = text.lower()
    for c in lower_text:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def make_report(path, total_words, character_dict):
    print(f"----- Report on {path} -----")
    print(f"The book contains {total_words} words in this document.")
    print("\n")
    sorted_chars = sorted(character_dict.items(), key=lambda x: x[1], reverse=True)
    for c in sorted_chars:
        if c[0].isalpha() == True:
            print(f"The '{c[0]}' character appears {c[1]} times.")
    print("----- End of Report -----")
    
main()