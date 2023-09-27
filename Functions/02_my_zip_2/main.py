def my_zip(b_string, b_list, num):
    if num == min(len(b_string), len(b_list)):
        return 1
    main_list = [b_string[num], b_list[num]]
    print(tuple(main_list))
    return my_zip(b_string, b_list, num + 1)


# a_string = 'abcd'
# a_list = [10, 20, 30, 40]
# count = 0
#
# my_zip(a_string, a_list, count)
