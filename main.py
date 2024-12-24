with open("books/frankenstein.txt") as f:
        file_contents = f.read()

def word_count(book):
    count = 0
    words = file_contents.split()
    for word in words:
            if word == word:
                   count += 1
    return count

def char_count(book):
    chars = {}
    for c in book:
        lowered = c.lower()
        if lowered.isalpha():
            chars[lowered] = chars.get(lowered, 0) + 1
    report = []
    for char, count in chars.items():
        report.append([char, count])
    return report


    

def main():
    show_words = word_count(file_contents)
    tuples_list = char_count(file_contents)
    print(f"--- Begin Report of {f} ---")
    print(f"{show_words} Words found in document")
    for item in tuples_list:
         value1, value2 = item
         print(f"The {value1} character was found {value2} times")
         

main()
