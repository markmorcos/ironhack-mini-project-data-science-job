USE project1;

SELECT * FROM project1.country;
SELECT * FROM project1.employment;
SELECT * FROM project1.work;
SELECT * FROM project1.job_title;
SELECT * FROM project1.job_category;
SELECT * FROM project1.job;


-- Count 
SELECT MIN(salary_in_usd) FROM project1.job;
SELECT MAX(salary_in_usd) FROM project1.job;


-- H1 = Avarage salary per job category 
SELECT jc.name AS job_category, ROUND(AVG(j.salary_in_usd),2) AS salary_per_year FROM project1.job_category as jc
JOIN project1.job as j
ON jc.id = j.category_id
GROUP BY job_category
ORDER BY salary_per_year desc ;

-- H2 = Average salary per employment type
SELECT * FROM job;
SELECT * FROM employment;
SELECT e.name AS employment_type, ROUND(AVG(j.salary_in_usd),2) AS average_salary FROM project1.employment as e
JOIN project1.job as j
ON e.id = j.employment_type_id
GROUP BY employment_type
ORDER BY average_salary desc;

-- MAX salary per employment type
SELECT e.name AS employment_type, MAX(j.salary_in_usd) AS max_salary FROM project1.employment as e
JOIN project1.job as j
ON e.id = j.employment_type_id
GROUP BY employment_type
ORDER BY max_salary desc;

-- H3 employment_type, salary, company_location
SELECT * FROM project1.employment;
SELECT * FROM project1.job;


-- H3 company_location, work setting and average salaries 
SELECT 
c.name AS company_location, 
w.name AS work_setting, 
ROUND(AVG(j.salary_in_usd),2) AS average_salary FROM project1.work as w
JOIN project1.job as j
ON w.id = j.work_setting_id
JOIN project1.country as c
ON c.id = j.company_location_id
GROUP BY work_setting, company_location
ORDER BY company_location, work_setting desc;


SELECT 
e.name AS employment_type, 
ROUND(AVG(j.salary_in_usd),2) AS salary, 
c.name AS employee_residence  FROM project1.employment as e
JOIN project1.job as j
ON e.id = j.employment_type_id
JOIN project1.country as c
ON c.id = j.employee_residence_id
GROUP BY employment_type, employee_residence
ORDER BY employment_type, salary desc;


SELECT 
    e.name AS employment_type, 
    c.name AS employee_residence, 
    ROUND(AVG(j.salary_in_usd), 2) AS avg_salary, 
    ROUND(STDDEV(j.salary_in_usd), 2) AS salary_stddev
FROM project1.employment AS e
JOIN project1.job AS j
    ON e.id = j.employment_type_id
JOIN project1.country AS c
    ON c.id = j.employee_residence_id
GROUP BY employment_type, employee_residence
ORDER BY employment_type, salary_stddev DESC;

SELECT jc.name AS job_category, ROUND(AVG(j.salary_in_usd),2) AS salary_per_year FROM project1.job_category as jc
JOIN project1.job as j
ON jc.id = j.category_id
GROUP BY job_category
ORDER BY salary_per_year desc ;


