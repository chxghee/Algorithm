

select CAR_TYPE, count(*) as CARS
from CAR_RENTAL_COMPANY_CAR
where OPTIONS like '%시트%'
group by CAR_TYPE
order by 1