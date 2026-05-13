
--------------------------------------------- Filters
SELECT * 
FROM 
	salaries 
WHERE
	year < '2023'
LIMIT 20
;
------------------------------------

SELECT * 
FROM 
	salaries 
WHERE
	exp_level ='SE'
LIMIT 20
;
------------------------------------
SELECT * 
FROM 
	salaries
WHERE 
		exp_level = 'MI'
	OR
		exp_level = 'SE' 
	OR
		exp_level = 'MI'
	-- NOT
	
LIMIT 20
;
------------------------------------- BETWEEN
SELECT 
	-- *
	DISTINCT year
FROM 
	salaries
WHERE 1=1
	AND year BETWEEN 2020 AND 2023 
	
	ORDER BY year 
LIMIT 20
;
------------------------------------- NOT BETWEEN
SELECT 
	-- *
	DISTINCT year
FROM 
	salaries
WHERE 1=1
	AND year NOT BETWEEN 2021 AND 2023 
	
	ORDER BY year 
LIMIT 20
;
--------------------------------------- IN
SELECT 
	-- *
	DISTINCT year
FROM 
	salaries
WHERE 1=1
	AND year IN(2020, 2021) 
	
	ORDER BY year 
LIMIT 20
;
--------------------------------------- NOT IN
SELECT 
	-- *
	DISTINCT year
FROM 
	salaries
WHERE 1=1
	AND year NOT IN(2020, 2021) 
	
	ORDER BY year 
LIMIT 20
;
--------------------------------------- IN ('text')
SELECT 
	-- *
	DISTINCT job_title
FROM 
	salaries
WHERE 1=1
	AND job_title IN('Data Scientist', 'Product Data Analyst') 
	
LIMIT 20
;
--------------------------------------- LIKE ('text ' приблизно)
SELECT 
	-- *
	DISTINCT job_title
FROM 
	salaries
WHERE 1=1
	-- AND job_title LIKE ('Data S%')
	-- AND job_title NOT LIKE ('Data_A%')
	-- AND job_title LIKE ('Data_A%')---------------- Відчутний до регістрів
	AND job_title LIKE ('_ata_A%')
	
LIMIT 20
;

--------------------------------------- iLIKE ('text ' приблизно)
SELECT 
	-- *
	DISTINCT job_title
FROM 
	salaries
WHERE 1=1
	
	AND job_title iLIKE ('data_A%')
	
LIMIT 20
;

--------------------------------------- IS NULL
SELECT 
	*
	-- DISTINCT job_title
FROM 
	salaries
WHERE 1=1
	-- AND job_title iLIKE ('data_A%')
	AND year IS NULL
LIMIT 20
;

--------------------------------------- IS NOT NULL
SELECT 
	COUNT(*)
	-- DISTINCT job_title
FROM 
	salaries
WHERE 1=1
	AND year IS NOT NULL
LIMIT 20
;








		
