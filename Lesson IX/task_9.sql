CREATE DATABASE IF NOT EXISTS employee;
USE employee;
CREATE TABLE IF NOT EXISTS workers (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
	first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    job  VARCHAR(30) NOT NULL,
    salary INTEGER NOT NULL
);
INSERT INTO workers (first_name, last_name, job, salary) VALUES ('Ivan', 'Ivanov', 'developer', 50000);
INSERT INTO workers (first_name, last_name, job, salary) VALUES ('Stepan', 'Golovin', 'project manager', 120000);
INSERT INTO workers (first_name, last_name, job, salary) VALUES ('Kate', 'Short', 'office manager', 29999);
INSERT INTO workers (first_name, last_name, job, salary) VALUES ('Leo', 'CiDaprio', 'trapper', 25000);
INSERT INTO workers (first_name, last_name, job, salary) VALUES ('Anton', 'Minogarov', 'Chief developer', 80450);
INSERT INTO workers (first_name, last_name, job, salary) VALUES ('Ryan', 'Howard', 'temp', 22130);
INSERT INTO workers (first_name, last_name, job, salary) VALUES ('Nikita', 'Sergeev', 'developer', 65130);
INSERT INTO workers (first_name, last_name, job, salary) VALUES ('Sergey', 'Nikitin', 'developer', 27894);

#Задача 2

SELECT * FROM workers WHERE salary < 30000;
SELECT first_name, last_name, salary FROM workers WHERE salary < 30000 AND job = 'developer';

# Для реализации связи многие-ко-многим создадим таблицу отношения сотрудников

CREATE TABLE IF NOT EXISTS subbordinations (	
	boss_id INTEGER NOT NULL,
    inferior_id INTEGER
);

INSERT INTO subbordinations (boss_id, inferior_id) VALUES (1, 6);
INSERT INTO subbordinations (boss_id, inferior_id) VALUES (2, 1);
INSERT INTO subbordinations (boss_id, inferior_id) VALUES (2, 5);
INSERT INTO subbordinations (boss_id, inferior_id) VALUES (2, 6);
INSERT INTO subbordinations (boss_id, inferior_id) VALUES (2, 7);
INSERT INTO subbordinations (boss_id, inferior_id) VALUES (2, 8);
INSERT INTO subbordinations (boss_id, inferior_id) VALUES (3, 6);
INSERT INTO subbordinations (boss_id, inferior_id) VALUES (5, 1);
INSERT INTO subbordinations (boss_id, inferior_id) VALUES (5, 7);
INSERT INTO subbordinations (boss_id, inferior_id) VALUES (5, 8);
INSERT INTO subbordinations (boss_id, inferior_id) VALUES (4, 0);
INSERT INTO subbordinations (boss_id, inferior_id) VALUES (7, 0);
INSERT INTO subbordinations (boss_id, inferior_id) VALUES (6, 0);
INSERT INTO subbordinations (boss_id, inferior_id) VALUES (8, 0);

SELECT first_name, last_name
FROM workers
JOIN subbordinations ON subbordinations.inferior_id = workers.id
WHERE subbordinations.boss_id= 2;