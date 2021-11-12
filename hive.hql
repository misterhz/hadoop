set hive.execution.engine=mr;

drop table if exists accidents_ext;
drop table if exists boroughs_ext;
drop view if exists manhattan_injuries;
drop view if exists manhattan_deaths;
drop view if exists manhattan;

create external table if not exists accidents_ext (
    street string,
    zip_code int,
    person_type string,
    damage string,
    accidents_count int
)
row format delimited fields terminated by '\t' stored as textfile
location './output_mr3/';

create external table if not exists boroughs_ext (
    zip_code int,
    borough string
)
row format delimited fields terminated by ',' stored as textfile
location './input/datasource4/';

create view manhattan_injuries as
select a.street, a.person_type, sum(a.accidents_count) as injured from accidents_ext a inner join boroughs_ext b on a.zip_code = b.zip_code
where a.damage = 'injured' and b.borough = 'MANHATTAN' group by a.street, a.person_type;

create view manhattan_deaths as
select a.street, a.person_type, sum(a.accidents_count) as killed from accidents_ext a inner join boroughs_ext b on a.zip_code = b.zip_code
where a.damage = 'killed' and b.borough = 'MANHATTAN' group by a.street, a.person_type;

create external table if not exists manhattan_ext (
    street string,
    person_type string,
    killed int,
    injured int
)
row format delimited fields terminated by ',' stored as textfile
location './output6/';

create view manhattan as
    (select street, person_type, 0 as killed, injured from manhattan_injuries
    union all
    select street, person_type, killed, 0 as injured from manhattan_deaths);

(select street, person_type, sum(killed) as total_killed, sum(injured) as total_injured from manhattan
where person_type = 'pedestrian' group by street, person_type order by total_killed + total_injured desc limit 3)
union all
(select street, person_type, sum(killed) as total_killed, sum(injured) as total_injured from manhattan
where person_type = 'cyclist' group by street, person_type order by total_killed + total_injured desc limit 3)
union all
(select street, person_type, sum(killed) as total_killed, sum(injured) as total_injured from manhattan
where person_type = 'motorist' group by street, person_type order by total_killed + total_injured desc limit 3);