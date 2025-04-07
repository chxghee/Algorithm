

select month(start_date), car_id, count(history_id) 'records'
from car_rental_company_rental_history
where car_id in (
    select car_id
    from car_rental_company_rental_history
    where date(start_date) >= '2022-08-01' and date(start_date) < '2022-11-01'
    group by car_id
    having count(history_id) >= 5
) and date(start_date) >= '2022-08-01' and date(start_date) < '2022-11-01'
group by car_id, month(start_date)
order by month(start_date), car_id desc
