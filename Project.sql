DROP DATABASE IF EXISTS NUconnect;

CREATE DATABASE IF NOT EXISTS NUconnect;

USE NUconnect;

CREATE TABLE school (
    schoolId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL UNIQUE,
    bio VARCHAR(300)
    #profilepic
);

CREATE TABLE role (
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

CREATE TABLE user (
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
    FOREIGN KEY (roleId) REFERENCES role(roleId)
);

CREATE TABLE userTagParent (
    userTagId INT AUTO_INCREMENT PRIMARY KEY,
    tagName VARCHAR(100),
    category VARCHAR(100)
);

CREATE TABLE userTag (
    userId INT NOT NULL,
    userTagId INT NOT NULL,
    FOREIGN KEY (userId) REFERENCES user(userId)
	    ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (userTagId) REFERENCES userTagParent(userTagId) 
	    ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE profile (
    profileId INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    middleName VARCHAR(50),
    lastName VARCHAR(50) NOT NULL,
    userId INT,
    schoolId INT,
    bio VARCHAR(300),
    #profilepic
    email VARCHAR(254) NOT NULL UNIQUE,
    FOREIGN KEY (userId) REFERENCES user(userId),
    FOREIGN KEY (schoolId) REFERENCES school(schoolId)
);

CREATE TABLE program (
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
    FOREIGN KEY (professorId) REFERENCES user(userId)
);

CREATE TABLE post (
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
    FOREIGN KEY (profileId) REFERENCES profile(profileId),
    FOREIGN KEY (programId) REFERENCES program(programId)
);

CREATE TABLE postTagParent (
    postTagId INT AUTO_INCREMENT PRIMARY KEY,
    tagName VARCHAR(100),
    category VARCHAR(100)
);

CREATE TABLE postTag (
    postId INT NOT NULL,
    postTagId INT NOT NULL,
    FOREIGN KEY (postId) REFERENCES post(postId)
	    ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (postTagId) REFERENCES postTagParent(postTagId) 
	    ON UPDATE cascade ON DELETE cascade
);

INSERT INTO school (name, bio) VALUES
('Boston University', 'Boston University is a private research university in Boston, Massachusetts, United States.'),
('University of Southern California', 'The University of Southern California is a private research university in Los Angeles, California, United States.');

INSERT INTO role (name, canPost, canApprove, canAssignProf, canApply, canRetract, canEditOwn, canEditAll, canDeleteOwn, canDeleteAll, canUpdateAccess) VALUES
('Admin', TRUE, TRUE, TRUE, FALSE, FALSE, TRUE, TRUE, TRUE, TRUE, TRUE),
('Professor', TRUE, FALSE, FALSE, TRUE, TRUE, TRUE, FALSE, TRUE, FALSE, FALSE),
('Student', FALSE, FALSE, FALSE, TRUE, TRUE, TRUE, FALSE, TRUE, FALSE, FALSE);

INSERT INTO user (firstName, middleName, lastName, phone, email, schoolId, roleId) VALUES
('Dao', 'Lain', 'Hope', '123-456-7890', 'dao@example.edu', 1, 3),
('Ben', NULL, 'June', '555-555-5555', 'ben@example.edu', 2, 3),
('Daniel', NULL, 'Smith', '098-765-4321', 'smith@example.edu', 1, 2),
('Weasley', 'Donald', 'Ron', '111-222-3456', 'ron@example.edu', 1, 2),
('White', 'Apple', 'Snow', '567-343-5678', 'snow@example.edu', 2, 2),
('Swift', NULL, 'Taylor', '345-222-3243', 'taylor@example.edu', 2, 2);

INSERT INTO userTagParent (tagName, category) VALUES
('Computer Science', 'Major'),
('2027', 'Graduation Year');

INSERT INTO userTag (userId, userTagId) VALUES
(1, 1),
(2, 2);

INSERT INTO profile (firstName, middleName, lastName, userId, schoolId, bio, email) VALUES
('Dao', 'Lain', 'Hope', 1, 1,'Software Engineer looking for a dialogue!', 'dao@example.com'),
('Ben', NULL, 'June', 2, 2,'Business Analyst specializing in market trends.', 'ben@example.com'),
('Daniel', NULL, 'Smith', 3, 1, 'Professor teaching Biology and is open to lead a dialogue', 'smith@example.edu'),
('Weasley', 'Donald', 'Ron', 4, 1, 'Professor teaching Chemistry and is closed to leading a dialogue','ron@example.edu'),
('White', 'Apple', 'Snow', 5, 2, 'An apple a day keeps the witch away', 'snow@example.edu'),
('Swift', NULL, 'Taylor', 6, 2, 'Does arena tours as a side hustle', 'taylor@example.edu');

INSERT INTO program (title, location, schoolId, professorId, programStart, programEnd) VALUES
('Dialogue: The Mathematical Heritage of Hungary', 'Hungary', 1, 1, '2024-01-01', '2024-06-01'),
('Dialogue: The Chemistry of Green Energy in Iceland', 'Iceland', 2, 2, '2024-02-01', '2024-07-01');

INSERT INTO post (postAuthor, title, body, profileId, programId, favorited) VALUES
('Dr. Smith', 'Dialogue: The Mathematical Heritage of Hungary', 'This is an introduction to computer science courses.', 3, 1, TRUE),
('White Apple Snow', 'Dialogue: The Chemistry of Green Energy in Iceland', 'Explore the world of finance and business opportunities in Iceland.', 5, 2, FALSE);

INSERT INTO postTag (postId, postTagId) VALUES
(1, 1),
(2, 2);

INSERT INTO postTagParent (tagName, category) VALUES
('Summer 1', 'Time'),
('Computer Science', 'Major');
