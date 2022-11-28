-- question 1
select * from people where city in ('Christchurch', 'Dunedin');

-- question 2
select name, age, weight from people where age < 20 and city = 'Dunedin';

-- question 3
select * from people where weight not between 50 and 90 order by age desc;

-- question 4
select weight from people;

-- question 5
select distinct weight from people;

-- question 6
-- ID, sex and city
-- not female or from Hamilton
-- 34
