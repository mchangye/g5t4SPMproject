drop  database if exists SBRP;

create schema SBRP;
use SBRP;
-- not creating any log tables yet...
-- should i have a table just for skills and a table just for roles?? single column table?? 

-- ###### STAFF ######
CREATE TABLE Staff (
  Staff_ID int NOT NULL,
  Staff_FName varchar(50) NOT NULL,
  Staff_LName varchar(50) NOT NULL,
  Dept varchar(50) NOT NULL, -- foreign key??nah idts
  Country varchar(50) NOT NULL,
  Email varchar(50) NOT NULL,
  Access_Rights int NOT NULL, -- 1 for HR, 2 for manager, 3 for staff?
  PRIMARY KEY (Staff_ID)
);
INSERT INTO Staff VALUES 
(1,'Jon','Tiong','CEO','Singapore','jon.t@xyz.com', "2"),
(2,'Matthew','Chang','IT','Singapore','matthew.c@xyz.com', '3')
;

-- ###### SKILLS ######
CREATE TABLE Skills (
-- Skill_ID int NOT NULL, 
Skill_Name varchar(50) NOT NULL, 
PRIMARY KEY (Skill_Name)
);
INSERT INTO Skills VALUES 
('Brand Management'),
('Business Negotiation')
;

-- ###### ROLES ######
CREATE TABLE Roles (
-- Role_ID int NOT NULL, 
Role_Name varchar(50) NOT NULL, 
-- Role_desc varchar(1000) NOT NULL, (put it as optional for now because the role desc may change depending on the role-listing)
PRIMARY KEY (Role_Name)
);
INSERT INTO Roles VALUES 
('Marketing Executive'),
('Comms Executive')
;


CREATE TABLE Role_Skill (
Role_Name varchar(50) NOT NULL,
Skill_Name varchar(50) NOT NULL, 
PRIMARY KEY (Role_Name,Skill_Name),
CONSTRAINT Role_Skill_fk1 FOREIGN KEY (Role_Name) REFERENCES Roles(Role_Name),
CONSTRAINT Role_Skill_fk2 FOREIGN KEY (Skill_Name) REFERENCES Skills(Skill_Name)
); -- take from LJPS

INSERT INTO Role_Skill VALUES 
('Marketing Executive', 'Brand Management'),
('Marketing Executive', 'Business Negotiation'),
('Comms Executive', 'Brand Management')
;

CREATE TABLE Role_Listing ( -- seems like it is taken from skills future so HR dont need to input their own skill??
  Role_Listing_ID int NOT NULL,
  Role_Name varchar(50) NOT NULL,
  Role_Desc varchar(1000) NOT NULL, -- this will have to update the existing role table??
  Role_Department varchar(50) NOT NULL, 
  Role_Function varchar(50) NOT NULL, -- function is new and need to input is equivalent to the track for the skills future framework
  Role_Country varchar(50) NOT NULL, 
  Available BOOLEAN NOT NULL, -- 0 if not available ? Or juyst expiry_date enough and dunnid available as a field
  Expiry_Date DATE, -- expiry date can be null i think. Or should it be a new table cos it can change
  PRIMARY KEY (Role_Listing_ID),
  CONSTRAINT Role_Listing_fk2 FOREIGN KEY (Role_Name) REFERENCES Roles(Role_Name)
  
); 
INSERT INTO Role_Listing VALUES 
(1,'Marketing Executive','The marketing executive will be tasked to do xxxxx','Marketing','Business','Malaysia', "1", 2023-12-31),
(2,'Comms Executive','The comms executive will be tasked to do xxxxx','Comms','Business','Singapore', "1", 2023-11-31)
;

CREATE TABLE Staff_Skill ( -- staff can input their skill proficiency
  Staff_ID int NOT NULL,
  Skill_Name varchar(50) NOT NULL,
  Proficiency int NOT NULL, -- 1-3 from basic intermediate advanced staff need to populate this setting
  PRIMARY KEY (Staff_ID, Skill_Name),
  CONSTRAINT Staff_Skill_fk1 FOREIGN KEY (Skill_Name) REFERENCES Skills(Skill_Name),
  CONSTRAINT Staff_Skill_fk2 FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID)
);

CREATE TABLE Role_Skill_Proficiency ( -- HR will input a proficiency level for the skill for the role
Role_Listing_ID int NOT NULL,
Skill_Name varchar(50) NOT NULL, 
Proficienct_Listing int NOT NULL, -- 1-3 from basic intermediate advanced staff need to populate this setting
PRIMARY KEY (Role_Listing_ID,Skill_Name),
CONSTRAINT Role_Skill_Proficiency_fk1 FOREIGN KEY (Role_Listing_ID) REFERENCES Role_Listing(Role_Listing_ID),
CONSTRAINT Role_Skill_Proficiency_fk2 FOREIGN KEY (Skill_Name) REFERENCES Role_Skill(Skill_Name)
);

CREATE TABLE Apply_Role ( -- how do we make it so that you can unapply or just update apply field to 0 when unapply
Staff_ID int NOT NULL,
Role_Listing_ID int NOT NULL,
Apply BOOLEAN NOT NULL, -- not null? whether u apply or if u withdraw then status become 0
PRIMARY KEY (Staff_ID,Role_Listing_ID),
CONSTRAINT Apply_Role_fk1 FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID),
CONSTRAINT Apply_Role_fk2 FOREIGN KEY (Role_Listing_ID) REFERENCES Role_Listing(Role_Listing_ID)
);

CREATE TABLE Extra_Skill ( -- staff can input x-factor skill
  Staff_ID int NOT NULL,
  Role_Listing_ID int NOT NULL,
  Skill_Name varchar(50) NOT NULL,
  Proficiency int NOT NULL, -- 1-3 from basic intermediate advanced staff need to populate this setting
  PRIMARY KEY (Staff_ID, Role_Listing_ID, Skill_Name),
  CONSTRAINT Extra_Skill_fk1 FOREIGN KEY (Staff_ID) REFERENCES Apply_Role(Staff_ID),
  CONSTRAINT Extra_Skill_fk2 FOREIGN KEY (Role_Listing_ID) REFERENCES Apply_Role(Role_Listing_ID)
);

CREATE TABLE Role_Status ( -- HR Update Application Status can we combine with apply table? Assume 1 status at a time
Staff_ID int NOT NULL,
Role_Listing_ID int NOT NULL,
Status varchar(20) NOT NULL,
PRIMARY KEY (Staff_ID,Role_Listing_ID),
CONSTRAINT Role_Status_fk1 FOREIGN KEY (Staff_ID) REFERENCES Apply_Role(Staff_ID),
CONSTRAINT Role_Status_fk2 FOREIGN KEY (Role_Listing_ID) REFERENCES Apply_Role(Role_Listing_ID)
);





