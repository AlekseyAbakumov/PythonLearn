import requests

import comtypes.client

print("Давай те скачаем и выведем среднедушевой доход")
myGod = input("Введите год: ") + " год"
print(myGod)
myMonth = input("Введите месяц: ")

sheet = requests.get("https://www.gks.ru/storage/mediabank/urov_11kv.doc")

shablon_doc = "F:/WORK/Shablon.doc"
shablon_txt = "F:/WORK/Shablon.txt"

with open(shablon_doc, 'wb') as f:
    f.write(sheet.content)

# преобразовываем в стандартный txt
wdFormatEncodedText = 7
input_file = shablon_doc
output_file = shablon_txt

word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(input_file)
doc.SaveAs(output_file, FileFormat=wdFormatEncodedText)
doc.Close()
word.Quit()

with open(shablon_txt, 'r') as f:
    x = f.readlines()

avg_dohod = None
# print(x)

year_flag = 0
month_flag = 0

for i in x:
    if year_flag == 1 and month_flag == 1:
        avg_dohod = i
        break
    if i.strip('\n ') == myGod:
        year_flag = 1
    if year_flag == 1:
        if i.strip('\n') == myMonth:
            month_flag = 1

print(avg_dohod)
