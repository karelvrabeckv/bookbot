def main():
    path = "books/frankenstein.txt"
    text = get_file_text(path)

    num_of_words = get_num_of_words(text)
    letters = count_letters(text)
    sorted_letters = sort_letters(letters)
    
    print(f"--- Begin report of {path} ---")
    print(f"{num_of_words} words found in the document")
    print("")

    for letter in sorted_letters:
        print(f"The '{letter["name"]}' character was found {letter["count"]} times")

    print("--- End report ---")

def get_file_text(path: str):
    with open(path) as f:
        return f.read()

def get_num_of_words(text: str):
    words = text.split()
    return len(words)

def count_letters(text: str):
    text = text.lower()

    letters = {}
    for letter in text:
        if not letter.isalpha():
            continue

        if letter in letters.keys():
            letters[letter] += 1
        else:
            letters[letter] = 1

    return letters

def sort_letters(letters: dict):
    sorted_letters = []

    for letter in letters:
        sorted_letters.append({ "name": letter, "count": letters[letter] })

    sorted_letters.sort(reverse=True, key=sort_on)

    return sorted_letters

def sort_on(dict: dict):
    return dict["count"]

main()
