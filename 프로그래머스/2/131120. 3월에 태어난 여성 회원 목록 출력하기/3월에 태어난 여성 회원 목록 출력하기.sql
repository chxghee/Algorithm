


select MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d") as DATE_OF_BIRTH
from MEMBER_PROFILE mp
where mp.GENDER = 'W'
    and 
    mp.DATE_OF_BIRTH like '%-03-%'
    and
    mp.TLNO is not NULL
order by mp.MEMBER_ID ASC

