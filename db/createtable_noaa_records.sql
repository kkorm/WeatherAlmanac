USE weather_records;

CREATE TABLE IF NOT EXISTS noaa_records (
    id INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
    day TINYINT NOT NULL,
    office_id VARCHAR(10) NOT NULL,
    station_id VARCHAR(10) NOT NULL,
    temp_max SMALLINT,
    temp_min SMALLINT,
    temp_avg SMALLINT,
    temp_hdd SMALLINT,
    temp_cdd SMALLINT,
    prec_water DECIMAL(5,2),
    prec_snow DECIMAL(5.2),
    prec_snow_depth TINYINT,
    wind_2minspeed_avg DECIMAL(5,2),
    wind_2minspeed_max SMALLINT,
    wind_dir TINYINT UNSIGNED,
    weather_types VARCHAR(10),
    wind_peak_speed TINYINT UNSIGNED,
    wind_peak_dir SMALLINT
)