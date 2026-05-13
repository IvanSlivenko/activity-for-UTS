SELECT *
FROM
salaries
;
--------------------
SELECT  
	year
	, exp_level AS level
	, emp_type as type
FROM salaries 
LIMIT 20
;

--------------------------
SELECT *
FROM
salaries

-- ML Engineer
-- 2023
-- salary_in_usd
;
-------------------------- Завдання 1
SELECT 
	job_title,
	year,
	salary_in_usd
FROM
	salaries
WHERE
	year = '2023'
	AND
		job_title='ML Engineer'
	ORDER BY salary_in_usd DESC
LIMIT 5
;
----------------------------------- Завдання 2
-- emp_location
-- salary_in_usd
-- Data Scientist


SELECT 
	emp_location,
	job_title,
	year,
	salary_in_usd
FROM
	salaries
WHERE
	year = '2023'
	AND
		job_title='Data Scientist'
	ORDER BY salary_in_usd ASC
LIMIT 10
;
----------------------------------- Завдання 3
SELECT *
FROM
salaries
;
--//////////////////////////////////

-- salary_ib_usd
-- remote_ration

SELECT 
	remote_ration
	emp_location,
	job_title,
	salary_in_usd
FROM
	salaries
WHERE
	remote_ration = '100'
	
	ORDER BY salary_in_usd DESC
LIMIT 5
;
------------------------------------- Завдання 4
SELECT *
FROM
salaries
LIMIT 1
;
--//////////////////////////////////

SELECT DISTINCT
	-- emp_location
	-- remote_ration
	job_title
FROM
	salaries
ORDER BY job_title ASC 	

;
----------------------------------- Завдання 5
SELECT COUNT(DISTINCT job_title) AS job_title 
FROM
	salaries
;
----------------------------------- Завдання 6
-- salary_in_usd
SELECT 
	ROUND(AVG(salary_in_usd),0)  AS avg_Sallary
	, MIN(salary_in_usd) AS min_Sallary
	, MAX(salary_in_usd) AS max_Sallary	

FROM
	salaries
WHERE year ='2023'	
;
--------------------------------- Завдання 7
-- ML Engineer
SELECT * 
	
FROM
	salaries
LIMIT 5
;
--//////////////////////////////////





		
