-- creates the database hbtn_Od_2 and the user user_Od_2
-- creates a database
CRAETES DATABASE IF NOT EXISTS Hbtn_Od_2;
-- creates a user
CRAETES DATABASE IF NOT EXISTS Hbtn_Od_2@localhost IDENTIFIED BY `user_Od_2_pwd`;
-- grants SELECT privileges to a user
GRANT SELECT ON hbtn_Od_2.* TO user_Od_2@localhost;
