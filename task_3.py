import glob
import os


def get_file_paths():
    files_path = os.getcwd() + '/sorted/'
    file_paths = glob.glob(files_path + '*.txt')
    return file_paths


def read_write_result():
    file_paths = get_file_paths()
    file_lst = []
    for file in file_paths:
        file_name = file.split('\\')[-1]
        with open(file, encoding='utf-8') as f:
            read_line = f.readlines()
            file_lst.append([len(read_line), file_name, read_line])
    file_lst.sort()
    with open("task_3_res.txt", "w", encoding='utf-8') as result_f:
        for res_file in file_lst:
            result_f.write(f"{res_file[0]}\n{res_file[1]}\n{''.join(res_file[2])}\n")
    return file_lst


print(read_write_result())









