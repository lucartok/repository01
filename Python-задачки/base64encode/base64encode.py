import base64

file_path = "test_dict.txt"
base64_file_path = file_path + '_b64'

with open(file_path, 'r') as f:
    for s_line in f:
        s_line = s_line[:-1]  # отрезаем символ переноса строки
        b_line = s_line.encode("utf-8")  # получаем строку байт
        e_line = base64.b64encode(b_line)  # кодируем в base64
        with open(base64_file_path, 'a') as f_out:
            f_out.write(e_line.decode('utf-8'))
            f_out.write('\n')
