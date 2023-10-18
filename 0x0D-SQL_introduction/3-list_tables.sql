-- script that lists all the tables of a database in your MySQL server.
mysql=$1
mysql -u root -p -e "USE $mysql; SHOW TABLES;"

