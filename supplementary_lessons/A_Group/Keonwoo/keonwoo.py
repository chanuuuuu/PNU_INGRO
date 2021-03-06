RFP 기능을 수행하는 함수들을 나열해 보았다.
Insert Select Delete Update를 수행할 수 있는 함수들을 만들어 보았고 그 것들을 Database(MariaDB)
와 연동하기 쉽게 기능을 구현할 수 있는 틀을 제작하였다.

1.조회함수 : sql query연동을 통해 데이터 베이스들의 모든 쿼리들을 표시해준다
2.수정함수 : 수정받을 인자들을 입력받아서 sql query문을 통해 데이터 베이스에 수정함과 동시에 입력 콘솔에 또한 수정된 사항들을 표시한다
3.삭제함수 : 삭제할 인자들을 입력 받으면 데이터 베이스의 그 해당 고객 데이터 파일 행을 모두 drop시킨다 , 인자로 primary키에 입력된 이름을 사용한다
4.입력함수 : input 함수를 사용하여서 콘솔창에  이름, 나이 , 성별,생일을 입력 받으면 데이터베이스에 저장하는것을 목표로한다.
  
앞으로 해나갈 사항
==========================
전체적인 틀을 수행할 수 있는 메인함수 (if __name__== '__main__')에 구현할 부분을 전체적으로
만들어 낼 것이다.

메인함수에서 전체적인 순서절차

특히 P와 N으로 페이지를 넘길 수 있는 부분을 함수로 고려할 것이다.

먼저 떠오른 생각은 global variable로 Page 변수를 생성한 뒤

함수에서 그 page변수를 필요할때마다 호출해서 앞으로 당기고 밀수있도록 함수를 조정할 것이다.
일단여기까지가 1차 목표이다 

