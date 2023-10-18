-- creates table force_name on your MySQL server.
   -- force_name description:
      -- id INT
      -- name VARCHAR(256) can’t be null
   -- database name will be passed as an argument of the mysql command
   -- If that table force_name already exists, script should not fail

CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
