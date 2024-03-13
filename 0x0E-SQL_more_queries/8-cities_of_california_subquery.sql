-- Lists all the cities of California that canbe found in the database hbtn_Od_usa
-- lists all rows of a column in database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = `california`) ORDER BY id ASC
