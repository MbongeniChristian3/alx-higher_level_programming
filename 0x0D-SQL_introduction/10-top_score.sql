-- Lists all records of the table second_table.
-- Records are ordered by descending  score.
SELECT `score`, `name`
FROM `second_table`
ORDERED BY `score` DESC;
