
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

SELECT compani_location
		, MAX(salary_in_usd) AS max_salary_in_usd 
	FROM salaries
	WHERE year=2023
	GROUP BY 1
	ORDER BY 2
LIMIT 1	
;






		
