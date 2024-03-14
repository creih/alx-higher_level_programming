-- task 8
-- using select cyane
SELECT cities.name FROM cities WHERE cities.state_id = ( SELECT name FROM states WHERE name='California') ORDER BY cities.id ASC;
