select SUM(g.SCORE) AS SCORE, e.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
from HR_EMPLOYEES as e, HR_GRADE as g
where e.EMP_NO = g.EMP_NO
group by e.EMP_NO
order by 1 desc
limit 1

