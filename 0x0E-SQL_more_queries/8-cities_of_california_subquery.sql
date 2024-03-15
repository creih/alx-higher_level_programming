-- task 8 about selecting multiple fields from diff tables
-- using select cyane
SELECT id, name FROM cities WHERE state_id=(SELECT id FROM states WHERE name='California') ORDER BY cities.id ASC;
