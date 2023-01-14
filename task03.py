# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def OpenForRead(path):
    data = open(path, 'r', encoding='utf-8')
    txt = data.read()
    data.close()
    return txt


def EncodingRLE(txt):
    count = 1
    rle_data = []

    for i in range(0, len(txt) - 1):
        if (txt[i] != txt[i + 1]) :
            rle_data.append(count)
            rle_data.append(txt[i])
            count = 1
        else:
            count += 1

    rle_data.append(count) 
    rle_data.append(txt[-1])      
    result = ''.join(str(i) for i in rle_data)
    return result


def OpenForWrite(path, text):
    with open(path, 'w', encoding='utf-8') as file:
        file.writelines(text)


def DecodingRLE(text):
    result = ''
    for i in range(len(text) - 1):
        if not text[i].isalpha() and text[i] != ' ' and text[i] != '\n':
            result += int(text[i])*text[i+1]
    return result


print()
for_rle = OpenForRead('for_encoding.txt')
print(f'Входные данные, которые мы берем для кодировки из файла "for_encoding.txt" : \n{for_rle}')
print()

rle_txt = EncodingRLE(for_rle)
print(f'Исходный текст, после применения кодировки : \n{rle_txt}')
print('Записываем его в отдельный файл "RLE_txt.txt"')
OpenForWrite('RLE_txt.txt', rle_txt)
print()

decoding_txt = DecodingRLE(rle_txt)
print(f'И расшифровываем RLE - кодировку : \n{decoding_txt}')
print('Записываем его в отдельный файл "after_decoding.txt"')
OpenForWrite('after_decoding.txt', decoding_txt)
