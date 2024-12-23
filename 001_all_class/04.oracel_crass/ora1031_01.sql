select *from member;

update member set id='fff',pw='1111',name='정약용' where id ='Towell';

commit;

select sysdate-1,sysdate,sysdate+1 from dual;

select hire_date,round(hire_date,'Month') from employees;

select hire_date,trunc(hire_date,'month') from employees;

select add_months(trunc(sysdate,'month'),1) from dual;

-- vip요금제로 변경을 하면 다음달 1일부터 혜택

select sysdate,add_months(trunc(sysdate,'month'),1) 다음달 from dual;

-- 입사일 기준 다음달 1일부터 혜택을 주겠다고함.
-- 입사일 다음달 1일 출력하시오.
select hire_date,add_months(trunc(hire_date,'month'),1) 다음달 from employees;

-- 입사일 기준 1년 후 날짜를 출력하시오.
select hire_date,add_months(hire_date,12) from employees;

-- 입사일 기준 1년 후 날짜와 1년후 그달의 마지막 날짜를 출력하시오.
select hire_date,last_day(hire_date) from employees;
select hire_date,add_months(hire_date,12),last_day(add_months(hire_date,12)) from employees;

-- 입력일 기준 1년후 마지막 날짜가 08/31,09/30,10/31인 학생들을 모두 출력하시오.
select sdate from students;
select last_day(add_months(sdate,12)) y from students;

select last_day(add_months(sdate,12)) from students where last_day(add_months(sdate,12)) in ('24/08/31','25/08/31','24/09/30','25/09/30','24/10/31','25/10/31') order by last_day(add_months(sdate,12)) ;

-- extract함수 : 년,월,일,시,분,초 만 분리해서 가져오는 함수
-- sysdate 년,월,일
select sysdate from dual;
select extract(year from sysdate) from dual;
select extract(month from sysdate) from dual;
select extract(day from sysdate) from dual;

-- systimestanp 년,월,일,시,분,초
select systimestamp from dual;
select extract(year from systimestamp) from dual;
select extract(month from systimestamp) from dual;
select extract(day from systimestamp) from dual;
select extract(hour from systimestamp) from dual;
select extract(minute from systimestamp) from dual;
select extract(second from systimestamp) from dual;

select sdate,extract(month from sdate),extract(year from last_day(sdate+365)) from students
where extract(year from last_day(sdate+365))=2025 and extract(month from last_day(sdate+365)) in (8,11,12);

-- substr함수 : 문자에서 시작위치. 가져올 개수
select substr(sysdate,4,2) from dual;

select sdate,substr(last_day(sdate+365),4,2) sdate2 from students where substr(last_day(sdate+365),4,2) in (8,11,12) order by sdate2;

-- 날짜 -> 문자 to_char   ## 날짜 포맷
-- 문자 -> 날짜 to_date   ## 날짜 사칙연산
-- 숫자 -> 문자 to_char   ## 천단위, 숫자앞에0을 표시, 통화표시
-- 문자 -> 숫자 to_number ## 천단위 표시, 천단위삭제해서 사칙연산

-- 날짜 형변환해서 날짜 포맷을 변경
-- date타입 -> char타입으로 변경해서 포맷.
select sysdate from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd') from dual;
select sysdate,to_char(sysdate,'yy-mm-dd') from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd am hh:mi:ss day') from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd hh24:mi:ss day') from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd hh24:mi:ss dy') from dual;
select sysdate,to_char(sysdate,'yyyy-mon-dd hh24:mi:ss') from dual;

select hire_date,to_char(hire_date,'yyyy-mm-dd hh:mi:ss') from employees;

-- students테이블 sdate 2024/01/01 형태로 출력하시오.
select sdate,to_char(sdate,'yyyy/mm/dd') from students;

select kor from students where kor=70;

-- 숫자타입 -> 문자타입 변경해서 포맷 천단위 표시
select salary*1382.86*12 from employees;

-- 자리수 채우기 9 : 빈공백으로 채움, 0 : 0으로 채움
-- L : 국가통화기호 표시, $ : $표시가 됨.
select to_char(salary*1382.86*12,'L000,999,999') from employees;

select 12,to_char(12,'000') from dual;

select to_char(123456,'000000000'),to_char(123456,'999,999,999') from dual;

create table chartable(
no number(4),
kor number(10),
kor_char varchar2(10),
kor_mark varchar2(10)
);

-- number,number.str-number 타입을 넣어도 입력
-- 문자형 타입에는 숫자형 타입가능
insert into chartable values(
1,10000,to_char(10000,'00000000'),to_char(10000,'0,000,000')
);
insert into chartable values(
2,10000,10000,10000
);
-- 숫자형 타입은 숫자앞에 0 있어도 표시가 되지 않음. : 문자형타입만 가능
-- 천단위 표시는 숫자형 타입에 입력이 안됨 : 문자형타입에만 가능
insert into chartable values(
3,3000000,3000000,3000000
);
select * from chartable;
commit;

create table chartable2(
no number(4),
kor number(10),
kor_char number(10),
kor_mark number(10)
);

insert into chartable2 values(
1,1000000,1000000,1000000
);
insert into chartable2 values(
2,2000000,02000000,02000000
);
select * from chartable2;
commit;

-- 숫자형타입, 문자형(숫자)타입은 사직연산간ㅇ
-- 숫자형타입과 문자 천단위 표시 숫자타입은 사칙연산 불가능, ,천단위표시는 문자형타입
-- 숫자형타입 + 문자(숫자형) 타입 = 두탕비 결과값 출력됨.
select kor*kor_char from chartable;
select kor*kor_mark from chartable;

desc chartable;

-- 2일 이후의 날짜를 출력하시오
select '20241031',to_date('2024/10/31')+2,sysdate+2 from dual;
select sysdate,sysdate+2 from dual;

select to_date('20241031')+2 from dual;

select to_date('20231031')from dual;

-- number형 타입 -> 날짜형 타입
select sysdate - to_date(20231101) from dual;
-- 문자형 타입-> 날짜형 타입 
select sysdate - to_date('20231101') from dual;

-- 문자형 타입 -> 숫자형 타입
-- 천단위 운자형타입 -> 천단위 제외 숫자형 타입
select to_number('20,000','999,999') from dual;

select * from chartable;
-- 문자형 천단위 타입 -> 숫자영 타입 변환
select kor,to_number(kor_mark,'999,999,999') from chartable;

-- 숫자형타입 이기에 사칙연산 가능
select kor*to_number(kor_mark,'999,999,999') from chartable;


-- delete chartable;

insert into chartable values(
3,30000,0030000,'3,000,000'
);

commit;
select * from chartable;

select department_id from employees;

select department_id from employees where department_id is null;

select commission_pct from employees where commission_pct is not null;

-- 월급*커미션을 계산하시오
select salary+salary*nvl(commission_pct,0) from employees;

-- null 경우 : 0 표시
select nvl(department_id,0) from employees;
-- null 경우 : CEO 표시, 숫자형타입을 문자형타입으로 변경
select nvl(to_char(department_id),'ceo') from employees;

-- 그룹합수
-- sum 합계,avg 평균,count 개수,min 최소값,max 최대값,median 중간값

select salary from employees;
select sum(salary) from employees;
select to_char(sum(salary),'999,999') from employees;

select avg(salary) from employees;
-- 소수점 2자리 반올림
select round(avg(salary),4) from employees;
select trunc(avg(salary),4) from employees;

select max(salary) from employees;
select min(salary) from employees;

-- 평균값보다 월급이 높은 사원을 출력하시오.
select avg(salary) from employees;
select * from employees;
-- 평균값을 select해서 입력함.
select emp_name,salary from employees where 6461<=salary;
select count(salary) from employees where salary >= (select avg(salary) from employees);

-- emp_name : 단일 함수, avg : 그룹함수  둘이 같이 쓰면 에러가남
select emp_name,avg(salary) from employees;

-- 단일함수와 그룹함수는 동시에 사용할수 없다
select department_id,max(salary) from employees;

-- students테이블 모든 학생의 kor점수 합계, 평균, 최대값,최소값을 구하시오
select sum(kor),avg(kor),max(kor),min(kor),median(kor) from students;


-- 부서번호가 50 사원등의 월급의 합,평균,최대값,최소값을 출력하시오.
select * from employees;
select sum(salary),avg(salary),max(salary),min(salary) from employees where department_id = 50;

-- 부서번호가 30
select sum(salary),avg(salary),max(salary),min(salary) from employees where department_id = 30;
select sum(salary),avg(salary),max(salary),min(salary) from employees where department_id = 10;

select max(salary) from employees where department_id=50;
-- group by : 단일함수를 출력하고 싶을때, 단일함수를 입력하면 됨.
select department_id,max(salary) from employees group by department_id;

select emp_name,salary from employees;

select emp_name,max(salary) from employees group by emp_name;

-- 107명의 평균
select avg(salary) from employees;
-- 단일함수,그룹함수 함꼐 사용하려면. group by 지정
select department_id,round(avg(salary)),count(salary) from employees  group by department_id order by department_id;

-- 평균월급보다 높은 사람 수를 출력하시오.
select count(salary),min(salary),max(salary) from employees where (select avg(salary) from employees)<= salary;

-- 수학함수: abs : 절대값, ceil : 올림, floor: 버림, round : 반올림, trunc: 절사, mod : 나머지, power : 제곱, sqrt : 제곱근
-- 제곱
select power(3,3),3*3*3 from dual;

-- 문자,숫자형 타입 -> 날짜형타입 변경가능
-- 숫자,날짜형 타입 -> 문자형타입 변경가능
-- 문자형 타입 -> 숫자형타입 변경가능
-- 날짜형 타입 -> 숫자형타입 변경불가, 형태를 변경해서 문자형으로 변경한 후 숫자형으로 변경가능
select 20240101,to_date('20240101') from dual;
select '2',to_number('2') from dual;

select '20240101' to_number('20240101') from dual;
select to_number(to_date('20240101')) from dual;

select sysdate,to_number(sysdate) from date;

-- 날짜형 -> 문자형변환
select sysdate,to_number(to_char(sysdate)) from dual;
select sysdate,to_number(to_char(sysdate,'yyyymmdd')) from dual;

-- 날짜형타입을 문자형 타입으로 변경시, 년 월 일 한글,특수문자 입력방법
select sysdate,to_char(sysdate,'yyyy"년"mm"월"dd"일"day') from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd day') from dual;

-- 숫자형 타입 : 사칙연산 계산해서 출력됨
select kor+eng from students;

-------------------------------------------------------------------------------
-- 문자형 함수
select emp_name,email from employees;

-- 문자형 타입을 합쳐서 + 기호를 사용해서 합치려고 하면 에러
select emp_name+email from employees;

-- || concat함수
select emp_name||email from employees; -- 속도가 조금 더 빠름
select concat(emp_name,email) from employees;

-- lower : 소문자 취환, upper : 대문자 취환, initcap : 첫글자 대문자 취환
select name from member where lower(name)='horacio';

select 'joHn',initcap('joHn'),lower('joHn'),upper('joHn') from dual;

-- lpad : 왼쪽자리수 채우기
select 'John',lpad('John',10,'#') from dual;

-- rpad : 오른쪽 자리수 채우기
select 'John',rpad('John',10,'#') from dual;

--trim : 앞,뒤공백 없애기, ltrim : 왼쪽 공백 없애기,rtrim : 오른쪽 공백 없애기
select length('    aaa   '),length(trim('    aaa   ')) from dual;

-- replace : 취환
select '    a  b c  ',trim('    a  b c  ')from dual;
select length('    a  b c  '),length(trim('    a  b c  ')),length(replace('    a  b c  ',' ',''))from dual;

-- substr : 특정위치 자르기 ( 시작위치, 개수 )
select 'abcdefg',substr('abcdefg',0,3),substr('abcdefg',3,2) from dual;

-- 입사일이 3월인 사원을 울력하시오.
select hire_date,substr(hire_date,4,2) from employees where substr(hire_date,4,2) in('03','08','10');

-- 7월 이상
select hire_date,substr(hire_date,4,2) from employees where substr(hire_date,4,2) >= 7;

select hire_date,substr(hire_date,4,2) hire_date2 from employees where substr(hire_date,4,2) > 01;

-- translate 취환
-- 한글자,한글자에 해당되는 단어를 각각의 당너로 취환
-- 순서에 없는 변화글자는 삭제처리
select 'axyz',translate('jxyzxkkcyjccx','xyk','ab') from dual;
select 'axyz',replace('jxyzxkkcyjccx','xy','ab') from dual;

-- lenght() : 문자열 길이
-- students테이블 name 글자길이가 5자 이상인 학생만 출력하시오.

select count(*) from students where length(name)>=10;

-- 사원의 월급의 합과 평균을 구하시오.
select sum(salary),avg(salary) from employees;
-- 영어점수의 합,평균,최대값,최소값을 구하시오.
select sum(eng),avg(eng),max(eng),min(eng) from students;
-- students테이블 에서
-- 홍길동,등록일 : 2023년12월02일 등록 
-- 유관순,등록일 : 2023년01월19일 ...
select name,to_char(sdate,'"등록일 : "yyyy"년"mm"월"dd"일"') from students;








