def get_text(path):
    with open(f"{path}") as file:
        content = file.read()
    return content

def word_count(text):
    words = text.split()
    return len(words)

def char_occurences(text):
    # text_set = set(text.lower())
    char_count_dict = {}
    # for char in text_set:
    #     char_count_dict[char] = text.lower().count(char)
    # return char_count_dict
    for char in text.lower():
        if char in char_count_dict.keys():
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

def output_data(word_count, char_count, path):
    output = ""
    output += f"--- Begin report of {path} ---"
    output += f"{word_count} words found in the document\n\n"
    for char in char_count:
        if char.isalpha():
            output += f"The '{char}' character was found {char_count[char]} times\n"
    output += "--- End report ---"

    return output


def main():
    path = "./books/frankenstein.txt"
    contents = get_text(path)
    count_of_words = word_count(contents)
    char_counts = char_occurences(contents)
    book_analysis = output_data(count_of_words, char_counts, path)
    print(book_analysis)

main()