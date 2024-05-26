def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{count_words(file_contents)} words in the document')
    
    l = dict_to_sorted_list(count_letters(file_contents))

    for item in l:
        print(f'The {item[0]} was found {item[1]} times')
    
    print('--- End report ---')

def count_words(text):
    words = text.split()
    return(len(words))

def count_letters(text):
    letter_count = {}

    for ch in text:
        if ch.isalpha() and ch.lower() not in letter_count:
            letter_count[ch.lower()] = 1
        if ch.isalpha() and ch.lower() in letter_count: 
            letter_count[ch.lower()] += 1
    return letter_count

def dict_to_sorted_list(letter_count):
    sorted_dict = sorted(letter_count.items(), key=lambda x:x[1], reverse=True)
    return sorted_dict


main()
