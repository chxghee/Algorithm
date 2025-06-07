

select ai.name, ai.DATETIME
from ANIMAL_INS as ai
where ai.ANIMAL_ID not in (
    select ao.ANIMAL_ID
    from ANIMAL_OUTS as ao
)
order by ai.DATETIME
limit 3;