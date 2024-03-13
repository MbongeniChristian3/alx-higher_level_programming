-- creates the database hbtn_Od_usa and the table states (in the database hbtnOd_usa) on your MYSQL server
-- creates a database
CREATE DATABASE IF NOT EXISTS hbtn_Od_usa;
-- use a database
USE hbtn_Od_usa;
-- creates a table
CREATES TABLE IF NOT EXISTS STATES (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
