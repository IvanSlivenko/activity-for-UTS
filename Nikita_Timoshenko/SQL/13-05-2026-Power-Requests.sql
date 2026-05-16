
--------------------------------------------- Вкладені запити

------------------------------------

SELECT * 
FROM 
	salaries 

LIMIT 20	
;
----------------------------------------------- Завдання 1

/*
Вивести всіх спеціалістів, в яких ЗП вище середньої 
*/

SELECT * 
FROM 
	salaries 
--filter 1
WHERE salary_in_usd > 

--------------------------------------- вкладений запит
(
	SELECT 
		AVG(salary_in_usd)
	FROM salaries 
	WHERE
		year = 2023
)

-- filter 2
AND 
	year = 2023

;
-------------------------------------------- Завдання 2
/*
Вивести всіх спеціалістів, які живуть в країнах, де середня 
зп 
вища за середню зп усіх країн.

*/

--1.
SELECT AVG(salary_in_usd)
	FROM
	salaries
;
--/////////////////////////////////

SELECT 
*
-- job_title
FROM salaries
WHERE emp_location IN 
(
	--2.
	------------------------ 2 рівень вкладеності
	SELECT compani_location
	FROM salaries
	WHERE year = 2023	
	GROUP BY compani_location
	HAVING AVG(salary_in_usd) > 
	----------------------------- 3 рівень вкладеності
	(
	-- 3.
		SELECT AVG(salary_in_usd)
		FROM salaries
		WHERE year = 2023
	)

)
;
--4.

------------------------------------------ Завдання 3

/*
Знайти мінімальну ЗП серед максимальних з/п по країнах у 2023 році
*/



---------------------------------------- Варіант 1 
SELECT  MIN(t.max_salary_in_usd)
FROM 
	(
	SELECT compani_location
		, MAX(salary_in_usd) AS max_salary_in_usd 
	FROM salaries
	WHERE year=2023
	GROUP BY 1
	) AS t
;	

----------------------------------------- Варіант 2
SELECT compani_location
		, MAX(salary_in_usd) AS max_salary_in_usd 
	FROM salaries
	WHERE year=2023
	GROUP BY 1
	ORDER BY 2
LIMIT 1	
;

----------------------------------------------------------------- Завдання 4
-- По кожній професцї вивести різницю між середньою зп та 
-- максимальною зп усіх спеціалістів

-- 1. Максимальна ЗП 
SELECT MAX(salary_in_usd) AS max_salary_in_usd 
FROM salaries
;

--2. Середня зп по всіх професіях
SELECT 
	job_title 
	, AVG(salary_in_usd) -
	(
		SELECT MAX(salary_in_usd) AS max_salary_in_usd 
		FROM salaries
	) AS  avg_dif_max_salary_in_usd
	 
FROM salaries
GROUP BY 1
;

-------------------------------------------------------------- Завдання 5
-- Вивести данні по співробітнику, який отримує другу за розміром зп таблиці

-------------------- Варіант 1
SELECT *
FROM
	(
	SELECT 
		job_title
		, salary_in_usd 
	FROM  salaries
	ORDER BY salary_in_usd DESC
	LIMIT 2
	)
ORDER BY salary_in_usd ASC	
LIMIT 1
;
-------------------- Варіант 2
SELECT 
		job_title
		, salary_in_usd 
	FROM  salaries
	ORDER BY salary_in_usd DESC
	LIMIT 1 OFFSET 1 


	












		
