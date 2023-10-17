-- script that prints the full description
-- of the table first_table from the database hbtn_0c_0
-- in your MySQL server.
SELECT id, name FROM first_table WHERE TABLE_SCHEMA = hbtn_0c_0 AND TABLE_NAME = first_table
