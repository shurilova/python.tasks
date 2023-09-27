def frequency(string):
    sym_dict = dict()
    count = 0
    for sym in string:
        if sym.isalpha():
            count += 1
            if sym in sym_dict:
                sym_dict[sym] += 1
            else:
                sym_dict[sym] = 1
    return sym_dict, count


text_file = open('text.txt', 'r')
data = text_file.read().lower()
frequency_dict, number_of_letters = frequency(data)
text_file.close()

for i_letter, i_number in frequency_dict.items():
    frequency_dict[i_letter] = round(i_number/number_of_letters, 3)

sorted_tuple = sorted(frequency_dict.items(), key=lambda x: (-x[1], x[0]), reverse=False)
res_list = dict(sorted_tuple)

analysis_file = open('analysis.txt', 'a')
for i_sym, i_frequency in res_list.items():
    analysis_file.write(i_sym + ' ')
    analysis_file.write(str(i_frequency) + '\n')
analysis_file.close()