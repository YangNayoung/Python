#전화번호부 검색
# 전화번호부 생성
tel1 = {"이름":"일미림", "전화번호":"010-1111-2222"}
tel2 = {"이름":"이미림", "전화번호":"010-2222-3333"}
phonebooks = []
phonebooks.append(tel1)
phonebooks.append(tel2)
print(phonebooks)
# 이름 입력
input_name = input("찾을 이름을 입력하세요. : ")
# 전화번호부 출력
count = 0
for phonebook in phonebooks:
    # if input_name == phonebook["이름"]:
    if input_name in phonebook["이름"]: #이름의 일부로 찾는다.
        print("{}님의 전화번호는 {} 입니다.".format(phonebook["이름"], phonebook["전화번호"]))
        count += 1
    
if count == 0:
    print("{}님의 전화번호는 없습니다.".format(input_name))
