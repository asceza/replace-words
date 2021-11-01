import sys

file_name = sys.argv[1]
original_word = sys.argv[2]

alternative_words_list_list = sys.argv[2::]
# формирует список (срез) из аргументов командной строки начиная с третьего и до конца с шагом 1

i = 0 # порядковый номер слова в списке
new_text_list = []

# print(f"{file_name} - название файла\n{original_word} - слово на замену\n{alternative_words_list} - альтернативные слова")

with open(file_name, "r") as f:
    word_list = f.read().split(' ')
    # формируем список из всех слов из файла, так как разделителем выступает пробел
    # знаки препинания включены в слова

for word in word_list:
    if (original_word in word) or (original_word.capitalize() in word):
        # если слово есть в списке, или слово с заглавной буквы есть в списке
        if original_word.capitalize() in word:
            word = word.replace(original_word.capitalize(), alternative_words_list_list[i].capitalize)
            # слово с заглавной буквы меняем на слово из списка с заглавной буквы
        else:
            word = word.replace(original_word, alternative_words_list_list[i])
            # заменяем слова без заглавной буквы
        i +=1
        if i>len(alternative_words_list_list)-1:
            i=0
    new_text_list.append(word) # добавляем к списку все слова из файла, в т.ч. и замененные

output_file_name = file_name[0:-4] + '_output' + file_name[-4::]
with open(output_file_name, "w") as f:
    f.write(" ".join(new_text_list))
    # соединяем все слова из списка с пробелом и пишем в файл
    # любой итерируемый объект может быть объединен

print(f"Файл {output_file_name} создан")
