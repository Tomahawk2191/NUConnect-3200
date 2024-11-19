DROP DATABASE IF EXISTS NUconnect;

CREATE DATABASE IF NOT EXISTS NUconnect;

USE NUconnect;

CREATE TABLE programs (
    programId INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR (100) NOT NULL UNIQUE,
    description (300),
    location (100) NOT NULL, 
    approved BOOLEAN DEFAULT false,
    schoolId INT,
    professorId INT,
    applicants JSON, #notnull?
    approvedApplicants JSON
    dateCreated DATETIME DEFAULT CURRENT_TIMESTAMP,
    programStart DATE,
    programEnd DATE;
    FOREIGN KEY (schoolId) REFERENCES school(schoolId),
    FOREIGN KEY (professorId) REFERENCES users(userId)
);

CREATE TABLE school (
    schoolId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL UNIQUE,
    programId INT,
    programs JSON, #notnull?
    students JSON,
    professors JSON,
    bio VARCHAR(300),
    #profilepic
    FOREIGN KEY (programId) REFERENCES programs(programId)
);

CREATE TABLE roles (
    roleId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    canPost BOOLEAN DEFAULT false,
    canApprove BOOLEAN DEFAULT false,
    canAssignProf BOOLEAN DEFAULT false,
    canApply BOOLEAN DEFAULT false,
    canRetract BOOLEAN DEFAULT false,
    canEditOwn BOOLEAN DEFAULT false,
    canEditAll BOOLEAN DEFAULT false,
    canDeleteOwn BOOLEAN DEFAULT false,
    canDeleteAll BOOLEAN DEFAULT false,
    canUpdateAccess BOOLEAN DEFAULT false
);

CREATE TABLE users (
    userId INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    middleName VARCHAR(50),
    lastName VARCHAR(50) NOT NULL,
    phone VARCHAR(15) UNIQUE,
    email VARCHAR(254) NOT NULL UNIQUE,
    schoolId INT,
    roleId INT,
    createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    lastLogin DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (schoolId) REFERENCES school(schoolId),
    FOREIGN KEY (roleId) REFERENCES roles(roleId)
);

CREATE TABLE userTags (
    userId INT,
    userTagId INT,
    FOREIGN KEY (userId) REFERENCES users(userId) 
	    ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (userTagId) REFERENCES userTagParent(userTagId) 
	    ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE userTagParent (
    userTagId INT AUTO_INCREMENT PRIMARY KEY,
    tagName VARCHAR(100),
    category VARCHAR(100)
);

CREATE TABLE profiles (
    profileId INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    middleName VARCHAR(50),
    lastName VARCHAR(50) NOT NULL,
    userId INT,
    schoolId INT,
    bio VARCHAR(300),
    #profilepic
    email VARCHAR(254) NOT NULL UNIQUE,
    userTagsArray JSON, #notnull?
    FOREIGN KEY (userId) REFERENCES users(userId),
    FOREIGN KEY (schoolId) REFERENCES programs(schoolId),
);

CREATE TABLE posts (
    postId INT AUTO_INCREMENT PRIMARY KEY,
    postAuthor VARCHAR(150) NOT NULL,
    title VARCHAR (100) NOT NULL,
    body VARCHAR (300),
    profileId INT,
    programId INT,
    #thumbnail,
    tags JSON, #notnull?
    published BOOLEAN DEFAULT false,
    favourited BOOLEAN DEFAULT false,
    applied BOOLEAN DEFAULT false,
    acceepted BOOLEAN DEFAULT false,
    createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    lastEdited DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (profileId) REFERENCES profiles(profileId),
    FOREIGN KEY (programId) REFERENCES programs(programId),
);

CREATE TABLE postTags (
    postId INT,
    postTagId INT,
    FOREIGN KEY (postId) REFERENCES posts(postId) 
	    ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (postTagId) REFERENCES postTagParent(postTagId) 
	    ON UPDATE cascade ON DELETE cascade,
);

CREATE TABLE postTagParent (
    postTagId INT AUTO_INCREMENT PRIMARY KEY,
    tagName VARCHAR(100),
    category VARCHAR(100),
);

INSERT INTO school (name, programs, professor) VALUES
('Boston University', JSON_ARRAY('CIEE Monteverde - Sustainability and the Environment', ' Mexico City: Gender and Migration'), JSON_ARRAY('Dr. Smith', 'Dr. Ron')),
('University of Southern California', JSON_ARRAY('Honors: Legal and philosophical perspectives on free speech and protest in France', 'Illegal Trade in Medical Products, Social Responsibility and Public Health'), JSON_ARRAY('Dr. Snow', 'Dr. Taylor'));

INSERT INTO roles (name, canEdit, canEditAll, canEditOwn, canDeleteOwn, canDeleteAll, canApprove, canAssign) VALUES
('Admin', TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE),
('Student', TRUE, FALSE, TRUE, TRUE, FALSE, FALSE, FALSE);

INSERT INTO users (firstName, middleName, lastName, phone, email, schoolId, roleId) VALUES
('Dao', 'Lain', 'Hope', '123-456-7890', 'Dao@example.edu', 1, 1),
('Ben', NULL, 'June', '555-555-5555', 'Ben@example.edu', 2, 2);

INSERT INTO userTags (userId) VALUES
(1),
(2);

INSERT INTO userTagParents (userTagId, tagName, category) VALUES
(1, 'Computer Science', 'Major'),
(2, '2027', 'Graduation Year');

INSERT INTO profiles (firstName, middleName, lastName, userId, bio, email, userTagsArray) VALUES
('Dao', 'Lain', 'Hope', 1, 'Software Engineer looking for a dialogue!', 'dao@example.com', JSON_ARRAY('Computer Science', '2027')),
('Ben', NULL, 'June', 2, 'Business Analyst specializing in market trends.', 'ben@example.com', JSON_ARRAY(NULL));

INSERT INTO programs (applicants, approve, programStart, programEnd, approvedApplicants) VALUES
(JSON_ARRAY('Dao', 'Ben'), TRUE, '2024-01-01', '2024-06-01', JSON_ARRAY('Alice')),
(JSON_ARRAY(), FALSE, '2024-02-01', '2024-07-01', JSON_ARRAY());

INSERT INTO posts (programId, postAuthor, tags, favorite, title, bodyText) VALUES
(1, 'Dr. Cooper', 'Computer Science', TRUE, 'Dialogue: The Mathematical Heritage of Hungary', JSON_OBJECT('content', 'This is an introduction to computer science courses.')),
(2, 'Lisa Smith', '2027', FALSE, 'Dialogue: The Chemistry of Green Energy in Iceland', JSON_OBJECT('content', 'Explore the world of finance and business opportunities in Iceland.'));

INSERT INTO postTags (postId) VALUES
(1),
(2);

INSERT INTO postTagParents (postTagId, postName, category) VALUES
(1, 'Summer 1', 'Time'),
(2, 'Computer Science', 'Major');
