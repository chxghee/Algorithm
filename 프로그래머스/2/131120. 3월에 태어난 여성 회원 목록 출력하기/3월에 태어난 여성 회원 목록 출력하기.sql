








select MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
from MEMBER_PROFILE mp
where 
    DATE_OF_BIRTH like '%-03-%' 
    and 
    TLNO is not NULL 
    and 
    GENDER = 'W'
order by MEMBER_ID asc;






