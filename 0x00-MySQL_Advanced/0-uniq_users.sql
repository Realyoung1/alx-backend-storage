-- create table 'users' with attrs (id,email,name)
i created a table if not exists users(
       id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255)
)
