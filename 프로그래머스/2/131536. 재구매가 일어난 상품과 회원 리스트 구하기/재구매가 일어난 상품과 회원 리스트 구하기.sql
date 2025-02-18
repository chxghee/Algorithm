select USER_ID, PRODUCT_ID
from ONLINE_SALE os
group by USER_ID, PRODUCT_ID
having count(*) >= 2
order by 1 asc, 2 desc