-- 코드를 작성해주세요

with MAX_COLONY as (
    select  year(DIFFERENTIATION_DATE) as YEAR, max(SIZE_OF_COLONY) as MAX_SIZE
    from ECOLI_DATA
    group by year(DIFFERENTIATION_DATE)
)



SELECT YEAR(DIFFERENTIATION_DATE) as YEAR,
    m.MAX_SIZE - d.SIZE_OF_COLONY as YEAR_DEV,
    ID

FROM ECOLI_DATA d
join MAX_COLONY m
on year(DIFFERENTIATION_DATE) = m.YEAR
order by 1 asc, 2 asc

