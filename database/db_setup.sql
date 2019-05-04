CREATE SCHEMA college;

CREATE TABLE college.school_info (
year integer,
id integer,
name VARCHAR(256),
city VARCHAR(256),
state VARCHAR(256),
school_url VARCHAR(256),
ownership integer,
region integer,
latitute float,
longitude float);


CREATE TABLE college.historical_demographics (
year integer,
id integer,
historically_black integer,
predominantly_black integer,
annh_serving integer,
tribal integer,
aanipi_serving integer,
histpanic integer,
nant integer,
men_only integer,
women_only integer,
religious_affiliation integer);

CREATE TABLE college.demographics (
year integer,
id integer,
size integer,
undergrad_size integer,
white float,
black float,
hispanic float,
asian float,
aian float,
nhpi float,
two_or_more float,
non_resident float,
unknown float
);

CREATE TABLE college.admissions (
year integer,
id integer,
admission_rate float,
sat_mid_reading float,
sat_mid_math float,
sat_mid_writing float,
sat_avg float,
act_mid_reading float,
act_mid_math float,
act_mid_writing float,
act_avg float);

CREATE TABLE college.degree_breakdown (
year integer,
id integer,
program varchar(256),
percent float);



