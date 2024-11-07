
select * from students;

-- 평균이 80점이상, 국어 90점 이상인 학생을 출력하시오
select * from students where avg>80 and kor>90;

-- 평균이 60점이상 또는 총점이 100점 이상
select * from students where avg>60 or total>100;

select * from students order by kor desc,eng desc;
