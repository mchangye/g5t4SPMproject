SET GLOBAL LOCAL_INFILE=TRUE;
drop  database if exists SBRP;

create schema SBRP;
use SBRP;

-- ###### Department ######

CREATE TABLE Department (
  Department_ID int AUTO_INCREMENT,
  Department_Name varchar(50) NOT NULL,
PRIMARY KEY (Department_ID)
 );
 
drop table if exists department_temp;
CREATE TEMPORARY TABLE department_temp (
	Department_ID int AUTO_INCREMENT PRIMARY KEY,
    Department_Name varchar(50)
);

LOAD DATA LOCAL INFILE "C:/Users/Dexter/Documents/GitHub/g5t4SPMproject/Database/Sample_Data/staff.csv" INTO TABLE department_temp 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES
(@dummy,@dummy,@dummy,@dept) set Department_Name = @dept ;

INSERT Department(Department_Name) SELECT DISTINCT Department_Name FROM department_temp;
drop table if exists department_temp;

 -- ###### Country ######
 CREATE TABLE Country (
  Country_ID int AUTO_INCREMENT,
  Country_Name varchar(50) NOT NULL,
 PRIMARY KEY (Country_ID)
 );
 drop table if exists country_temp;
 CREATE TEMPORARY TABLE country_temp (
	Country_ID int AUTO_INCREMENT PRIMARY KEY,
    Country_Name varchar(50)
);

LOAD DATA LOCAL INFILE "C:/Users/Dexter/Documents/GitHub/g5t4SPMproject/Database/Sample_Data/staff.csv" INTO TABLE country_temp 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES
(@dummy,@dummy,@dummy,@dummy, @Country) set Country_Name = @Country ;

-- select * from country_unique;

INSERT Country(Country_Name) SELECT DISTINCT Country_Name FROM Country_temp;
drop table if exists department_unique;
-- select * from Country;

-- ###### Access Rights ###### 
CREATE TABLE Access_Rights (
Access_ID int NOT NULL, -- 1 for Admin, 2 for User, 3 for Manager, 4 for HR
Access_Control_Name varchar(50) NOT NULL,
PRIMARY KEY (Access_ID)
);

LOAD DATA LOCAL INFILE "C:/Users/Dexter/Documents/GitHub/g5t4SPMproject/Database/Sample_Data/Access_Control.csv" INTO TABLE Access_Rights 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;

-- ###### STAFF ######
CREATE TABLE Staff (
  Staff_ID int AUTO_INCREMENT,
  Staff_FName varchar(50) NOT NULL,
  Staff_LName varchar(50) NOT NULL,
  Department_ID int NOT NULL,
  Country_ID int NOT NULL,
  Email varchar(50) NOT NULL,
  Access_ID int NOT NULL, -- 1 for Admin, 2 for User, 3 for Manager, 4 for HR
  PRIMARY KEY (Staff_ID),
  CONSTRAINT Staff_fk1 FOREIGN KEY (Department_ID) REFERENCES Department(Department_ID),
  CONSTRAINT Staff_fk2 FOREIGN KEY (Country_ID) REFERENCES Country(Country_ID),
  CONSTRAINT Staff_fk3 FOREIGN KEY (Access_ID) references Access_Rights(Access_ID)
);

drop table if exists staff_temp;
CREATE TEMPORARY TABLE staff_temp (
Staff_ID int NOT NULL,
  Staff_FName varchar(50) NOT NULL,
  Staff_LName varchar(50) NOT NULL,
  Department_Name varchar(50) NOT NULL,
  Country_Name varchar(50) NOT NULL,
  Email varchar(50) NOT NULL,
  Access_ID int NOT NULL, -- 1 for Admin, 2 for User, 3 for Manager, 4 for HR
  PRIMARY KEY (Staff_ID)
);

LOAD DATA LOCAL INFILE "C:/Users/Dexter/Documents/GitHub/g5t4SPMproject/Database/Sample_Data/staff.csv" INTO TABLE staff_temp 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;

select * from staff_temp;
UPDATE staff_temp
INNER JOIN Department ON staff_temp.Department_Name = Department.Department_Name
SET staff_temp.Department_Name = Department.Department_ID;

UPDATE staff_temp
INNER JOIN Country ON staff_temp.Country_Name = Country.Country_Name
SET staff_temp.Country_Name = Country.Country_ID;

-- select * from country;
-- select * from department;
-- select * from staff_temp;

INSERT INTO Staff
SELECT * FROM Staff_temp;
drop table if exists Staff_temp;

-- select * from Staff;

-- ###### SKILLS ######
CREATE TABLE Skills (
Skill_ID int AUTO_INCREMENT, 
Skill_Name varchar(50) NOT NULL, 
Skill_Desc varchar(1000) NOT NULL, 
PRIMARY KEY (Skill_ID)
);

LOAD DATA LOCAL INFILE "C:/Users/Dexter/Documents/GitHub/g5t4SPMproject/Database/Sample_Data/skill.csv" INTO TABLE Skills character set latin1
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES
(@Skill_Name,@Skill_Desc) set Skill_Name = @Skill_Name, Skill_Desc = @Skill_Desc;

-- select * from Skills;

-- ###### ROLES ######
CREATE TABLE Roles (
Role_ID int AUTO_INCREMENT, 
Role_Name varchar(50) NOT NULL, 
Role_Desc varchar(10000) NOT NULL, 
PRIMARY KEY (Role_ID)
);

LOAD DATA LOCAL INFILE "C:/Users/Dexter/Documents/GitHub/g5t4SPMproject/Database/Sample_Data/role.csv" INTO TABLE Roles character set latin1
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES
(@Role_Name,@Role_Desc) set Role_Name = @Role_Name, Role_Desc = @Role_Desc;

-- select * from Roles;

-- ###### ROLE SKILL######
CREATE TABLE Role_Skill ( 
Role_ID int NOT NULL, -- we take in role_name and skill_name from the LJPS so we convert the skillname and role_name first with the corresponding id then we update this table
Skill_ID int NOT NULL, 
PRIMARY KEY (Role_ID,Skill_ID),
CONSTRAINT Role_Skill_fk1 FOREIGN KEY (Role_ID) REFERENCES Roles(Role_ID),
CONSTRAINT Role_Skill_fk2 FOREIGN KEY (Skill_ID) REFERENCES Skills(Skill_ID)
); 

drop table if exists role_skill_temp;
CREATE TEMPORARY TABLE role_skill_temp (
role_name varchar(50) NOT NULL,
skill_name varchar(50) NOT NULL,
PRIMARY KEY (role_name, skill_name)
);

LOAD DATA LOCAL INFILE "C:/Users/Dexter/Documents/GitHub/g5t4SPMproject/Database/Sample_Data/role_skill.csv" INTO TABLE role_skill_temp
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;

-- select * from role_skill_temp;

UPDATE role_skill_temp
INNER JOIN Roles ON role_skill_temp.role_name = Roles.Role_Name
SET role_skill_temp.role_name = Roles.Role_ID;

UPDATE role_skill_temp
INNER JOIN Skills ON role_skill_temp.skill_name = Skills.Skill_Name
SET role_skill_temp.skill_name = Skills.Skill_ID;

-- select * from role_skill_temp;
-- select * from roles;
-- select * from skills;
-- select * from Role_Skill;

INSERT INTO Role_Skill
SELECT * FROM role_skill_temp;
drop table if exists role_skill_temp;

-- select * from Role_Skill;

-- ###### ROLE Listing######
CREATE TABLE Role_Listing ( -- seems like it is taken from skills future so HR dont need to input their own skill??
  Role_Listing_ID int AUTO_INCREMENT,
  Role_ID int NOT NULL,
  Role_Listing_Desc varchar(1000) NOT NULL,
  Role_Department_ID int NOT NULL, 
  Role_Country_ID int NOT NULL, 
  Available BOOLEAN NOT NULL, -- 0 if not available ? Or juyst expiry_date enough and dunnid available as a field
  Expiry_Date DATE NOT NULL, -- expiry date can be null i think. Or should it be a new table cos it can change
  PRIMARY KEY (Role_Listing_ID),
  CONSTRAINT Role_Listing_fk1 FOREIGN KEY (Role_ID) REFERENCES Roles(Role_ID),
  CONSTRAINT Role_Listing_fk2 FOREIGN KEY (Role_Department_ID) REFERENCES Department(Department_ID),
  CONSTRAINT Role_Listing_fk3 FOREIGN KEY (Role_Country_ID) REFERENCES Country(Country_ID)
); 
INSERT INTO Role_Listing VALUES 
(1,1,'The account manager acts as a ....',5,3,1, "2023-12-31"),
(2,2,'Admin executive will xxxxx',5,5,1, "2023-11-30"),
(3,5, 'Consultant will be xxxx',5,1,1, '2023-12-25'),
(4,6, 'The developer in this team will be involved in ....',9,1,1, '2023-10-05')
;

-- ###### Staff Skill######
CREATE TABLE Staff_Skill ( -- staff can input their skill proficiency
  Staff_ID int NOT NULL,
  Skill_ID int NOT NULL, 
  Proficiency int NOT NULL, -- 1-4 from basic intermediate advanced expert.  0 if never update. Default is 0.
  PRIMARY KEY (Staff_ID, Skill_ID),
  CONSTRAINT Staff_Skill_fk1 FOREIGN KEY (Skill_ID) REFERENCES Skills(Skill_ID),
  CONSTRAINT Staff_Skill_fk2 FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID)
);

drop table if exists staff_skill_temp;
CREATE TEMPORARY TABLE staff_skill_temp (
staff_id int NOT NULL,
skill_name varchar(50) NOT NULL,
PRIMARY KEY (staff_id, skill_name)
);

LOAD DATA LOCAL INFILE "C:/Users/Dexter/Documents/GitHub/g5t4SPMproject/Database/Sample_Data/staff_skill.csv" INTO TABLE staff_skill_temp
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;

UPDATE staff_skill_temp
INNER JOIN Skills ON staff_skill_temp.skill_name = Skills.Skill_Name
SET staff_skill_temp.skill_name = Skills.Skill_ID;

ALTER TABLE staff_skill_temp
ADD Proficiency int NOT NULL;
select * from staff_skill_temp;

INSERT INTO Staff_Skill
SELECT * FROM staff_skill_temp;
drop table if exists staff_skill_temp;

-- select * from Staff_Skill;

-- ###### Role_Listing_Skill######
CREATE TABLE Role_Listing_Skill_Proficiency ( -- HR will input a proficiency level for the skill for the role
Role_Listing_ID int NOT NULL,
Role_ID int NOT NULL,
Skill_ID int NOT NULL, 
Proficienct_Listing int NOT NULL, -- 1-4 from basic intermediate advanced expert.
PRIMARY KEY (Role_Listing_ID,Role_ID,Skill_ID),
CONSTRAINT Role_Listing_Skill_Proficiency_fk1 FOREIGN KEY (Role_Listing_ID) REFERENCES Role_Listing(Role_Listing_ID),
CONSTRAINT Role_Listing_Skill_Proficiency_fk2 FOREIGN KEY (Role_ID) REFERENCES Role_Skill(Role_ID),
CONSTRAINT Role_Listing_Skill_Proficiency_fk3 FOREIGN KEY (Skill_ID) REFERENCES Role_Skill(Skill_ID)
);

INSERT INTO Role_Listing_Skill_Proficiency VALUES 
(1,1,1, 3),
(1,1, 10, 3),
(1,1,12, 3),
(1,1,14, 2),
(1,1,15, 2),
(1,1,20, 2),
(1,1,21, 3),
(1,1,25, 1),
(1,1,51, 3),
(1,1,53, 3),
(1,1,54, 3),
(1,1,61, 3),
(1,1,72, 3),
(2,2,20, 4),
(2,2,21, 3),
(2,2,24, 4),
(2,2,53, 2),
(2,2,70, 1),
(2,2,72, 1),
(2,2,79, 1),
(3,5, 1, 4),
(3,5, 12, 4),
(3,5, 14, 2),
(3,5, 20, 3),
(3,5, 21, 1),
(3,5, 25, 2),
(3,5, 52, 1),
(3,5, 53, 1),
(3,5, 54, 4),
(3,5, 56, 4),
(3,5, 72, 4),
(4,6,4,4),
(4,6,5,4),
(4,6,6,4),
(4,6,13,3),
(4,6,14,2),
(4,6,17,1),
(4,6,18,1),
(4,6,20,1),
(4,6,21,4),
(4,6,22,3),
(4,6,26,2),
(4,6,52,4),
(4,6,53,1),
(4,6,54,2),
(4,6,56,3),
(4,6,66,2),
(4,6,67,4),
(4,6,68,3),
(4,6,69,1),
(4,6,72,1),
(4,6,74,1),
(4,6,81,4)
;

-- ###### APPLICATION ######
CREATE TABLE Application ( -- how do we make it so that you can unapply or just update apply field to 0 when unapply
Application_ID int AUTO_INCREMENT,
Staff_ID int NOT NULL,
Role_Listing_ID int NOT NULL,
Apply BOOLEAN NOT NULL, -- not null? whether u apply or if u withdraw then status become 0. Each time you apply/ unapply it is a new value
Time_Stamp datetime NOT NULL,
PRIMARY KEY (Application_ID),
CONSTRAINT Application_fk1 FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID),
CONSTRAINT Application_fk2 FOREIGN KEY (Role_Listing_ID) REFERENCES Role_Listing(Role_Listing_ID)
);

INSERT INTO Application VALUES 
(1, 140889, 3,1,CURRENT_TIMESTAMP),
(2, 140004, 4,1,CURRENT_TIMESTAMP),
(3, 140004, 1,1,CURRENT_TIMESTAMP),
(4, 140025, 2,1,CURRENT_TIMESTAMP),
(5, 151407, 3,1,CURRENT_TIMESTAMP),
(6, 151410, 1,1,CURRENT_TIMESTAMP),
(7, 151410, 1,1,CURRENT_TIMESTAMP),
(8, 151410, 3,1,CURRENT_TIMESTAMP),
(9, 151533, 1,1,CURRENT_TIMESTAMP),
(10, 151534, 1,1,CURRENT_TIMESTAMP)
;

UPDATE Application SET Apply=0, Time_Stamp = CURRENT_TIMESTAMP WHERE Staff_ID= 2 AND Role_Listing_ID = 3;  


-- ###### Add extra skill in role (Not so important) ######
-- CREATE TABLE Extra_Skill ( -- staff can input x-factor skill
--   Staff_ID int NOT NULL,
--   Role_Listing_ID int NOT NULL,
--   Skill_Name varchar(50) NOT NULL,
--   Proficiency int NOT NULL, -- 1-4 from basic intermediate advanced expert
--   PRIMARY KEY (Staff_ID, Role_Listing_ID, Skill_Name),
--   CONSTRAINT Extra_Skill_fk1 FOREIGN KEY (Staff_ID) REFERENCES Application(Staff_ID),
--   CONSTRAINT Extra_Skill_fk2 FOREIGN KEY (Role_Listing_ID) REFERENCES Application(Role_Listing_ID)
-- );

-- ###### Add role status (Not so important) ######
-- CREATE TABLE Role_Status ( -- HR Update Application Status can we combine with apply table? Assume 1 status at a time
-- Staff_ID int NOT NULL,
-- Role_Listing_ID int NOT NULL,
-- Status varchar(20) NOT NULL,
-- PRIMARY KEY (Staff_ID,Role_Listing_ID),
-- CONSTRAINT Role_Status_fk1 FOREIGN KEY (Staff_ID) REFERENCES Application(Staff_ID),
-- CONSTRAINT Role_Status_fk2 FOREIGN KEY (Role_Listing_ID) REFERENCES Application(Role_Listing_ID)
-- );

-- testing
select * from Staff;
select * from Role_Listing;
select * from Staff_Skill;
select * from Role_Listing_Skill_Proficiency;
select * from Application;






