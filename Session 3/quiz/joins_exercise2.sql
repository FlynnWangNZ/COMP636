-- question 1
select t.tourid, count(*) as NumEntries from tournament t, entry e where t.tourid = e.tourid and year = 2012 group by t.tourid;

-- question 2
select t1.tourid as TourID, t2.tourname, t1.numentries from (select t.tourid, count(*) as NumEntries from tournament t, entry e where t.tourid = e.tourid and year = 2012 group by t.tourid) t1, tournament t2 where t1.tourid = t2.tourid;

-- question 3
select t1.memberid as MemberID, t2.firstname, t2.lastname, t1.year as Year from (select memberid, year from entry where tourid = (select tourid from tournament where tourid = 40)) t1, member t2 where t1.memberid = t2.memberid;

-- question 4
select memberid, firstname, lastname from member where memberid in (select memberid from entry where tourid = (select tourid from tournament where tourid = 40))
