DROP DATABASE IF EXISTS NUconnect;

CREATE DATABASE IF NOT EXISTS NUconnect;

USE NUconnect;

CREATE TABLE school
(
    schoolId INT AUTO_INCREMENT PRIMARY KEY,
    name     VARCHAR(200) NOT NULL UNIQUE,
    bio      VARCHAR(300)
);

CREATE TABLE role
(
    roleId          INT AUTO_INCREMENT PRIMARY KEY,
    name            VARCHAR(150) NOT NULL,
    canPost         BOOLEAN DEFAULT false,
    canApprove      BOOLEAN DEFAULT false,
    canAssignProf   BOOLEAN DEFAULT false,
    canApply        BOOLEAN DEFAULT false,
    canRetract      BOOLEAN DEFAULT false,
    canEditOwn      BOOLEAN DEFAULT false,
    canEditAll      BOOLEAN DEFAULT false,
    canDeleteOwn    BOOLEAN DEFAULT false,
    canDeleteAll    BOOLEAN DEFAULT false,
    canUpdateAccess BOOLEAN DEFAULT false
);

CREATE TABLE user
(
    userId     INT AUTO_INCREMENT PRIMARY KEY,
    firstName  VARCHAR(50)  NOT NULL,
    middleName VARCHAR(50),
    lastName   VARCHAR(50)  NOT NULL,
    phone      VARCHAR(17) UNIQUE,
    email      VARCHAR(254) NOT NULL UNIQUE,
    schoolId   INT,
    roleId     INT,
    createdAt  DATETIME DEFAULT CURRENT_TIMESTAMP,
    lastLogin  DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (schoolId) REFERENCES school (schoolId),
    FOREIGN KEY (roleId) REFERENCES role (roleId)
);

CREATE TABLE userTagParent
(
    userTagId INT AUTO_INCREMENT PRIMARY KEY,
    tagName   VARCHAR(100),
    category  VARCHAR(100)
);

CREATE TABLE userTag
(
    userId    INT NOT NULL,
    userTagId INT NOT NULL,
    FOREIGN KEY (userId) REFERENCES user (userId)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (userTagId) REFERENCES userTagParent (userTagId)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE profile
(
    profileId  INT AUTO_INCREMENT PRIMARY KEY,
    firstName  VARCHAR(50)  NOT NULL,
    middleName VARCHAR(50),
    lastName   VARCHAR(50)  NOT NULL,
    userId     INT,
    schoolId   INT,
    bio        VARCHAR(300),
    #profilepic
    email      VARCHAR(254) NOT NULL UNIQUE,
    FOREIGN KEY (userId) REFERENCES user (userId),
    FOREIGN KEY (schoolId) REFERENCES school (schoolId)
);

CREATE TABLE program
(
    programId    INT AUTO_INCREMENT PRIMARY KEY,
    title        VARCHAR(100) NOT NULL UNIQUE,
    description  VARCHAR(300),
    location     VARCHAR(100) NOT NULL,
    approved     BOOLEAN  DEFAULT false,
    awaiting     BOOLEAN  DEFAULT false,
    schoolId     INT,
    professorId  INT,
    dateCreated  DATETIME DEFAULT CURRENT_TIMESTAMP,
    programStart DATE,
    programEnd   DATE,
    FOREIGN KEY (schoolId) REFERENCES school (schoolId),
    FOREIGN KEY (professorId) REFERENCES user (userId)
);

CREATE TABLE post
(
    postId     INT AUTO_INCREMENT PRIMARY KEY,
    postAuthor VARCHAR(150) NOT NULL,
    title      VARCHAR(100) NOT NULL,
    body       VARCHAR(300),
    userId     INT,
    programId  INT,
    #thumbnail,
    published  BOOLEAN  DEFAULT false,
    favorited  BOOLEAN  DEFAULT false,
    createdAt  DATETIME DEFAULT CURRENT_TIMESTAMP,
    lastEdited DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (userId) REFERENCES user (userId),
    FOREIGN KEY (programId) REFERENCES program (programId)
);

CREATE TABLE postTagParent
(
    postTagId INT AUTO_INCREMENT PRIMARY KEY,
    tagName   VARCHAR(100),
    category  VARCHAR(100)
);

CREATE TABLE postTag
(
    postId    INT NOT NULL,
    postTagId INT NOT NULL,
    FOREIGN KEY (postId) REFERENCES post (postId)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (postTagId) REFERENCES postTagParent (postTagId)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE application
(
    applicationId INT AUTO_INCREMENT PRIMARY KEY,
    userId        INT,
    programId     INT,
    applied       BOOLEAN DEFAULT false,
    accepted      BOOLEAN DEFAULT false,
    denied        BOOLEAN DEFAULT false,
    FOREIGN KEY (userId) REFERENCES user (userId),
    FOREIGN KEY (programId) REFERENCES program (programId)
);

INSERT INTO school (name, bio)
VALUES ('Boston University',
        'Boston University is a private research university in Boston, Massachusetts, United States.'),
       ('University of Southern California',
        'The University of Southern California is a private research university in Los Angeles, California, United States.');

INSERT INTO role (name, canPost, canApprove, canAssignProf, canApply, canRetract, canEditOwn, canEditAll, canDeleteOwn, canDeleteAll, canUpdateAccess) VALUES
('Admin', TRUE, TRUE, TRUE, FALSE, FALSE, TRUE, TRUE, TRUE, TRUE, TRUE),
('Professor', TRUE, FALSE, TRUE, TRUE, TRUE, TRUE, FALSE, TRUE, FALSE, FALSE),
('Student', FALSE, FALSE, FALSE, TRUE, TRUE, TRUE, FALSE, TRUE, FALSE, FALSE);

INSERT INTO user (firstName, middleName, lastName, phone, email, schoolId, roleId)
VALUES ('Daniel', NULL, 'Smith', '098-765-4321', 'smith@example.edu', 1, 2),
       ('Weasley', 'Donald', 'Ron', '111-222-3456', 'ron@example.edu', 1, 2),
       ('White', 'Apple', 'Snow', '567-343-5678', 'snow@example.edu', 2, 2),
       ('Swift', NULL, 'Taylor', '345-222-3243', 'taylor@example.edu', 2, 2),
       ('Dao', 'Lain', 'Hope', '123-456-7890', 'dao@example.edu', 1, 3),
       ('Ben', NULL, 'June', '555-555-5555', 'ben@example.edu', 2, 3),
       ('Brown', 'Charlie', 'Alex', '444-333-2222', 'charlie@example.edu', 2, 2),
       ('Collins', 'Susan', 'Jade', '777-888-9999', 'jade@example.edu', 1, 3);

INSERT INTO userTagParent (tagName, category)
VALUES ('Computer Science', 'Major'),
       ('2027', 'Graduation Year'),
       ('Business', 'Curriculum');

INSERT INTO userTag (userId, userTagId)
VALUES (1, 1),
       (2, 2);

INSERT INTO profile (firstName, middleName, lastName, userId, schoolId, bio, email)
VALUES ('Daniel', NULL, 'Smith', 1, 1, 'Professor teaching Biology and is open to lead a dialogue',
        'smith@example.edu'),
       ('Weasley', 'Donald', 'Ron', 2, 1, 'Professor teaching Chemistry and is closed to leading a dialogue',
        'ron@example.edu'),
       ('White', 'Apple', 'Snow', 3, 2, 'An apple a day keeps the witch away', 'snow@example.edu'),
       ('Swift', NULL, 'Taylor', 4, 2, 'Does arena tours as a side hustle', 'taylor@example.edu'),
       ('Dao', 'Lain', 'Hope', 5, 1, 'Software Engineer looking for a dialogue!', 'dao@example.com'),
       ('Ben', NULL, 'June', 6, 2, 'Business Analyst specializing in market trends.', 'ben@example.com');

INSERT INTO program (title, location, schoolId, professorId, programStart, programEnd, approved, awaiting)
VALUES ('Dialogue: The Mathematical Heritage of Hungary', 'Hungary', 1, 1, '2024-01-01', '2024-06-01', TRUE, FALSE),
       ('Dialogue: The Chemistry of Green Energy in Iceland', 'Iceland', 2, 3, '2024-02-01', '2024-07-01', FALSE, TRUE);

INSERT INTO post (postAuthor, title, body, programId, userId, favorited)
VALUES ('Dr. Smith', 'Dialogue: The Mathematical Heritage of Hungary',
        'This is an introduction to computer science courses.', 1, 1, TRUE),
       ('White Apple Snow', 'Dialogue: The Chemistry of Green Energy in Iceland',
        'Explore the world of finance and business opportunities in Iceland.', 2, 3, FALSE);

INSERT INTO postTagParent (tagName, category)
VALUES ('Summer 1', 'Time'),
       ('Computer Science', 'Major');

INSERT INTO postTag (postId, postTagId)
VALUES (1, 1),
       (2, 2);

INSERT INTO application (userId, programId, applied, accepted, denied)
VALUES (1, 1, TRUE, FALSE, FALSE),
       (4, 2, TRUE, TRUE, FALSE);

# Persona 1: Student
#1.1
INSERT INTO application (userId, programId, applied, accepted, denied)
VALUES (5, 1, TRUE, FALSE, FALSE),
       (5, 2, TRUE, FALSE, FALSE);

#1.2
DELETE
FROM application
WHERE userId = 5
  AND programId = 1;

#1.3
INSERT INTO userTag (userId, userTagId)
VALUES (5, 1),
       (5, 2);

#1.4
INSERT INTO application (userId, programId, applied, accepted, denied)
VALUES (5, 1, TRUE, FALSE, FALSE),
       (5, 2, TRUE, TRUE, FALSE);

#1.5
INSERT INTO program (title, location, schoolId, professorId, programStart, programEnd)
VALUES ('Dialogue: Innovation in Artificial Intelligence', 'Singapore', 1, 2, '2024-05-01', '2024-08-01'),
       ('Dialogue: Sustainable Engineering Practices', 'Germany', 2, 3, '2024-06-01', '2024-09-01');

#1.6
UPDATE userTag
SET userTagId = (SELECT userTagId FROM userTagParent WHERE tagName = 'Computer Science')
WHERE userId = 5;

# Persona 2: Professor
#2.1
INSERT INTO program (title, location, schoolId, professorId, programStart, programEnd, approved, awaiting)
VALUES ('Dialogue: Data Ethics and Privacy', 'Ireland', 1, 1, '2024-04-01', '2024-08-01', FALSE, TRUE);

#2.2
DELETE
FROM program
WHERE professorId = 1
  AND title = 'Dialogue: Data Ethics and Privacy';

#2.3
UPDATE program
SET location    = 'Scotland',
    description = 'A hands-on program on AI ethics and social impact'
WHERE programId = 1
  AND professorId = 1;

#2.4
INSERT INTO application (userId, programId, applied, accepted, denied)
VALUES (6, 1, TRUE, FALSE, FALSE),
       (5, 1, TRUE, TRUE, FALSE);

#2.5
INSERT INTO application (userId, programId, applied, accepted, denied)
VALUES (1, 2, TRUE, FALSE, FALSE);

#2.6
UPDATE userTag
SET userTagId = (SELECT userTagId FROM userTagParent WHERE tagName = 'Business')
WHERE userId = 1;

# Persona 3: NU Administrator
#3.1
SELECT *
FROM program;

#3.2
DELETE
FROM post
WHERE body LIKE '%inappropriate content%';

#3.3
SELECT *
FROM user;

#3.4
UPDATE role
SET canAssignProf = TRUE
WHERE roleId = (SELECT roleId FROM role WHERE name = 'Professor');

#3.5
DELETE FROM user
WHERE firstName = 'Weasley' AND lastName = 'Ron';

#3.6
UPDATE program
SET description = 'Updated program details for new courses'
WHERE programId = 2;

# Persona 4: Outside University Administrator
#4.1
UPDATE program
SET approved = TRUE
WHERE programId = 1;

#4.2
INSERT INTO program (title, location, schoolId, professorId, programStart, programEnd, approved)
VALUES
    ('Dialogue: International Business Strategies', 'Japan', 2, 4, '2024-06-01', '2024-09-01', FALSE);

#4.3
UPDATE program
SET description = 'Travel to Greece and learn more about engineering'
WHERE programId = 2;

#4.4
UPDATE program
SET professorId = (SELECT userId FROM user WHERE email = 'jenni@example.edu')
WHERE programId = 2;

#4.5
SELECT lastName, middleName, firstName
FROM user
WHERE schoolId = 2;

#4.6
SELECT lastName, middleName, firstName
FROM user
         JOIN application a on user.userId = a.userId
WHERE schoolId = 2
  AND denied = true;