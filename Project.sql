DROP DATABASE IF EXISTS NUconnect;

CREATE DATABASE IF NOT EXISTS NUconnect;

USE NUconnect;

CREATE TABLE school (
    schoolId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL UNIQUE,
    bio VARCHAR(300)
    #profilepic
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
    phone VARCHAR(17) UNIQUE,
    email VARCHAR(254) NOT NULL UNIQUE,
    schoolId INT,
    roleId INT,
    createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    lastLogin DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (schoolId) REFERENCES school(schoolId),
    FOREIGN KEY (roleId) REFERENCES roles(roleId)
);

CREATE TABLE programs (
    programId INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR (100) NOT NULL UNIQUE,
    description VARCHAR (300),
    location VARCHAR (100) NOT NULL,
    approved BOOLEAN DEFAULT false,
    schoolId INT,
    professorId INT,
    dateCreated DATETIME DEFAULT CURRENT_TIMESTAMP,
    programStart DATE,
    programEnd DATE,
    FOREIGN KEY (schoolId) REFERENCES school(schoolId),
    FOREIGN KEY (professorId) REFERENCES users(userId)
);

CREATE TABLE userTagParent (
    userTagId INT AUTO_INCREMENT PRIMARY KEY,
    tagName VARCHAR(100),
    category VARCHAR(100)
);

CREATE TABLE userTags (
    userId INT NOT NULL,
    userTagId INT NOT NULL,
    FOREIGN KEY (userId) REFERENCES users(userId) 
	    ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (userTagId) REFERENCES userTagParent(userTagId) 
	    ON UPDATE cascade ON DELETE cascade
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
    FOREIGN KEY (userId) REFERENCES users(userId),
    FOREIGN KEY (schoolId) REFERENCES school(schoolId)
);

CREATE TABLE posts (
    postId INT AUTO_INCREMENT PRIMARY KEY,
    postAuthor VARCHAR(150) NOT NULL,
    title VARCHAR (100) NOT NULL,
    body VARCHAR (300),
    profileId INT,
    programId INT,
    #thumbnail,
    published BOOLEAN DEFAULT false,
    favorited BOOLEAN DEFAULT false,
    applied BOOLEAN DEFAULT false,
    accepted BOOLEAN DEFAULT false,
    createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    lastEdited DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (profileId) REFERENCES profiles(profileId),
    FOREIGN KEY (programId) REFERENCES programs(programId)
);

CREATE TABLE postTagParent (
    postTagId INT AUTO_INCREMENT PRIMARY KEY,
    tagName VARCHAR(100),
    category VARCHAR(100)
);

CREATE TABLE postTags (
    postId INT NOT NULL,
    postTagId INT NOT NULL,
    FOREIGN KEY (postId) REFERENCES posts(postId) 
	    ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (postTagId) REFERENCES postTagParent(postTagId) 
	    ON UPDATE cascade ON DELETE cascade
);

INSERT INTO school (name, programs, professors) VALUES
('Boston University', JSON_ARRAY('CIEE Monteverde - Sustainability and the Environment', ' Mexico City: Gender and Migration'), JSON_ARRAY('Dr. Smith', 'Dr. Ron')),
('University of Southern California', JSON_ARRAY('Honors: Legal and philosophical perspectives on free speech and protest in France', 'Illegal Trade in Medical Products, Social Responsibility and Public Health'), JSON_ARRAY('Dr. Snow', 'Dr. Taylor'));

INSERT INTO roles (name, canPost, canApprove, canAssignProf, canApply, canRetract, canEditOwn, canEditAll, canDeleteOwn, canDeleteAll, canUpdateAccess) VALUES
('Admin', TRUE, TRUE, TRUE, FALSE, FALSE, TRUE, TRUE, TRUE, TRUE, TRUE),
('Professor', TRUE, FALSE, FALSE, TRUE, TRUE, TRUE, FALSE, TRUE, FALSE, FALSE),
('Student', FALSE, FALSE, FALSE, TRUE, TRUE, TRUE, FALSE, TRUE, FALSE, FALSE);

INSERT INTO users (firstName, middleName, lastName, phone, email, schoolId, roleId) VALUES
('Dao', 'Lain', 'Hope', '123-456-7890', 'dao@example.edu', 1, 3),
('Ben', NULL, 'June', '555-555-5555', 'ben@example.edu', 2, 3),
('Daniel', NULL, 'Smith', '098-765-4321', 'smith@example.edu', 1, 2),
('Weasley', 'Donald', 'Ron', '111-222-3456', 'ron@example.edu', 1, 2),
('White', 'Apple', 'Snow', '567-343-5678', 'snow@example.edu', 2, 2),
('Swift', NULL, 'Taylor', '345-222-3243', 'taylor@example.edu', 2, 2);

INSERT INTO programs (title, location, schoolId, professorId, applicants, approvedApplicants, programStart, programEnd) VALUES
('Dialogue: The Mathematical Heritage of Hungary', 'Hungary', 1, 1, JSON_ARRAY('Dao', 'Ben'), JSON_ARRAY('Alice'), '2024-01-01', '2024-06-01'),
('Dialogue: The Chemistry of Green Energy in Iceland', 'Iceland', 2, 2, JSON_ARRAY(), JSON_ARRAY(), '2024-02-01', '2024-07-01');

INSERT INTO userTagParent (tagName, category) VALUES
('Computer Science', 'Major'),
('2027', 'Graduation Year');

INSERT INTO userTags (userId, userTagId) VALUES
(1, 1),
(2, 2);

INSERT INTO profiles (firstName, middleName, lastName, userId, bio, email, userTagsArray) VALUES
('Dao', 'Lain', 'Hope', 1, 'Software Engineer looking for a dialogue!', 'dao@example.com', JSON_ARRAY('Computer Science', '2027')),
('Ben', NULL, 'June', 2, 'Business Analyst specializing in market trends.', 'ben@example.com', JSON_ARRAY(NULL));

INSERT INTO posts (postAuthor, title, body, profileId, programId, tags, favorited) VALUES
('Dr. Smith', 'Dialogue: The Mathematical Heritage of Hungary', 'This is an introduction to computer science courses.', 1, 1, JSON_OBJECT(1, ), TRUE),
('White Apple Snow', 'Dialogue: The Chemistry of Green Energy in Iceland', 'Explore the world of finance and business opportunities in Iceland.', 3, 2, JSON_OBJECT('content', '2027'), FALSE);

INSERT INTO postTags (postId, postTagId) VALUES
(1, 1),
(2, 2);

INSERT INTO postTagParent (tagName, category) VALUES
('Summer 1', 'Time'),
('Computer Science', 'Major');
