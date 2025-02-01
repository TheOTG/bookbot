def sort_on(dict):
    return dict["num"]

def countWords(text):
    return len(text.split())

def countChar(text):
    char_dict = {}
    for char in text:
        if char.lower() not in char_dict:
            char_dict[char.lower()] = 1
        else:
            char_dict[char.lower()] += 1
    return char_dict

def main():
    with open("books/frankenstein.txt") as f:
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

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print("")

        for char in char_list:
            if char["char"].isalpha():
                print(f"The '{char["char"]}' character was found {char["num"]} times")

        print("--- End report ---")

main()