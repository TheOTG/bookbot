from stats import countWords, countChar
import sys

def sort_on(dict):
    return dict["num"]

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        word_count = countWords(file_contents)
        char_dict = countChar(file_contents)
        char_list = []

        for char in char_dict:
            char_list.append({
                "char": char,
                "num": char_dict[char]
            })
        
        char_list.sort(reverse = True, key=sort_on)

        print(f"--- Begin report of {sys.argv[1]} ---")
        print(f"{word_count} words found in the document")
        print("")

        for char in char_list:
            if char["char"].isalpha():
                print(f"'{char["char"]}: {char["num"]}'")

        print("--- End report ---")

main()