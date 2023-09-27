first_tour_file = open('first_tour.txt', 'r')

second_tour_list = []
count = 0

for index, i_line in enumerate(first_tour_file):
    if index == 0:
        main_points = int(i_line)
    else:
        string_list = i_line.split()
        if int(string_list[2]) > main_points:
            second_tour_list.append(string_list)

res_list = sorted(second_tour_list, key=lambda x: x[2], reverse=True)

len_of_res_list = 0
for i_len in res_list:
    len_of_res_list += 1

first_tour_file.close()

second_tour_file = open('second_tour.txt', 'a')
second_tour_file.write(str(len_of_res_list) + '\n')
for i_list in res_list:
    i_list[0], i_list[1], i_list[2] = i_list[1], i_list[0], i_list[2]
    res_str = ''
    for i_index, i_data in enumerate(i_list):
        if i_index == 0:
            count += 1
            res_str = '{}) {}.'.format(count, i_data[0])
        elif i_index == 1:
            res_str += ' {}'.format(i_data)
        else:
            res_str += ' {}'.format(i_data) + '\n'
    second_tour_file.write(res_str)

second_tour_file.close()