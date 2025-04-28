
select count(*) as FISH_COUNT, fn.FISH_NAME
from FISH_INFO as fi left join FISH_NAME_INFO as fn 
on fi.FISH_TYPE = fn.FISH_TYPE
group by fn.FISH_NAME
order by 1 desc