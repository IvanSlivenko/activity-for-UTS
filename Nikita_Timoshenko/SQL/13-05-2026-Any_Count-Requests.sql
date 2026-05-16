
--------------------------------------------- Декілька таблиць

------------------------------------

----------------------- Вся таблиця
SELECT * 
FROM 
	salaries 

LIMIT 10	
;

-------------------------------- Кількість рядків в талиці
SELECT COUNT (*)
FROM
	salaries	
;

--------------------------------- Кількість відсутніх значень в колонці salary_in_usd
SELECT 
	COUNT (*)
	, COUNT(*) - COUNT(salary_in_usd) AS missing_values
FROM
	salaries	
;

--------------------------
SELECT
	job_title
	, COUNT (*)
	, COUNT(*) - COUNT(job_title) AS missing_values_job_title
FROM
	salaries
GROUP BY job_title	
ORDER BY missing_values_job_title DESC
;

-----------------------------------------------
SELECT 
	job_title
	, COUNT(*)
FROM
	salaries
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10
;
------------------------------------------------

SELECT 
	job_title
	, exp_level
	, MIN(salary_in_usd)
	, MAX(salary_in_usd)
	, ROUND(AVG(salary_in_usd),2) AS avg
	, ROUND(stddev(salary_in_usd),2)
FROM
	salaries
GROUP BY 1,2
-- ORDER BY 2 DESC
LIMIT 10
;
--------------------------------------------------

SELECT 
	job_title
	, TRUNC(salary_in_usd,-1)
	, COUNT(*) AS count_salary_in_usd
FROM
	salaries
GROUP BY job_title, salary_in_usd
ORDER BY 3 DESC
;

-----------------------------------------------------
SELECT
	CASE 
		WHEN salary_in_usd <= 10000 THEN 'A'
		WHEN salary_in_usd <= 20000 THEN 'B'
		WHEN salary_in_usd <= 50000 THEN 'C'
		WHEN salary_in_usd <= 100000 THEN 'D'
		WHEN salary_in_usd <= 200000 THEN 'E'
		ELSE 'F' END AS salary_category
	, COUNT(*)
FROM salaries
GROUP BY 1






		
