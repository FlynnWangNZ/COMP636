-- question 1
select m.FirstName as MemberFirst, m.lastname as MemberLast, m.MemberTeam as TeamName, t.PracticeNight as PracticeNight from member m, team t where m.memberteam  = t.teamname

-- question 2
select m.FirstName as MemberFirst, m.lastname as MemberLast, m.MemberTeam as TeamName, t.PracticeNight as PracticeNight from member m left join team t on m.memberteam = t.teamname;

-- question 3
select 
t1.firstname as MemberFirst,
t1.lastname as MemberLast,
t1.TeamName as TeamName,
t1.PracticeNight as PracticeNight,
t2.FirstName as CaptainFirst,
t2.Lastname as CaptainLast,
t3.firstname as ViceCaptFirst,
t3.lastname as ViceCaptLast
from (select * from member m left join team t on m.memberteam = t.teamname) t1 left join (select * from member m left join team t on m.memberteam = t.teamname) t2 on t1.teamcaptain = t2.memberid left join (select * from member m left join team t on m.memberteam = t.teamname) t3 on t1.teamvicecaptain = t3.memberid
