-- Question 2 BlogDB
DROP DATABASE IF EXISTS NUconnect;

CREATE DATABASE NUconnect;
USE NUconnect;

CREATE TABLE programs (
    programId INT AUTO_INCREMENT PRIMARY KEY,
    applicants JSON,
    approve boolean,
    dateCreated DATETIME DEFAULT CURRENT_TIMESTAMP,
    programStart DATE,
    programEnd DATE,
    approvedApplicants JSON);

CREATE TABLE posts (
    postId INT AUTO_INCREMENT PRIMARY KEY,
    programId INT,
    FOREIGN KEY (programId) REFERENCES programs(programId),
    postAuthor VARCHAR(150),
    tags VARCHAR(100),
    favorite boolean,
    title VARCHAR (200),
    bodyText JSON);

CREATE TABLE school (
    schoolId INT AUTO_INCREMENT PRIMARY KEY,
    programId INT,
    FOREIGN KEY (programId) REFERENCES programs(programId),
    programs JSON,
    name VARCHAR(200) NOT NULL UNIQUE,
    professor JSON);

CREATE TABLE roles (
    roleId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150),
    canEdit boolean,
    canEditAll boolean,
    canEditOwn boolean,
    canDeleteOwn boolean,
    canDeleteAll boolean,
    canApprove boolean,
    canAssign boolean);


CREATE TABLE users (
    userId INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    middleName VARCHAR(50),
    lastName VARCHAR(50)NOT NULL,
    phone VARCHAR(15),
    email VARCHAR(254)NOT NULL UNIQUE,
    schoolId INT,
    roleId INT,
    FOREIGN KEY (schoolId) REFERENCES school(schoolId),
    FOREIGN KEY (roleId) REFERENCES roles(roleId));

CREATE TABLE userTags (
    userTagId INT AUTO_INCREMENT PRIMARY KEY,
    userId INT,
    FOREIGN KEY (userId) REFERENCES users(userId) ON DELETE CASCADE);

CREATE TABLE userTagParents (
    tagName VARCHAR(100),
    category VARCHAR(100),
    userTagId INT,
    FOREIGN KEY (userTagId) REFERENCES userTags(userTagId) ON DELETE CASCADE);

CREATE TABLE profiles (
    profileId INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    middleName VARCHAR(50),
    lastName VARCHAR(50) NOT NULL,
    userId INT,
    FOREIGN KEY (userId) REFERENCES users(userId) ON DELETE CASCADE,
    bio VARCHAR(300),
    email VARCHAR(254) NOT NULL UNIQUE,
    userTagsArray JSON);

CREATE TABLE postTags (
    postTagId INT AUTO_INCREMENT PRIMARY KEY,
    postId INT,
    FOREIGN KEY (postId) REFERENCES posts(postId) ON DELETE CASCADE);

CREATE TABLE postTagParents (
    postName VARCHAR(100),
    category VARCHAR(100),
    postTagId INT,
    FOREIGN KEY (postTagId) REFERENCES postTags(postTagId) ON DELETE CASCADE);

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
