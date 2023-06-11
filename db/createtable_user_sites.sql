USE weather_records;

CREATE TABLE IF NOT EXISTS user_sites (
    id INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
    description VARCHAR(50)
);