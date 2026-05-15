
--------------------------------------------- Agregation

------------------------------------

SELECT * 
FROM 
	salaries 

LIMIT 20	
;
-------------------------------------------------------
/*
Для кожної професії та відповідного досвіду навести :

- кількість наявних спецалістів у таблиці
- середню заробітну плату


*/

SELECT 
	year
	, job_title
	, exp_level
	, COUNT(*) AS job_nmb
	, ROUND(AVG(salary_in_usd*44),2) AS salary_avg_in_uah
FROM salaries
WHERE year ='2023'
GROUP BY job_title, exp_level, year
ORDER BY job_title, exp_level
;

------------------------------------------------------- HAVING
/*

Для професій, що зустрічаються лише 2 раз
навести заробітну плату

*/


SELECT 
	year
	, job_title
	-- , COUNT(*) AS job_nmb
	, ROUND(AVG(salary_in_usd*44),2) AS salary_avg_in_uah
FROM salaries
WHERE year =2023
GROUP BY job_title, year
HAVING COUNT(*)=2
	AND ROUND(AVG(salary_in_usd*44),2) > 4000000
ORDER BY 2
;


---------------------------------------------







		
