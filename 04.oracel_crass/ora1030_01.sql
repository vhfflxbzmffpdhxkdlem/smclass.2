select sysdate from dual;

select sysdate-30,sysdate,sysdate+30 from dual;

-- employees테이블 hire_date 컬럼
select hire_date,hire_date-1,hire_date+1 from employees;

-- 날짜 범위 검색가능, 정력 order by, asc: 순차정력, dasc:역순정렬
select emp_name,hire_date from employees where hire_date>='020101' and hire_date<='041231' order by hire_date desc;

select emp_name,hire_date from employees where hire_date between '020101' and '041231' order by hire_date desc;


-- like 
select emp_name from employees where emp_name like '___a%';

select emp_name from employees where emp_name like '%a_';

-- 정렬 desc : null값이 제일 위에 검색, asc : 제일 아래
 select department_id from employees order by department_id desc;
 
 -- 월급(salary) 역순정렬
 select emp_name,salary from employees order by salary desc;
 
 -- students테이블에서 total 역순정렬
 select name,total from students order by total desc;
 
 -- hire_date 기준 , 순차정력
 select emp_name,hire_date,salary from employees order by hire_date;
 
select name,kor,eng,math from students order by kor desc, eng desc;

select name,kor,eng,math from students order by kor desc;

-- 한국어도 순차정렬 : ㄱ,ㄴ,ㄷ,... 역순정렬 : ㅎ,ㅍ,ㅌ,...
select name from students order by name desc;

-- 입사일이 빠른 순으로 정렬하는데, 이름은 역숭으로 정렬하시오.
select emp_name,hire_date from employees order by hire_date asc,emp_name desc;


-- abs 절대값
select -10 vel,abs(-10) as abs from dual;

select kor,eng,kor-eng,abs(kor-eng) abs from students order by abs desc;

-- floor 소수점 이하 버림
select 3.141592 ,floor(3.141592) from dual;
-- trunc : 버림,자리수 지정
select 34.5678,trunc(34.5678,2) from dual;
select 34.5678,trunc(34.5678,-1) from dual;

select 3.141592,ceil(34.1592,2) from dual;

-- round 반올림, 자리수 범위지점
-- 소수점 첫째자리
select 34.5678,round(34.5678) from dual;

-- 소수점 둘째자리까지 출력, 셋째자리에서 반올림 됨.
select 34.5678,round(34.5678,2) from dual;

-- 양수 첫째자리에서 반올림, 소수점 자리수에서 앞쪽으로 한칸위치 반올림.
select 35.5678,round(35.5678,-1) from dual;

-- mod : 나머지
select 24/2,mod(27,2) from dual;
select 30/3,mod(31,7) from dual;

-- 사원번호가 홀수 인 사원을 출력하시오.
select employee_id,emp_name from employees where mod(employee_id,2)=1 order by employee_id;

select * from employees;
-- 최종연봉 : 월급*12+(월급*12)*커미션, 소수점 2자리에서 반올림. 첫째자리로 만드시오.
select salary,round(salary*12+((salary*12)*nvl(commission_pct,0))*1381.86795,1) ysalary from employees;

select * from students;

-- 시퀀스 : 자동으로 번호부여
create sequence stu_seq
start with 1
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache;

-- 시퀀스에서 번호생성
select stu_seq.nextval from dual;

select stu_seq.currval from dual;

-- 게시판 테이블 생성
create table board(
bno number(4),
btitle varchar2(100),
bcontent varchar2(4000),
id varchar2(30),
bhit number(10),
bdate date
);

insert into board values(
1,'제목입니다.','내용입니다.','aaa',1,sysdate
);
insert into board values(
2,'제목입니다.2','내용입니다.2','aaa',1,sysdate
);

insert into board values(
stu_seq.nextval,'제목입니다.2','내용입니다.2','aaa',1,sysdate
);

select * from board;
commit;

creat seqyebce board_seq
start with 129  --시작번호
increment by 1  -- 증감숫자
minvalue 1      -- 최소값
maxvalue 9999   -- 최대값
nocycle         -- 1~9999이상이 되면,다시 1
nocache;        -- 메모리에 시퀀스값 미리할당

insert into board values(
board_seq.nextval,'제목14','내용14','aaa',1,sysdate
);

update board set btitle='제목을 다시 변경' where bno=14;
commit;

drop table board;

create table board(
bno number(4),
btitle varchar2(100),
bcontent clob,  -- 대용량 글자타입
id varchar2(30), 
bgroup number(4), -- 답변당기 경우 수서정의
bstep number(4),  -- 답변달기 드려쓰기
bindent number(4), -- 조회수
bhit number(10),-- 등록일
bdate date
);

select board_seq.currval from dual;

insert into board values(
board_seq.nextval,'제목1','내용1','aaa',board_seq.currval,0,0,1,sysdate
);
select * from board;

-- 시퀀스 생성
-- students_seq.nextval
-- students 테이블 100->101
-- 101.'홍길순',100,99,90,total,avg,rank,날짜
-- 1명을 일력하세요

create sequence students_seq
start with 101
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache;


insert into students values(
students_seq.nextval,'홍길순',100,99,90,(100+99+90),(100+99+90)/3,0,sysdate
);

select * from students;
commit;

select no,name,kor,eng,math,total,round(avg,2),rank,sdate from students;

select *,round(avg,2) from students;

select s.*,round(avg,2) from students s;

select dept_seq.nextval from dual;

-- s_seq
-- 시작 1, 증분 1, 최대값 99999

create sequence s_seq
star with 1
increment by 1
minvalue 1
maxvalue 99999
nocache
nocycle;

-- 시퀀스 생성, nextval : 다음 시퀀스번호 생성. currval : 현재시퀀스 번호 보여줌
select s_seq.nextval from dual;

select emp_seq.nextval from dual;
select emp_seq.currval form dual;

-- 타입
-- 문자형,숫자형,날짜형
-- char,varchar2,nchar,nvarchar2,long,clob
-- char,varchar2 : 한국문자 입력시 3byte사용
-- varchar2(6) : 한글 2글자 입력
-- nvarchar2(5) : 한글 입력 5자리까지 입력가능

-- number
-- date,timestamp


































































































































































