drop  database if exists SBRP;

create schema SBRP;
use SBRP;

-- ###### Department ######

CREATE TABLE Department (
  Department_ID int AUTO_INCREMENT,
  Department_Name varchar(50) NOT NULL,
PRIMARY KEY (Department_ID)
 );
 
INSERT INTO Department VALUES 
(1,'Corporate'),
(2,'Technology'),
(3, 'HR'),
(4, 'Accounting'),
(5, 'Marketing'),
(6, 'Finance'),
(7, 'Operations');

  -- ###### Job Function ######
 CREATE TABLE Job_Function (
  Job_Function_ID int AUTO_INCREMENT,
  Job_Function_Name varchar(50) NOT NULL,
 PRIMARY KEY (Job_Function_ID)
 );
 
INSERT INTO Job_Function VALUES 
(1,'Informaion Technology'),
(2,'Business Partnerships'),
(3, 'Strategy'),
(4, 'Marketing'),
(5, 'Operations')
;

 -- ###### Country ######
 CREATE TABLE Country (
  Country_ID int AUTO_INCREMENT,
  Country_Name varchar(50) NOT NULL,
 PRIMARY KEY (Country_ID)
 );
 
INSERT INTO Country VALUES 
(1,'Singapore'),
(2,'Malaysia'),
(3, 'Indonesia'),
(4, 'China'),
(5, 'Japan'),
(6, 'Hong Kong'),
(7, 'India');

-- ###### STAFF ######
CREATE TABLE Staff (
  Staff_ID int AUTO_INCREMENT,
  Staff_FName varchar(50) NOT NULL,
  Staff_LName varchar(50) NOT NULL,
  Department_ID int NOT NULL,
  Country_ID int NOT NULL,
  Email varchar(50) NOT NULL,
  Access_Rights int NOT NULL, -- 1 for HR, 2 for manager, 3 for staff?
  PRIMARY KEY (Staff_ID),
  CONSTRAINT Staff_fk1 FOREIGN KEY (Department_ID) REFERENCES Department(Department_ID),
  CONSTRAINT Staff_fk2 FOREIGN KEY (Country_ID) REFERENCES Country(Country_ID)
);

INSERT INTO Staff VALUES 
(1,'Jon','Tiong','1','1','jon.t@xyz.com', 2),
(2,'Matthew','Chang','4','2','matthew.c@xyz.com', 3),
(3,'Dexter','Ong','5','3','dexter.o@xyz.com', 2),
(4,'Leroy','Tham','3','6','leroy.t@xyz.com', 1),
(5,'Wei Sern','Tay','3','7','weisern.t@xyz.com', 1),
(6,'Jing','Chen','2','1','chenjing@xyz.com', 3)
;

CREATE TABLE Staff_HR (
	Staff_ID int NOT NULL,
    Access_Key varchar(20) NOT NULL,
    PRIMARY KEY (Staff_ID),
    CONSTRAINT Staff_HR_fk1 FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID)
    );
    
INSERT INTO Staff_HR VALUES 
(4,'AABB'),
(5,'CCCC');


CREATE TABLE Staff_Manager (
	Staff_ID int NOT NULL,
    Hiring_Code varchar(20) NOT NULL,
    PRIMARY KEY (Staff_ID),
    CONSTRAINT Staff_Manager_fk1 FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID)
    );
    
INSERT INTO Staff_Manager VALUES 
(1,'hello'),
(2,'happy');

-- ###### SKILLS ######
CREATE TABLE Skills (
Skill_ID int AUTO_INCREMENT, 
Skill_Name varchar(50) NOT NULL, 
PRIMARY KEY (Skill_ID)
);

INSERT INTO Skills VALUES -- separate into technical vs critical core skills? For now nvm because the LJPS data only has role and skill
(1,'Brand Management'),
(2,'Business Negotiation'),
(3, 'Stakeholder Management'),
(4, 'Python'),
(5, 'Cleaning')
;

-- ###### ROLES ######
CREATE TABLE Roles (
Role_ID int AUTO_INCREMENT, 
Role_Name varchar(50) NOT NULL, 
-- Role_desc varchar(1000) NOT NULL, (put it as optional for now because the role desc may change depending on the role-listing)
PRIMARY KEY (Role_ID)
);
INSERT INTO Roles VALUES 
(1,'Marketing Executive'),
(2,'Comms Executive'),
(3, 'Toilet Cleaner'),
(4, 'Janitor'),
(5, 'Admin Assistant')
;

-- ###### ROLE SKILL######
CREATE TABLE Role_Skill ( 
Role_ID int NOT NULL, -- we take in role_name and skill_name from the LJPS so we convert the skillname and role_name first with the corresponding id then we update this table
Skill_ID int NOT NULL, 
PRIMARY KEY (Role_ID,Skill_ID),
CONSTRAINT Role_Skill_fk1 FOREIGN KEY (Role_ID) REFERENCES Roles(Role_ID),
CONSTRAINT Role_Skill_fk2 FOREIGN KEY (Skill_ID) REFERENCES Skills(Skill_ID)
); 

INSERT INTO Role_Skill VALUES 
(1, 2),
(1, 1),
(1, 3),
(2, 1),
(2, 2),
(2, 3),
(3, 5),
(4, 5)
;

-- ###### ROLE Listing######
CREATE TABLE Role_Listing ( -- seems like it is taken from skills future so HR dont need to input their own skill??
  Role_Listing_ID int AUTO_INCREMENT,
  Role_ID int NOT NULL,
  Role_Desc varchar(1000) NOT NULL, -- desc depends on the listing
  Role_Department_ID int NOT NULL, 
  Role_Function_ID int NOT NULL, -- function is new and need to input is equivalent to the track for the skills future framework
  Role_Country_ID int NOT NULL, 
  Available BOOLEAN NOT NULL, -- 0 if not available ? Or juyst expiry_date enough and dunnid available as a field
  Expiry_Date DATE NOT NULL, -- expiry date can be null i think. Or should it be a new table cos it can change
  PRIMARY KEY (Role_Listing_ID),
  CONSTRAINT Role_Listing_fk1 FOREIGN KEY (Role_ID) REFERENCES Roles(Role_ID),
  CONSTRAINT Role_Listing_fk2 FOREIGN KEY (Role_Department_ID) REFERENCES Department(Department_ID),
  CONSTRAINT Role_Listing_fk3 FOREIGN KEY (Role_Country_ID) REFERENCES Country(Country_ID),
  CONSTRAINT Role_Listing_fk4 FOREIGN KEY (Role_Function_ID) REFERENCES Job_function(Job_Function_ID)
  
); 
INSERT INTO Role_Listing VALUES 
(1,1,'The marketing executive will be tasked to do xxxxx',5,4,3,1, "2023-12-31"),
(2,2,'The comms executive will be tasked to do xxxxx',5,2,2, 1, "2023-11-30"),
(3,4, 'The janitor is involved in cleaning up our trash',5,5,3,1, '2023-12-25'),
(4,5, 'Admin assitant will be involve in aadalskd alskvas oaisbdosia oaisbdaoi sdb oiabsfdosa ib ',7,5,6,1, '2023-10-05')
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

INSERT INTO Staff_Skill VALUES 
(1, 1, 0),
(1, 2, 5),
(1, 3, 5),
(1, 4, 0),
(2, 1, 3),
(2, 2, 0),
(3, 4, 2),
(3, 5, 1)
;

-- ###### Role_Listing_Skill######
CREATE TABLE Role_Listing_Skill_Proficiency ( -- HR will input a proficiency level for the skill for the role
Role_Listing_ID int NOT NULL,
Skill_ID int NOT NULL, 
Proficienct_Listing int NOT NULL, -- 1-4 from basic intermediate advanced expert.
PRIMARY KEY (Role_Listing_ID,Skill_ID),
CONSTRAINT Role_Listing_Skill_Proficiency_fk1 FOREIGN KEY (Role_Listing_ID) REFERENCES Role_Listing(Role_Listing_ID),
CONSTRAINT Role_Listing_Skill_Proficiency_fk2 FOREIGN KEY (Skill_ID) REFERENCES Role_Skill(Skill_ID)
);

INSERT INTO Role_Listing_Skill_Proficiency VALUES 
(1, 1, 3),
(1, 2, 3),
(1, 3, 3),
(2, 1, 2),
(2, 2, 4),
(2, 3, 2),
(3, 5, 4)
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
(1, 2, 3,1,CURRENT_TIMESTAMP),
(2, 2, 4,1,CURRENT_TIMESTAMP),
(3, 3, 1,1,CURRENT_TIMESTAMP),
(4, 3, 2,1,CURRENT_TIMESTAMP),
(5, 3, 3,1,CURRENT_TIMESTAMP),
(6, 4, 1,1,CURRENT_TIMESTAMP),
(7, 2, 1,1,CURRENT_TIMESTAMP),
(8, 3, 3,1,CURRENT_TIMESTAMP),
(9, 4, 1,1,CURRENT_TIMESTAMP),
(10, 6, 1,1,CURRENT_TIMESTAMP)
;

UPDATE Application SET Apply=0, Time_Stamp = CURRENT_TIMESTAMP WHERE Staff_ID= 2 AND Role_Listing_ID = 3;  


-- ###### Add extra skill in role (Not so important) ######
CREATE TABLE Extra_Skill ( -- staff can input x-factor skill
  Staff_ID int NOT NULL,
  Role_Listing_ID int NOT NULL,
  Skill_Name varchar(50) NOT NULL,
  Proficiency int NOT NULL, -- 1-4 from basic intermediate advanced expert
  PRIMARY KEY (Staff_ID, Role_Listing_ID, Skill_Name),
  CONSTRAINT Extra_Skill_fk1 FOREIGN KEY (Staff_ID) REFERENCES Application(Staff_ID),
  CONSTRAINT Extra_Skill_fk2 FOREIGN KEY (Role_Listing_ID) REFERENCES Application(Role_Listing_ID)
);

-- ###### Add role status (Not so important) ######
CREATE TABLE Role_Status ( -- HR Update Application Status can we combine with apply table? Assume 1 status at a time
Staff_ID int NOT NULL,
Role_Listing_ID int NOT NULL,
Status varchar(20) NOT NULL,
PRIMARY KEY (Staff_ID,Role_Listing_ID),
CONSTRAINT Role_Status_fk1 FOREIGN KEY (Staff_ID) REFERENCES Application(Staff_ID),
CONSTRAINT Role_Status_fk2 FOREIGN KEY (Role_Listing_ID) REFERENCES Application(Role_Listing_ID)
);
-- testing
select * from Staff;
select * from Role_Listing;
select * from Staff_Skill;
select * from Role_Listing_Skill_Proficiency;
select * from Application;

-- test jira link to github
-- test again demo




