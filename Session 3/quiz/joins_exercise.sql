-- question 1
select FirstName, LastName, Phone from member where memberteam in (select teamname from team where PracticeNight='Monday');

-- question 2
select FirstName, LastName, Handicap, PracticeNight from member, team where member.Handicap<20 and member.MemberTeam = team.TeamName

-- question 3
select practicenight, count(*) as NumberOfMembers from member, team where member.memberteam = team.TeamName group by PracticeNight;

-- question 4
select TeamName, count(*) as NumberOfMembers, count(*)*playerFee as TotalFee from member, team where member.memberteam = team.TeamName group by teamname;
