def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count = count_char(text)
    report = get_report(count)
    #print(f"{num_words} words found in the document")
    #print(count)
    #print(report)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_char(text):
    lowerd_text = text.lower()
    count = {}
    for char in lowerd_text:
        count[char] = count.get(char, 0) + 1
    return count

def get_report(data):
    filtered_data = {k: v for k, v in data.items() if k.isalpha()}
    sorted_data = sorted(filtered_data.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_data:
        print(f"The '{char}' character was found {count} times")

    #for count in count.items():
    #    if count.jsalpha() == True
    #        print(f"The '{count[0]}' character was found {count[1]} times")
    #        result = str(f"The '{count[0]}' character was found {count[1]} times")
    #    
    #return result

main()