-- task 101
-- about order by desc
SELECT city, AVG(value) AS average_temperature_fahrenheit FROM temperatures GROUP BY city ORDER BY average_temperature_fahrenheit DESC;
