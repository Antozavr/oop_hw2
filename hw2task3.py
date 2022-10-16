import os
from operator import itemgetter

text_dict = {}

file_names = ('1.txt', '2.txt', '3.txt')
for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as txt_file:
        txt_file_list = txt_file.readlines()
        str_count = len(txt_file_list)
        work_dict = {file_name: [str_count, txt_file_list]}
        text_dict.update(work_dict)
        sorted_tuple = sorted(text_dict.items(), key=lambda x: x[1])
        dict(sorted_tuple)


with open('final_task.txt', 'w', encoding='utf-8') as file:
    for title, other in sorted_tuple:
        file.writelines(title + '\n')
        i, o = other
        file.writelines(str(i) + '\n')
        for y in o:
            file.writelines(y + '\n')

















