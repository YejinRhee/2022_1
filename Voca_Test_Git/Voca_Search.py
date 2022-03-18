#3 단어 입력시 뜻 보여주는 기능
Eng = open('Day21_Eng','rt')
Kor = open('Day21_Kor','rt', encoding="UTF-8")
Dictionary = {}

while True :
    voca = Eng.readline().lower()
    meaning = Kor.readline()
    if not voca :
        break
    Dictionary[voca] = meaning
Eng.close()
Kor.close()

which_voca = input()
which_voca += ' \n'
print(Dictionary[which_voca])

