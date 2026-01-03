def get_num_words(text): 
    num_words = len(text.split())
    return num_words

def get_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def get_report_list(dict):
    new_list = []
    for key, value in dict.items():
        if key.isalpha() == False:
            pass
        else:
            new_dict = {'char': key, 'num': value}
            new_list.append(new_dict)
    def sort_on(items):
        return items["num"]
    new_list.sort(reverse=True, key=sort_on)
    return new_list 