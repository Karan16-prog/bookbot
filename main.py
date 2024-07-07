def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    word_count = get_book_word_count(text)
    char_count_dict = get_book_char_count(text)

    generate_book_report(char_count_dict, word_count, book_path)    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_word_count(text):
    return len(text.split())

def get_book_char_count(text):
    char_dict = {}
    for char in text:
        if char.isalpha():
            if char.lower() in char_dict:
                char_dict[char.lower()] += 1
            else:
                char_dict[char.lower()] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def generate_book_report(char_dict, total_count, path):
    char_dict_list = []
    
    for char in char_dict:
        char_dict_list.append({
            "char": char,
            "count": char_dict[char]
        })
    
    char_dict_list.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {path} ---")
    print(f"{total_count} words found in the document\n")
    for item in char_dict_list:
        print(f"The '{item["char"]}' character was found {item["count"]} times")

    print("--- End report ---")
main()