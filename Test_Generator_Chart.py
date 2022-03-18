#1 Eng:Kor 사전 만들기
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

#2 test & answer 만들기
import random
import pandas as pd
import openpyxl
Eng_Kor_list = list(Dictionary.items())
random.shuffle(Eng_Kor_list)
Eng = []
for i in range(len(Eng_Kor_list)):
    Eng.append(Eng_Kor_list[i][0])

# 이건 그냥 txt file로 만들었던 첫번재 버전
# test = open('test','wt')
# answer = open('answer','wt')
# test.write(EngOnly)
# answer.write(Eng_Kor)

# 이건 DataFrame으로 만든 두번째
EngOnly = pd.DataFrame(data=Eng, columns=['Voca'])
EngOnly.index = EngOnly.index + 1
Eng_Kor = pd.DataFrame(data=Eng_Kor_list, columns=['Voca','Meaning'])
Eng_Kor.index = Eng_Kor.index + 1
with pd.ExcelWriter('Test_Answer.xlsx') as writer:
    EngOnly.to_excel(writer, sheet_name='Test')
    Eng_Kor.to_excel(writer, sheet_name='Answer')

# 이건 각 아웃풋을 다른 엑셀 파일로 저장
# EngOnly.to_excel('C:/Users/Yejin/PycharmProjects/pythonProject/VocaTest/Test.xlsx')
# Eng_Kor.to_excel('C:/Users/Yejin/PycharmProjects/pythonProject/VocaTest/Answer.xlsx')

print(EngOnly.head())
print(Eng_Kor.head())
# test.close()
# answer.close()




