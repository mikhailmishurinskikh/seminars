def freq_analysys(text_file):
    with open(text_file, 'r') as in_file:
        text = in_file.read()
        text = list(text)
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    letters_nums = dict(zip(list(letters), [0 for i in range(33)]))

    for i in text:
        if i in letters:
            letters_nums[i] += 1
        elif i in letters.upper():
            letters_nums[i.lower()] += 1
    letters_nums = {x: y for x, y in sorted(letters_nums.items(), key = lambda x: x[1], reverse=1)} 
    return ''.join(letters_nums.keys())
