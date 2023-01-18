-- #1
SELECT countries.name, languages.language, languages.percentage FROM languages
LEFT JOIN countries ON country_code = countries.code WHERE language="Slovene" ORDER BY  languages.percentage DESC;

-- #2
SELECT countries.name, COUNT(cities.name) from countries
LEFT JOIN cities ON country_code = countries.code GROUP BY countries.name ORDER BY COUNT(cities.name) DESC;

-- #3
SELECT cities.name, cities.population, country_id from cities
LEFT JOIN countries ON country_code = countries.code WHERE countries.name="MEXICO" AND cities.population > 500000 ORDER BY cities.population DESC ;

-- #4
SELECT countries.name, languages.language, languages.percentage FROM languages
LEFT JOIN countries ON country_code = countries.code WHERE languages.percentage > 89 ORDER BY languages.percentage DESC;

-- #5
SELECT countries.name, countries.surface_area, countries.population from countries
where countries.surface_area < 501 AND countries.population > 100000;

-- #6
SELECT countries.name, countries.government_form , countries.capital, countries.life_expectancy from countries
where countries.government_form="Constitutional Monarchy" AND countries.life_expectancy > 75;


-- #7
SELECT countries.name, cities.name, cities.district, cities.population from cities
LEFT JOIN countries ON country_code = countries.code WHERE countries.name="Argentina" AND cities.district="Buenos Aires" AND cities.population > 500000;

-- #8
SELECT countries.region, count(countries.region) from countries GROUP BY countries.region ORDER BY count(countries.region) DESC


