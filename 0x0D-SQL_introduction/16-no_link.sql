-- task 16 about
-- write 2nd table recs
USE hbtn_0c_0;
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
