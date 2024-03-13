creates the MYSQL server user user_Od_1 and grant all privileges
CREATE USER IF NOT EXISTS user_Od_1@localhost IDENTIFIED BY `user_Od_1pwd`;
GRANT ALL PRIVILEGES ON * . * TO user_Od_1@localhost;

