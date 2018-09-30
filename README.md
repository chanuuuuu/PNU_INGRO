# PNU_INGRO
## 고객 정보 관리 시스템 RFP

## 1. 주요 내용
지금 까지 배운 내용을 토대로 고객의 정보를 관리하는 프로그램을 만듭니다.
고객의 정보를 관리하는 프로그램에서 사용하는 고객 정보를 저장하는 자료구조는 자신 있는 것을 이용합니다.

## 2. 요구사항 - 데이타
고객의 정보는 _이름_, _성별_, _이메일_, _출생년도_가 있습니다. 
고객의 정보를 입력받아 본인이 선택한 자료구조에 저장해야  합니다.  
이름은  문자열로  저장하며, 
성별은  남자는  M,  여자는 F로 저장합니다.
이메일은 문자열로 저장하며, 태어난 연도는 정수로 저장합니다.

## 2. 요구사항 - 기능
고객 관리 프로그램은 고객의 정보를 _저장_, _조회_, _수정_, _삭제_할 수 있는 
기능이  있어야 합니다. 
고객 정보를 파일에 저장하는 기능을 구현하지 않아도 됩니다.
“I”를 눌러 고객의 정보를 입력받도록 하며, 저장된 고객 정보는 “P” 또는 “N”을 눌러 
이전 고객정보 또는 다음 고객정보를 조회할 수 있어야  합니다.  
조회한 고객 정보는 “U”를 눌러 새로운 정보로 수정할 수  있어야  합니다. 
“D”를 누르면 조회한 고객 정보를 삭제해야 합니다. 프로그램의 종료는 “Q”를 누릅니다.

* 객체지향 개념을 적용하여 확장성을 고려한 애플리케이션이 되도록 해야 합니다.
