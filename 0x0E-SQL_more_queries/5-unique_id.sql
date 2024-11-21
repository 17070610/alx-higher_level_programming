-- Creates a table with a unique id

CREATE TABLE IF NOT EXISTS unique_id(
	id DEFAULT 1 UNIQUE,
	name VARCHAR(255)
);
