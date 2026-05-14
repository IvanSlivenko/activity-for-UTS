
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
	job_title
	, COUNT(*) AS job_nmb
	, ROUND(AVG(salary_in_usd*44),2) AS salary_avg_in_uah
FROM salaries
GROUP BY job_title
ORDER BY salary_avg_in_uah DESC
;








		
