-- Query: Create 3 new dojos
INSERT INTO dojos_and_ninjas_schema.dojos (name) VALUES ("Online");
INSERT INTO dojos_and_ninjas_schema.dojos (name) VALUES ("San Jose");
INSERT INTO dojos_and_ninjas_schema.dojos (name) VALUES ("Seattle");

-- Query: Delete the 3 dojos you just created
SET SQL_SAFE_UPDATES = 0;
DELETE FROM dojos_and_ninjas_schema.dojos;

-- Query: Create 3 more dojos
INSERT INTO dojos_and_ninjas_schema.dojos (name) VALUES ("Burbank"); -- dojo #4
INSERT INTO dojos_and_ninjas_schema.dojos (name) VALUES ("Bellavue"); -- dojo #5
INSERT INTO dojos_and_ninjas_schema.dojos (name) VALUES ("Online"); -- dojo #6

-- Query: Create 3 ninjas that belong to the first dojo
INSERT INTO dojos_and_ninjas_schema.ninjas (first_name, last_name, age,dojo_id) values ("Juleus", "Alquizalas", 50, 4);
INSERT INTO dojos_and_ninjas_schema.ninjas (first_name, last_name, age,dojo_id) values ("Jeremy", "Alquizalas", 19, 4);
INSERT INTO dojos_and_ninjas_schema.ninjas (first_name, last_name, age,dojo_id) values ("Kyle", "Alquizalas", 15, 4);

-- Query: Create 3 ninjas that belong to the second dojo
INSERT INTO dojos_and_ninjas_schema.ninjas (first_name, last_name, age,dojo_id) values ("Po", "Panda", 15, 5);
INSERT INTO dojos_and_ninjas_schema.ninjas (first_name, last_name, age,dojo_id) values ("Tigres", "Tiger", 16, 5);
INSERT INTO dojos_and_ninjas_schema.ninjas (first_name, last_name, age,dojo_id) values ("Oogway", "Turtle", 105, 5);

-- Query: Create 3 ninjas that belong to the third dojo
INSERT INTO dojos_and_ninjas_schema.ninjas (first_name, last_name, age,dojo_id) values ("Toothless", "NightFury", 17, 6);
INSERT INTO dojos_and_ninjas_schema.ninjas (first_name, last_name, age,dojo_id) values ("StormFly", "DeadlyNadder", 15, 6);
INSERT INTO dojos_and_ninjas_schema.ninjas (first_name, last_name, age,dojo_id) values ("Meatlug", "Grongkle", 16, 6);


-- Query: Retrieve all the ninjas from the first dojo
SELECT id FROM dojos ORDER BY id ASC LIMIT 1;
SELECT * FROM ninjas WHERE dojo_id = (SELECT id FROM dojos ORDER BY id ASC LIMIT 1);

-- Query: Retrieve all the ninjas from the last dojo
SELECT id FROM dojos_and_ninjas_schema.dojos ORDER BY id DESC LIMIT 1;
SELECT * FROM ninjas WHERE dojo_id = (SELECT id FROM dojos_and_ninjas_schema.dojos ORDER BY id DESC LIMIT 1);


-- Query: Retrieve the last ninja's dojo

SELECT dojo_id from ninjas ORDER BY id DESC LIMIT 1;