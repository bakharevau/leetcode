SELECT user_id AS buyer_id,
       join_date,
       count(order_id) AS orders_in_2019
FROM Orders
RIGHT JOIN Users
ON Orders.buyer_id = Users.user_id
AND year(order_date)=2019
GROUP BY user_id, join_date