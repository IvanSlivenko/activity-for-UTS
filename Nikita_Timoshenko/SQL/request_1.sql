SELECT 
	  1 AS nbm_1
	, 2 AS nbm_2
	, 5 + 5  AS nbm_3

;
-------------------------
SELECT *
FROM salaries
LIMIT 10
;
-------------------------

SELECT 
	 COUNT(*)            AS count_all
	, COUNT(exp_level)  AS count_level
	, COUNT( DISTINCT exp_level)
FROM salaries

LIMIT 10

;

--------------------------------------------
SELECT
	AVG(salary_in_usd) AS salary_avg
	, MIN(salary_in_usd) AS salary_min 
	, MAX(salary_in_usd) AS salary_max 

FROM salaries

WHERE 
	year = '2023'


LIMIT 10
;
-------------------------
SELECT 
	year
	, exp_level
	, salary_in_usd
	, salary_in_usd * 43 as salary_in_uah
	, salary_in_usd * 43 / 12 as salary_in_uah_Mount
------------------------------------------------------- case
	-- 'SE' - Senior
	-- 'MI' - Middle
	-- Other 

	, CASE 
		WHEN  exp_level = 'SE' 
			THEN 'Senior'
		WHEN  exp_level = 'MI'	
			THEN 'Middle'
		ELSE 'Other' 
	  END	AS full_level	
			
FROM salaries

WHERE 
		year=2023
ORDER BY salary_in_usd asc

LIMIT 100
;
-------------------------



SELECT
	year
	, job_title
	, salary_in_usd

FROM salaries
WHERE 
	year = '2023'
	AND
		job_title='ML Engineer'
ORDER BY salary_in_usd asc	
-- LIMIT 10
;

---------------------------------------------
















