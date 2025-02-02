# Write your MySQL query statement below
WITH rk AS (
    SELECT DISTINCT 
        product_id, 
        new_price AS price, 
        RANK() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rk
    FROM 
        products p
    WHERE 
        change_date <= '2019-08-16'
)

SELECT 
    product_id, 
    price 
FROM 
    rk
WHERE 
    rk = 1

UNION

SELECT DISTINCT 
    product_id, 
    10 AS price
FROM 
    products
WHERE 
    product_id NOT IN (
        SELECT 
            product_id
        FROM 
            products
        WHERE 
            change_date <= '2019-08-16'
    );