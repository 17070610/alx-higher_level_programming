-- creating a full table with rows and data in it

CREATE TABLE IF NOT EXISTS second_table (
	id INT PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	score INT NOT NULL
);

INSERT INTO second_table (id, name, score)
VALUES
	(1, 'John', 10),
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'Goerge', 8);
