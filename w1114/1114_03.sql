create table students2(
s_name varchar2(100),
s_major varchar2(100),
s_age number default 0,
s_grade number default 0,
s_gender varchar2(30)
);

select * from employees;

select * from students2;

insert into students2 values(
'홍길동','com',20,1,'M'
);
commit;