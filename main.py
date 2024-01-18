def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        letters = []
        for word in words:
            for letter in word:
                letters.append(letter.lower())
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        letters_count ={}
        for character in alphabet:
            letters_count[character] = letters.count(character)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document")
        for key in letters_count:
            print(f"The '{key}' character was found {letters_count[key]} times")

main()