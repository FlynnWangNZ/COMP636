-- question 1
create view YoungOnes as select * from people where age < 21;

-- question 2
select * from YoungOnes;

-- question 3
create view ChchDunedinPeople as select name, sex, age from people where city in ('Christchurch', 'Dunedin');
