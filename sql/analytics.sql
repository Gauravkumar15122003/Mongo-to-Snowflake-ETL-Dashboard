--Top products by revenue
SELECT p.product_id, p.name, SUM(oi.item_total) as revenue
FROM FACT_ORDER_ITEMS oi
JOIN DIM_PRODUCTS p ON p.product_id = oi.product_id
GROUP BY 1,2
ORDER BY revenue DESC
LIMIT 10;


--Customer Lifetime Value
SELECT c.customer_id, c.name, SUM(o.order_total) as lifetime_spend, COUNT(o.order_id) as orders
FROM FACT_ORDERS o
JOIN DIM_CUSTOMERS c ON c.customer_id = o.customer_id
GROUP BY 1,2
ORDER BY lifetime_spend DESC
LIMIT 20;


--Average rating per product:
SELECT p.product_id, p.name, AVG(r.rating) as avg_rating, COUNT(r.review_id) as reviews
FROM FACT_REVIEWS r
JOIN DIM_PRODUCTS p ON p.product_id = r.product_id
GROUP BY 1,2
ORDER BY avg_rating DESC
LIMIT 20;