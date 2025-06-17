-- 코드를 작성해주세요
select ID, 
    case 
        when SizeRank = 1 then "CRITICAL"
        when SizeRank = 2 then "HIGH"
        when SizeRank = 3 then "MEDIUM"
        when SizeRank = 4 then "LOW"
            end as COLONY_NAME
from (
    select 
        ID, 
        SIZE_OF_COLONY, 
        NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC) AS SizeRank
    from 
        ECOLI_DATA
) as RankedColony
order by ID