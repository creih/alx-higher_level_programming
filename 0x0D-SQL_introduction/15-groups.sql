-- task 15 about use of cout
-- ikoreshwa rya function count()
SELECT score, COUNT(score) FROM second_table GROUP BY score HAVING COUNT(score)>1;
