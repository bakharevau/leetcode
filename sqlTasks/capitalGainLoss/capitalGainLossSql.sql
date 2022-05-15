SELECT stock_name, (gain - loss) AS capital_gain_loss
FROM
(
SELECT stock_name, SUM(price) AS loss
FROM Stocks
WHERE operation = 'Buy'
GROUP BY stock_name
)S1 LEFT JOIN
(
SELECT stock_name, SUM(price) AS gain
FROM Stocks
WHERE operation = 'Sell'
GROUP BY stock_name
) S2
USING(stock_name)