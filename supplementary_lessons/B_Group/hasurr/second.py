"""
고객 정보 관리 시스템 RFP

주요 내용 지금 까지 배운 내용을 토대로 고객의 정보를 관리하는 프로그램을 만듭니다.
고객의 정보를 관리하는 프로그램에서 사용하는 고객 정보를 저장하는 자료구조는 자신 있는 것을 이용합니다.

요구사항 -
데이타 고객의 정보는 이름, 성별, 이메일, 출생년도가 있습니다.
고객의 정보를 입력받아 본인이 선택한 자료구조에 저장해야 합니다.
이름은 문자열로 저장하며, 성별은 남자는 M, 여자는 F로 저장합니다.
이메일은 문자열로 저장하며, 태어난 연도는 정수로 저장합니다.

요구사항 -
기능 고객 관리 프로그램은 고객의 정보를 저장, 조회, 수정, 삭제할 수 있는 기능이 있어야 합니다.
고객 정보를 파일에 저장하는 기능을 구현하지 않아도 됩니다.
“I”를 눌러 고객의 정보를 입력받도록 하며,
저장된 고객 정보는 “P” 또는 “N”을 눌러 이전 고객정보 또는 다음 고객정보를 조회할 수 있어야 합니다.
조회한 고객 정보는 “U”를 눌러 새로운 정보로 수정할 수 있어야 합니다.
“D”를 누르면 조회한 고객 정보를 삭제해야 합니다. 프로그램의 종료는 “Q”를 누릅니다.

객체지향 개념을 적용하여 확장성을 고려한 애플리케이션이 되도록 해야 합니다.
"""
import re

list_customer_information = []
index_costomer_list = 0
asd = []

def insert_inform():
    validation = False
    print('=====고객 정보 입력=====')
    # while validation != True:
    name = input("이름 : ")
        # if not re.match(r'[a-zA-Zㄱ-ㅎ]', name):
        #     print("올바른 이름입력이 아닙니다. 다시 시도해주세요")
        # else:
        #     vlaidation = True

    validation = False
    while validation != True:
        gender = input('성별 (M 또는 F)) : ')
        if gender.upper() == 'M' or gender.upper() == 'F':
            validation = True
        else:
            print("올바른 성별입력이 아닙니다. 다시 시도해주세요")

    validation = False
    while validation != True:
        email = input('이메일 (형식 : a@a.com) : ')
        if len(email) > 6:
            if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                print("올바른 이메일이 아닙니다. 다시 시도해주세요")
            else:
                validation = True
    
    validation = False
    while validation != True:
        birth = input('생년월일(ex. 940915) :')
        if len(birth) == 6:
            if not re.match(r"[0-9]", birth):
                print('올바른 생년월일이 아닙니다.') # 아닌경우
            else:
                validation = True # 맞는경우
    return name, gender, email, birth

def insert_inform_to_dict(name, gender, email, birth):
    global list_customer_information
    customer_information['name'] = name
    customer_information['gender'] = gender
    customer_information['email'] = email
    customer_information['birth'] = birth
    list_customer_information.append(customer_information)
    return customer_information

def get_inform(index_list = 0):
    global list_customer_information
    global index_costomer_list

    print('=====고객 정보 조회=====')
    print('이름    : ',list_customer_information[index_list]['name'])
    print('성별    : ',list_customer_information[index_list]['gender'])
    print('이메일  : ',list_customer_information[index_list]['email'])
    print('출생년도: ',list_customer_information[index_list]['birth'])
    while True:
        print('P : 다음 고객 정보\n','N : 이전 고객 정보\n', 'U : 정보 수정')
        u_i = input('입력 : ')
        user_input = u_i.upper()
        if user_input == 'P' or user_input == 'N' or user_input == 'U':
            return user_input
            break
        else:
            print('입력이 틀렸습니다. 다시입력해 주세요.')
    


def adjust_inform():
    print('=====고객 정보 수정=====')


while True:
    print('='*50)
    print('고객관리 프로그램입니다.')
    print('='*50)
    print("고객의 정보는 이름, 성별, 이메일, 출생년도를 저장합니다.")
    print("할 일을 선택하십시오.(종료를 원한다면 0)")
    print("""
    1. 고객정보입력 
    2. 고객정보조회
    3. 고객정보수정
    4. 고객정보삭제
                """)
    customer_information = {'name':'', 'gender':'M', 'email':'a@a.com', 'birth':'940915'}    # 딕셔너리 초기화     
    select = input("입력 : ")
    if select == '0':
        break
    if select == "1":
        name, gender, email, birth = insert_inform()
        insert_inform_to_dict(name, gender, email, birth)
        print(list_customer_information)
        print('입력되었습니다.')

    elif select == '2':
        next_step = get_inform()
        while True:    
            if next_step == 'P':
                index_costomer_list += 1
                if list_customer_information[index_costomer_list] == False:
                    print("마지막 고객정보 입니다.")
                else:
                    next_step = get_inform(index_costomer_list) # 다음 조회

            elif next_step == 'N':
                index_costomer_list -= 1

                if index_costomer_list < 0:
                    print("처음 고객 정보입니다.")
                
                else:
                    next_step = get_inform(index_costomer_list) # 이전 조회

            elif next_step == 'U':
                print('수정할 고객 정보를 입력하세요 :')
                name, gender, email, birth = insert_inform()
                list_customer_information[index_costomer_list] = insert_inform_to_dict(name, gender, email, birth)
                print("수정된 고객의 정보입니다. :")
                print(list_customer_information[index_costomer_list])
            break
    
    elif select =='3':
            adjust_inform()

