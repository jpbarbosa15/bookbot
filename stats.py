def word_count(book_content):
    text = book_content.split()
    return len(text)

def count_unique_character(book_content):
    chars = {}
    words = book_content.lower().split()
    for word in words:
        for ch in word:
            if ch in chars:
                chars[ch] += 1
            else:
                chars[ch] = 1
    
    return chars

def sort_on(items):
    return items["num"]

def sort_dicts(dict):
    sorted_list = []
    for key in dict:
        sorted_list.append({"char": key, "num": dict[key]})

    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list