from frequency import freq_analysys
with open('freq_examples.txt', 'a') as out_file:
    string_1 = freq_analysys('examples_of_texts/War_and_community.txt')
    string_2 = freq_analysys('examples_of_texts/We.txt')
    string_3 = freq_analysys('examples_of_texts/Wikipedia_artical.txt')
    out_data = f'{string_1}\n{string_2}\n{string_3}'
    out_file.write(out_data)
