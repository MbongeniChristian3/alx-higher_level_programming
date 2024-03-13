-- creates the table id_not_null on your MYSQL server
-- creates a table
CREATES TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));

