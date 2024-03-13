-- creates the database hbtn_Od_usa and the table cities (in the database hbtnOd_usa) on your MYSQL server
-- creates a database
CREATE DATABASE IF NOT EXISTS hbtn_Od_usa;
-- use a database
USE hbtn_Od_usa;
-- creates a table
CREATES TABLE IF NOT EXISTS cities (id INT UNIQUE NOT NULL AUTO_INCREMENT NOT NULL, state_id INT NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY(state_id) REFERENCES states(id));


