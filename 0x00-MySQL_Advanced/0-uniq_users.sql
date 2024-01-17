-- i created a table if noit exists usesr
CREATE TABLE IF NOT EXIST users(
       id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255)
)
