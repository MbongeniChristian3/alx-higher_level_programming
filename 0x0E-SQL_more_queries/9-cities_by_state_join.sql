-- lists all cities contained in the database hbtn_Od_usa
-- lists all rows of a paarticular column in a database
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;

