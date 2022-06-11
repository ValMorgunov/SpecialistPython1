# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/
l = text.count(" ")
count = 0
crop_text = text
# TODO: your code here
while l > 0:
    l -= 1
    index = crop_text.index(" ")
    if index>5:
        count+=1
    crop_text=crop_text[index+1:]
print(count)
