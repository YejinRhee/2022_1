#1 Eng:Kor Dictionary
Eng = open('Day21_Eng','rt')
Kor = open('Day21_Kor','rt', encoding="UTF-8")
Dictionary = {}

while True :
    voca = Eng.readline().lower().strip()
    meaning = Kor.readline().strip()
    if not voca :
        break
    Dictionary[voca] = meaning
Eng.close()
Kor.close()
print(Dictionary.items())

#2 test & answer output
import random
import pandas as pd
import openpyxl
Eng_Kor_list = list(Dictionary.items())
random.shuffle(Eng_Kor_list)

Eng_Kor = pd.DataFrame(data=Eng_Kor_list, columns=['Voca','Meaning'])
Eng_Kor.index = Eng_Kor.index + 1
Eng_Only = Eng_Kor['Voca']
Eng_Only.index = Eng_Only.index + 1
with pd.ExcelWriter('Test_Answer.xlsx') as writer:
    Eng_Only.to_excel(writer, sheet_name='Test')
    Eng_Kor.to_excel(writer, sheet_name='Answer')




