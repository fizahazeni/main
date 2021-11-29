#SQL queries performed for project in NTU for the module BC2402

#Q1
select * from country_details;
SELECT SUM(population) AS Total_Population
FROM (SELECT population FROM country_details
WHERE continent = "Asia") sum_population;

#Q2 
SELECT SUM(population) AS total_population_ASEAN
from country_details
WHERE iso_code IN ('BRN', 'KHM', 'IDN', 'LAO', 'MYS', 'MMR', 'PHL', 'SGP', 'THA', 'VNM');

#Q3
SELECT DISTINCT source_name FROM source;

#Q4
SELECT date, daily_vaccinations
FROM country_vaccinations_table 
WHERE iso_code="SGP" AND (date BETWEEN "2021-03-01" AND "2021-05-31");

#Q5
SELECT MIN(date) FROM country_vaccinations_table 
WHERE iso_code="SGP" AND daily_vaccinations > 0;

#Q6
SELECT ROUND(SUM(new_cases_smoothed)) FROM country_cases
WHERE iso_code = 'SGP' AND
date >= (SELECT min(date)
FROM country_vaccinations_table
WHERE iso_code = 'SGP' AND daily_vaccinations > 0);

#Q7
SELECT ROUND(SUM(new_cases)) FROM country_cases
WHERE iso_code = 'SGP' AND
`date` < (SELECT MIN(date)
FROM country_vaccinations_table
WHERE iso_code = 'SGP' AND
daily_vaccinations > 0);

#Q8
SELECT c.country, cc.date, cv.vaccine, cv.total_vaccinations, 
concat(round(cc.new_cases_smoothed/c.population*100,5),”%”) as Percentage_of_new_cases
FROM country_details c INNER JOIN country_cases cc ON c.iso_code = cc.iso_code 
INNER JOIN country_vaccinations_by_manufacturer cv ON cc.date = cv.date 
WHERE c.country = "Germany" AND cv.location="Germany";

#Q9
SELECT ac.country, a.date, ROUND(a.new_cases_smoothed) 'New Cases', b.vaccine, b.total_vaccinations '20th Day', 
c.total_vaccinations '30th Day', d.total_vaccinations '40th Day'
FROM country_details ac, country_cases a, country_vaccinations_by_manufacturer b, country_vaccinations_by_manufacturer c, 
country_vaccinations_by_manufacturer d
WHERE ac.country = 'Germany' AND
ac.country=b.location AND
ac.iso_code = a.iso_code AND
ac.country=c.location AND
b.vaccine=c.vaccine AND
ac.country=d.location AND
b.vaccine=d.vaccine AND
b.date = date_add(a.date, interval 20 day) AND
c.date = date_add(a.date, interval 30 day) AND
d.date = date_add(a.date, interval 40 day);

#Q10
SELECT ac.country, a.date, a.vaccine, a.total_vaccinations 'Total Vaccinations', ROUND(b.new_cases_smoothed) '21st Day',
ROUND(c.new_cases_smoothed) '60th Day', ROUND(d.new_cases_smoothed) '120th Day'
FROM country_details ac, country_vaccinations_by_manufacturer a, country_cases b, country_cases c, country_cases d
WHERE ac.country = 'Germany' AND
ac.country = a.location AND
ac.iso_code=b.iso_code AND
ac.iso_code=c.iso_code AND
ac.iso_code=d.iso_code AND
b.date = date_add(a.date, interval 21 day) AND
c.date = date_add(a.date, interval 60 day) AND
d.date = date_add(a.date, interval 120 day);
