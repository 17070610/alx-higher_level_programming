-- Creates a table id_not_null on my MySQL server where id has a default value 1

CREATE TABLE IF NOT EXISTS id_not_null(id INT DEFAULT 1, name VARCHAR(255) NOT NULL);
