DROP DATABASE IF EXISTS `data-science-job-analysis`;
CREATE DATABASE IF NOT EXISTS `data-science-job-analysis`;
USE `data-science-job-analysis`;

CREATE TABLE country (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE work_setting (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE employment_type (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE job_title (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE job_category (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE job (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    salary_in_usd FLOAT NOT NULL,
	company_location_id INT NOT NULL,
    employee_residence_id INT NOT NULL,
    work_setting_id INT NOT NULL,
    employment_type_id INT NOT NULL,
    job_title_id INT NOT NULL,
    job_category_id INT NOT NULL,
    
    FOREIGN KEY(company_location_id) REFERENCES country(id),
    FOREIGN KEY(employee_residence_id) REFERENCES country(id),
    FOREIGN KEY(work_setting_id) REFERENCES work_setting(id),
    FOREIGN KEY(employment_type_id) REFERENCES employment_type(id),
    FOREIGN KEY(job_title_id) REFERENCES job_title(id),
    FOREIGN KEY(job_category_id) REFERENCES job_category(id)
);

