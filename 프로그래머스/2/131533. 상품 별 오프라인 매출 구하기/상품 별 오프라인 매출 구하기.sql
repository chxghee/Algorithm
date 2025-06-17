

select PRODUCT_CODE, sum(PRICE * SALES_AMOUNT) as SALES
from PRODUCT as p, OFFLINE_SALE as o
where
    p.PRODUCT_ID = o.PRODUCT_ID
group by PRODUCT_CODE
order by SALES desc, PRODUCT_CODE asc







