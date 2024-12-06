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
    canPost         BOOLEAN DEFAULT False,
    canApprove      BOOLEAN DEFAULT False,
    canAssignProf   BOOLEAN DEFAULT False,
    canApply        BOOLEAN DEFAULT False,
    canRetract      BOOLEAN DEFAULT False,
    canEditOwn      BOOLEAN DEFAULT False,
    canEditAll      BOOLEAN DEFAULT False,
    canDeleteOwn    BOOLEAN DEFAULT False,
    canDeleteAll    BOOLEAN DEFAULT False,
    canUpdateAccess BOOLEAN DEFAULT False
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
    FOREIGN KEY (schoolId) REFERENCES school (schoolId)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (roleId) REFERENCES role (roleId)
        ON UPDATE cascade ON DELETE restrict
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
    FOREIGN KEY (userId) REFERENCES user (userId)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (schoolId) REFERENCES school (schoolId)
        ON UPDATE cascade ON DELETE restrict
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
    FOREIGN KEY (schoolId) REFERENCES school (schoolId)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (professorId) REFERENCES user (userId)
        ON UPDATE cascade ON DELETE restrict
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
    -- published  BOOLEAN  DEFAULT false,
    -- favorited  BOOLEAN  DEFAULT false,
    createdAt  DATETIME DEFAULT CURRENT_TIMESTAMP,
    lastEdited DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (userId) REFERENCES user (userId)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (programId) REFERENCES program (programId)
        ON UPDATE cascade ON DELETE cascade
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
    FOREIGN KEY (userId) REFERENCES user (userId)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (programId) REFERENCES program (programId)
        ON UPDATE cascade ON DELETE cascade
);


INSERT INTO school (name, bio)
VALUES ('Boston University',
        'Boston University is a private research university in Boston, Massachusetts, United States.'),
       ('University of Southern California',
        'The University of Southern California is a private research university in Los Angeles, California, United States.');
insert into school (name, bio)
values ('Fashion Institute of New York', 'Pre-emptive');
insert into school (name, bio)
values ('Dijla University College', 'foreground');
insert into school (name, bio)
values ('Universidad Autónoma Juan Misael Saracho', 'modular');
insert into school (name, bio)
values ('Muscat College', 'contingency');
insert into school (name, bio)
values ('Kansai University', 'time-frame');
insert into school (name, bio)
values ('Mozyr State Pedagogical Institute', 'Implemented');
insert into school (name, bio)
values ('Acharya Nagarjuna University', 'fault-tolerant');
insert into school (name, bio)
values ('Universität Liechtenstein', 'disintermediate');
insert into school (name, bio)
values ('Universidade Salvador', 'Profound');
insert into school (name, bio)
values ('Universidad San Francisco Xavier de Chuquisaca', 'knowledge base');
insert into school (name, bio)
values ('University of Virginia, College at Wise', 'contextually-based');
insert into school (name, bio)
values ('Alice-Salomon-Fachhochschule für Sozialarbeit und Sozialpädagogik Berlin', 'Re-contextualized');
insert into school (name, bio)
values ('Internationale Fachhochschule Bad Honnef', 'Open-architected');
insert into school (name, bio)
values ('Universidad de la Tercera Edad', 'Persistent');
insert into school (name, bio)
values ('Universidad Nacional de Tumbes', 'composite');
insert into school (name, bio)
values ('Canadian College of Business & Computers', 'model');
insert into school (name, bio)
values ('Bhagwant University', 'ability');
insert into school (name, bio)
values ('Taoist College Singapore', 'foreground');
insert into school (name, bio)
values ('Universidad Latinoamericana', 'Digitized');
insert into school (name, bio)
values ('Rajshahi University of Engineering and Technology', 'Profit-focused');
insert into school (name, bio)
values ('Strayer University', 'alliance');
insert into school (name, bio)
values ('University of Alabama - Birmingham', 'collaboration');
insert into school (name, bio)
values ('Fourah Bay College, University of Sierra Leone', 'Streamlined');
insert into school (name, bio)
values ('Universidad Nacional de San Juan', '3rd generation');
insert into school (name, bio)
values ('Fukuoka Prefectural University', 'Universal');
insert into school (name, bio)
values ('Caucasus University', 'Robust');
insert into school (name, bio)
values ('Kabul Medical University', 'attitude');
insert into school (name, bio)
values ('Warsaw School of Information Technology', 'real-time');
insert into school (name, bio)
values ('Saigon University', 'radical');
insert into school (name, bio)
values ('Emanuel University', 'global');
insert into school (name, bio)
values ('Nigerian Turkish Nile University', 'leading edge');
insert into school (name, bio)
values ('Rochester Institute of Technology', 'Programmable');
insert into school (name, bio)
values ('Brigham Young University Hawaii', 'Team-oriented');
insert into school (name, bio)
values ('Universidad de Salamanca', 'model');
insert into school (name, bio)
values ('Technische Universität Berlin', 'workforce');
insert into school (name, bio)
values ('Ecole Nationale Vétérinaire de Lyon', 'Integrated');
insert into school (name, bio)
values ('Daffodil International University', 'support');
insert into school (name, bio)
values ('Life University', 'bandwidth-monitored');
insert into school (name, bio)
values ('Delta State University', 'exuding');
insert into school (name, bio)
values ('Crawford University ', 'Focused');
insert into school (name, bio)
values ('National Military Academy of Afghanistan', 'eco-centric');
insert into school (name, bio)
values ('Western Kentucky University', 'Programmable');
insert into school (name, bio)
values ('Ecole Supérieure d''Optique', 'tangible');
insert into school (name, bio)
values ('Escuela Bancaria y Comercial', 'composite');
insert into school (name, bio)
values ('Université Louis Pasteur (Strasbourg I)', 'focus group');
insert into school (name, bio)
values ('Southeastern Oklahoma State University', 'Optimized');
insert into school (name, bio)
values ('Wofford College', 'clear-thinking');
insert into school (name, bio)
values ('Universidad Chileno Britanica de Cultura', 'local');
insert into school (name, bio)
values ('Gebze Institute of Technology', 'coherent');
insert into school (name, bio)
values ('Institute of Teachers Education, Malay Language', 'intranet');
insert into school (name, bio)
values ('Gaborone Universal College of Law', 'systematic');
insert into school (name, bio)
values ('Al Fashir University', 'firmware');
insert into school (name, bio)
values ('Universite des Sciences Islamiques de Constantine', 'Open-architected');
insert into school (name, bio)
values ('University of Exeter', 'attitude-oriented');
insert into school (name, bio)
values ('National Aviation Univesity', 'stable');
insert into school (name, bio)
values ('Morehouse College', '24/7');
insert into school (name, bio)
values ('Samara State University of Economics', 'intranet');
insert into school (name, bio)
values ('Semey State Medical University', 'Customizable');
insert into school (name, bio)
values ('Shimane University', 'software');
insert into school (name, bio)
values ('Universitas Ngurah Rai', 'coherent');
insert into school (name, bio)
values ('Pacific University', 'Inverse');
insert into school (name, bio)
values ('Universidad Empresarial Siglio 21', 'logistical');
insert into school (name, bio)
values ('Universidad Ciencias Comerciales', 'Total');
insert into school (name, bio)
values ('Université du Québec à Rimouski', 'Function-based');
insert into school (name, bio)
values ('AgroParisTech', 'Polarised');
insert into school (name, bio)
values ('Shiraz University of Medical Sciences', 'Cloned');
insert into school (name, bio)
values ('Fachhochschule Köln', 'firmware');
insert into school (name, bio)
values ('Universität Stuttgart', 'methodology');
insert into school (name, bio)
values ('Université du Sahel', 'hybrid');
insert into school (name, bio)
values ('Hogere Zeevaartschool - Maritime Academy', 'project');
insert into school (name, bio)
values ('Toyama Medical and Pharmaceutical University', 'paradigm');
insert into school (name, bio)
values ('University of Idaho', 'Object-based');
insert into school (name, bio)
values ('Institute of Teachers Education, Tengku Ampuan Afzan', 'User-centric');
insert into school (name, bio)
values ('Bicol University', 'tertiary');
insert into school (name, bio)
values ('Nihon University', 'directional');
insert into school (name, bio)
values ('Utrecht University', 'multimedia');
insert into school (name, bio)
values ('Barton College', 'fault-tolerant');
insert into school (name, bio)
values ('Université d''Evry Val d''Essonne', 'firmware');
insert into school (name, bio)
values ('University of Science and Culture', 'Object-based');
insert into school (name, bio)
values ('Ural State Forestry Technical Academy', 'middleware');
insert into school (name, bio)
values ('The American College', 'Graphic Interface');
insert into school (name, bio)
values ('Addis Ababa University', 'systemic');
insert into school (name, bio)
values ('Heidelberg College', 'Digitized');
insert into school (name, bio)
values ('Kinjo Gakuin University', 'coherent');
insert into school (name, bio)
values ('Gifu University', 'human-resource');
insert into school (name, bio)
values ('Universiteit Antwerpen, UFSIA', 'pricing structure');
insert into school (name, bio)
values ('Amravati University', 'analyzer');
insert into school (name, bio)
values ('University of Health Sciences', 'cohesive');
insert into school (name, bio)
values ('Namik Kemal University', 'Vision-oriented');
insert into school (name, bio)
values ('Mills Grae University', 'Synchronised');
insert into school (name, bio)
values ('Indian Institute of Information Technology and Management - Kerala', 'budgetary management');
insert into school (name, bio)
values ('Ulyanovsk State Agricultural Academy', 'motivating');
insert into school (name, bio)
values ('Union College Nebraska', 'Business-focused');
insert into school (name, bio)
values ('University of Oxford', 'Profound');
insert into school (name, bio)
values ('Academy of Public Administration of Belarus', 'frame');
insert into school (name, bio)
values ('Goldsmiths College, University of London', 'local');
insert into school (name, bio)
values ('Tiraspol State University', 'well-modulated');
insert into school (name, bio)
values ('Sevastopol National Technical University', 'Distributed');
insert into school (name, bio)
values ('Singhania University Rajasthan', 'hardware');
insert into school (name, bio)
values ('University of Medicine and Pharmacy of Iasi', 'Devolved');


INSERT INTO role (name, canPost, canApprove, canAssignProf, canApply, canRetract, canEditOwn, canEditAll, canDeleteOwn,
                  canDeleteAll, canUpdateAccess)
VALUES ('Admin', TRUE, TRUE, TRUE, FALSE, FALSE, TRUE, TRUE, TRUE, TRUE, TRUE),
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
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (1, 'Adler', 'Hubbert', 'Danielsson', '374-940-7237', 'adanielsson0@about.me', 88, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (2, 'Missy', 'Pottinger', 'Kinnerley', '743-786-3640', 'mkinnerley1@adobe.com', 68, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (3, 'Cinderella', null, 'Ladbury', '635-615-7529', 'cladbury2@flickr.com', 15, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (4, 'Dara', 'Honisch', 'Murdy', '735-691-1168', 'dmurdy3@zimbio.com', 17, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (5, 'Ely', null, 'Skip', '808-693-6397', 'eskip4@nasa.gov', 86, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (6, 'Walden', 'Gullefant', 'Bodiam', '862-403-6183', 'wbodiam5@taobao.com', 48, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (7, 'Roslyn', 'Blackston', 'Schruyer', '395-691-3239', 'rschruyer6@jimdo.com', 34, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (8, 'Kent', 'Bass', 'Bilt', '682-248-4149', 'kbilt7@disqus.com', 50, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (9, 'Haley', null, 'Pessler', '340-202-5351', 'hpessler8@prnewswire.com', 97, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (10, 'Albie', 'Waddams', 'Kennedy', '761-473-0585', 'akennedy9@japanpost.jp', 97, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (11, 'Doloritas', null, 'Johanchon', '439-345-2365', 'djohanchona@naver.com', 86, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (12, 'Aguie', 'Zemler', 'Marusik', '611-713-8847', 'amarusikb@desdev.cn', 38, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (13, 'Andras', 'Beardwell', 'Pretious', '374-278-7131', 'apretiousc@feedburner.com', 33, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (14, 'Tina', 'Ceeley', 'Challinor', '245-843-1544', 'tchallinord@bloglovin.com', 82, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (15, 'Coraline', 'Wellan', 'Muge', '217-349-0062', 'cmugee@ucoz.ru', 11, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (16, 'Thadeus', 'Crusham', 'Billyeald', '256-304-2337', 'tbillyealdf@gizmodo.com', 55, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (17, 'Max', 'Biles', 'Wooffinden', '118-236-3956', 'mwooffindeng@imdb.com', 49, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (18, 'Wakefield', null, 'Milkin', '329-889-0855', 'wmilkinh@va.gov', 7, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (19, 'Rob', 'Loads', 'Luttgert', '755-684-7303', 'rluttgerti@smugmug.com', 84, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (20, 'Dorena', null, 'Derycot', '835-155-8608', 'dderycotj@discuz.net', 71, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (21, 'D''arcy', 'Skerrett', 'Korejs', '389-949-3319', 'dkorejsk@tuttocitta.it', 48, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (22, 'Harmon', 'Hundall', 'Ingree', '486-409-9786', 'hingreel@linkedin.com', 56, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (23, 'Hallie', 'Biggadyke', 'Craigmile', '953-519-3496', 'hcraigmilem@oaic.gov.au', 54, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (24, 'Dunn', 'Schole', 'Gohn', '817-165-3914', 'dgohnn@statcounter.com', 16, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (25, 'Charlotte', 'McElrea', 'Alder', '393-627-2987', 'caldero@devhub.com', 62, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (26, 'Douglas', 'Gooden', 'Shrimplin', '588-333-0682', 'dshrimplinp@nifty.com', 30, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (27, 'Elli', 'Petrolli', 'Brambley', '446-202-0997', 'ebrambleyq@timesonline.co.uk', 18, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (28, 'Dean', 'Hassett', 'Krysztowczyk', '821-229-8410', 'dkrysztowczykr@phpbb.com', 9, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (29, 'Winnah', 'Lissaman', 'Lattey', '701-285-2606', 'wlatteys@de.vu', 27, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (30, 'Anthony', 'Cloney', 'Wildbore', '995-541-7874', 'awildboret@nasa.gov', 75, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (31, 'Raleigh', 'Sleford', 'Quickfall', '342-248-3651', 'rquickfallu@1688.com', 76, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (32, 'Jenifer', null, 'Windeatt', '866-459-8747', 'jwindeattv@posterous.com', 79, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (33, 'Annnora', 'Innett', 'Wimpenny', '638-432-4972', 'awimpennyw@wiley.com', 28, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (34, 'Cyndi', 'Ploughwright', 'Martino', '758-834-2446', 'cmartinox@wix.com', 92, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (35, 'Rory', 'Pride', 'Musgrove', '689-714-7171', 'rmusgrovey@soundcloud.com', 96, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (36, 'Lenka', 'Gianninotti', 'Wareham', '966-363-2786', 'lwarehamz@rakuten.co.jp', 92, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (37, 'Cherlyn', 'Ciobotaru', 'Watson-Brown', '780-249-1195', 'cwatsonbrown10@alexa.com', 94, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (38, 'Siana', 'Biasi', 'Poel', '788-635-4842', 'spoel11@psu.edu', 58, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (39, 'Berke', 'Gravenor', 'Shelmerdine', '408-441-8692', 'bshelmerdine12@google.es', 41, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (40, 'Aristotle', 'Biaggetti', 'Morgen', '809-107-4017', 'amorgen13@bbb.org', 24, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (41, 'Ariel', 'MacCarrick', 'Djakovic', '855-869-6847', 'adjakovic14@webnode.com', 36, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (42, 'Violetta', 'Cogman', 'De Carlo', '406-712-8809', 'vdecarlo15@squarespace.com', 54, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (43, 'Henrieta', null, 'Feldhorn', '748-521-6449', 'hfeldhorn16@aboutads.info', 41, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (44, 'Colan', 'Garroway', 'Aldgate', '229-677-9607', 'caldgate17@chicagotribune.com', 11, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (45, 'Jeff', 'Serrell', 'Moorerud', '353-983-8159', 'jmoorerud18@mozilla.org', 88, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (46, 'Devon', 'Knight', 'Duguid', '249-793-2004', 'dduguid19@blinklist.com', 16, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (47, 'Guinna', 'Squirrell', 'Boyce', '681-530-4775', 'gboyce1a@unesco.org', 13, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (48, 'Oralee', 'Yakovich', 'Broscombe', '194-593-2829', 'obroscombe1b@virginia.edu', 68, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (49, 'Sidnee', 'Dennidge', 'Wandrey', '270-474-7176', 'swandrey1c@wufoo.com', 21, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (50, 'Devin', 'O''Shavlan', 'Passmore', '864-381-3927', 'dpassmore1d@arstechnica.com', 44, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (51, 'Sandor', null, 'Bentham', '412-274-2788', 'sbentham1e@friendfeed.com', 89, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (52, 'Ivan', null, 'Springate', '328-995-8611', 'ispringate1f@nsw.gov.au', 39, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (53, 'Colet', 'Gurr', 'Canaan', '811-223-5311', 'ccanaan1g@ameblo.jp', 34, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (54, 'Maegan', 'Elis', 'Longmead', '477-982-5837', 'mlongmead1h@cdc.gov', 41, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (55, 'Melessa', 'Llop', 'Eglin', '466-433-0490', 'meglin1i@rediff.com', 89, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (56, 'Gawain', null, 'Callard', '606-791-6051', 'gcallard1j@craigslist.org', 19, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (57, 'Leila', null, 'Tellenbrook', '294-740-5693', 'ltellenbrook1k@independent.co.uk', 96, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (58, 'Geoff', 'Hembery', 'Kenningham', '437-286-3062', 'gkenningham1l@guardian.co.uk', 49, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (59, 'Denni', 'Corradeschi', 'Mullarkey', '199-848-8874', 'dmullarkey1m@go.com', 72, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (60, 'Blondie', 'Vennings', 'Bergin', '662-327-0516', 'bbergin1n@examiner.com', 70, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (61, 'Zitella', null, 'Poutress', '570-519-8386', 'zpoutress1o@cnet.com', 80, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (62, 'Dunstan', null, 'Welfare', '470-293-7169', 'dwelfare1p@globo.com', 54, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (63, 'Gallagher', 'Grisbrook', 'Dowgill', '211-603-1860', 'gdowgill1q@surveymonkey.com', 15, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (64, 'Maybelle', 'Curnick', 'Sidwick', '998-874-9392', 'msidwick1r@ustream.tv', 14, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (65, 'Hilary', 'Penley', 'Funcheon', '412-677-3556', 'hfuncheon1s@g.co', 88, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (66, 'Orville', 'Breward', 'Brandel', '812-238-1469', 'obrandel1t@tinypic.com', 34, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (67, 'Moll', 'Simoncelli', 'Myles', '113-646-1314', 'mmyles1u@blogtalkradio.com', 13, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (68, 'Robbert', 'Hallybone', 'Kamena', '927-180-6609', 'rkamena1v@seattletimes.com', 23, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (69, 'Worden', 'Hampton', 'Cregin', '697-214-9698', 'wcregin1w@diigo.com', 62, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (70, 'Korey', 'Potier', 'Burgisi', '500-451-0970', 'kburgisi1x@163.com', 92, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (71, 'Rafferty', 'Calven', 'Abethell', '733-586-6199', 'rabethell1y@booking.com', 21, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (72, 'Suellen', 'Frostdick', 'Alesbrook', '447-838-1245', 'salesbrook1z@home.pl', 82, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (73, 'Rochella', 'Lanktree', 'Dominichelli', '743-468-9922', 'rdominichelli20@facebook.com', 37, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (74, 'Carrie', 'Riggulsford', 'Thornhill', '818-700-9849', 'cthornhill21@freewebs.com', 10, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (75, 'Klara', 'Jeannesson', 'Mash', '406-107-8864', 'kmash22@cocolog-nifty.com', 78, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (76, 'Malchy', 'Tomkin', 'Sneesby', '412-870-7544', 'msneesby23@is.gd', 43, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (77, 'Brok', 'Heasman', 'Forsyth', '598-169-0626', 'bforsyth24@github.com', 44, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (78, 'Astrix', null, 'Ruzic', '725-998-7304', 'aruzic25@chronoengine.com', 99, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (79, 'Almira', 'Jakoviljevic', 'Greenard', '577-722-5751', 'agreenard26@timesonline.co.uk', 21, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (80, 'Andra', null, 'Stollenwerck', '490-474-7090', 'astollenwerck27@shop-pro.jp', 47, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (81, 'Annissa', 'Sparke', 'Darlington', '218-387-0056', 'adarlington28@symantec.com', 36, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (82, 'Beniamino', 'Bellhanger', 'Ferronel', '729-982-4414', 'bferronel29@yahoo.com', 2, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (83, 'Abbot', 'Pischoff', 'Skewes', '618-505-4258', 'askewes2a@sun.com', 81, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (84, 'Jacquetta', 'Seemmonds', 'Houselee', '959-574-0764', 'jhouselee2b@fema.gov', 54, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (85, 'Mickie', 'Doge', 'Dominiak', '499-386-5417', 'mdominiak2c@amazon.de', 32, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (86, 'Ezra', 'Cain', 'Elion', '330-935-1640', 'eelion2d@nba.com', 16, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (87, 'Rolf', null, 'Lillistone', '315-273-1558', 'rlillistone2e@cnet.com', 49, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (88, 'Rochette', 'Ecclesall', 'Birchenough', '607-610-7474', 'rbirchenough2f@boston.com', 77, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (89, 'Natalee', 'Lobley', 'Gamage', '657-308-2987', 'ngamage2g@networkadvertising.org', 74, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (90, 'Wallis', null, 'Schust', '838-408-9982', 'wschust2h@e-recht24.de', 55, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (91, 'Opaline', 'Gabbitus', 'Morey', '265-901-8495', 'omorey2i@chron.com', 65, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (92, 'Piper', 'Dallon', 'Clibbery', '578-790-5580', 'pclibbery2j@ebay.com', 34, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (93, 'Wandie', 'Jeenes', 'Delacote', '445-884-4468', 'wdelacote2k@stumbleupon.com', 8, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (94, 'Anneliese', 'Clive', 'Hevey', '492-920-7949', 'ahevey2l@friendfeed.com', 63, 1);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (95, 'Francisca', null, 'Gann', '286-125-6355', 'fgann2m@pinterest.com', 95, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (96, 'Astra', 'Matschke', 'Verlander', '448-863-4259', 'averlander2n@mozilla.com', 94, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (97, 'Solomon', 'Buer', 'Fortun', '678-257-3937', 'sfortun2o@google.de', 31, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (98, 'Berte', 'Pitrelli', 'Quirk', '501-134-1704', 'bquirk2p@netlog.com', 93, 3);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (99, 'Marcile', null, 'Eckley', '833-586-8666', 'meckley2q@mit.edu', 13, 2);
insert into user (userId, firstName, middleName, lastName, phone, email, schoolId, roleId)
values (100, 'Flori', 'Alp', 'Clemas', '611-144-5600', 'fclemas2r@wp.com', 5, 2);


INSERT INTO userTagParent (tagName, category)
VALUES ('Computer Science', 'Major'),
       ('2027', 'Graduation Year'),
       ('Business', 'Curriculum'),
       ('Gaming', 'Entertainment'),
       ('AI', 'Technology'),
       ('Machine Learning', 'Technology'),
       ('Photography', 'Hobbies'),
       ('Cooking', 'Hobbies'),
       ('Travel', 'Lifestyle'),
       ('Fitness', 'Lifestyle'),
       ('Blockchain', 'Technology'),
       ('Movies', 'Entertainment'),
       ('Music', 'Entertainment'),
       ('Painting', 'Hobbies'),
       ('Gardening', 'Hobbies'),
       ('Health', 'Lifestyle'),
       ('Programming', 'Technology'),
       ('Reading', 'Hobbies'),
       ('Cycling', 'Hobbies'),
       ('Climbing', 'Hobbies'),
       ('Streaming', 'Entertainment'),
       ('VR Games', 'Technology'),
       ('Board Games', 'Entertainment'),
       ('Cryptocurrency', 'Technology'),
       ('Yoga', 'Lifestyle'),
       ('Dancing', 'Hobbies'),
       ('Fishing', 'Hobbies'),
       ('Crafting', 'Hobbies'),
       ('Design', 'Technology'),
       ('UX/UI Design', 'Technology'),
       ('Astronomy', 'Hobbies'),
       ('K-pop', 'Entertainment'),
       ('Podcasts', 'Entertainment'),
       ('Anime', 'Entertainment'),
       ('Writing', 'Hobbies'),
       ('Storytelling', 'Hobbies'),
       ('E-sports', 'Entertainment'),
       ('Game Development', 'Technology'),
       ('Sound Design', 'Technology'),
       ('Video Editing', 'Technology'),
       ('Language Learning', 'Hobbies'),
       ('Meditation', 'Lifestyle'),
       ('Social Media', 'Technology'),
       ('E-commerce', 'Technology'),
       ('Web Development', 'Technology'),
       ('App Development', 'Technology'),
       ('Digital Marketing', 'Technology'),
       ('Entrepreneurship', 'Lifestyle'),
       ('Self-improvement', 'Lifestyle'),
       ('Networking', 'Lifestyle'),
       ('Home Decor', 'Hobbies'),
       ('Fashion', 'Lifestyle'),
       ('Luxury Cars', 'Lifestyle'),
       ('Camping', 'Hobbies'),
       ('Hiking', 'Hobbies'),
       ('Martial Arts', 'Lifestyle'),
       ('Skating', 'Hobbies'),
       ('Robotics', 'Technology'),
       ('Smart Homes', 'Technology'),
       ('Space Exploration', 'Technology'),
       ('Environmentalism', 'Lifestyle'),
       ('Sustainability', 'Lifestyle'),
       ('Bird Watching', 'Hobbies'),
       ('Geocaching', 'Hobbies'),
       ('Scuba Diving', 'Hobbies'),
       ('Surfing', 'Hobbies'),
       ('Freelancing', 'Lifestyle'),
       ('Investing', 'Lifestyle'),
       ('Stock Market', 'Technology'),
       ('AI Ethics', 'Technology'),
       ('Philosophy', 'Hobbies'),
       ('Cultural Studies', 'Hobbies'),
       ('History', 'Hobbies'),
       ('Archaeology', 'Hobbies'),
       ('Antiques', 'Hobbies'),
       ('Interior Design', 'Lifestyle'),
       ('Calligraphy', 'Hobbies'),
       ('Tattoo Art', 'Hobbies'),
       ('Live Music', 'Entertainment'),
       ('DJing', 'Entertainment'),
       ('Stand-up Comedy', 'Entertainment'),
       ('Circus Arts', 'Entertainment'),
       ('Event Planning', 'Lifestyle'),
       ('Baking', 'Hobbies'),
       ('Urban Gardening', 'Hobbies'),
       ('Leatherworking', 'Hobbies'),
       ('Woodworking', 'Hobbies'),
       ('DIY Projects', 'Hobbies'),
       ('RC Cars', 'Hobbies'),
       ('Drone Flying', 'Hobbies'),
       ('Fitness Coaching', 'Lifestyle'),
       ('Pilates', 'Lifestyle'),
       ('Mindfulness', 'Lifestyle'),
       ('Astrology', 'Hobbies'),
       ('Tarot Reading', 'Hobbies'),
       ('Magic Tricks', 'Entertainment'),
       ('Stage Performance', 'Entertainment'),
       ('Community Service', 'Lifestyle'),
       ('Volunteer Work', 'Lifestyle'),
       ('Pet Care', 'Lifestyle'),
       ('Dog Training', 'Hobbies'),
       ('Cat Training', 'Hobbies');

INSERT INTO userTag (userId, userTagId)
VALUES (1, 1),
       (2, 2);
insert into userTag (userId, userTagId)
values (4, 74);
insert into userTag (userId, userTagId)
values (75, 34);
insert into userTag (userId, userTagId)
values (35, 34);
insert into userTag (userId, userTagId)
values (29, 33);
insert into userTag (userId, userTagId)
values (85, 31);
insert into userTag (userId, userTagId)
values (49, 85);
insert into userTag (userId, userTagId)
values (13, 69);
insert into userTag (userId, userTagId)
values (23, 42);
insert into userTag (userId, userTagId)
values (26, 84);
insert into userTag (userId, userTagId)
values (66, 69);
insert into userTag (userId, userTagId)
values (94, 2);
insert into userTag (userId, userTagId)
values (66, 32);
insert into userTag (userId, userTagId)
values (60, 90);
insert into userTag (userId, userTagId)
values (49, 5);
insert into userTag (userId, userTagId)
values (14, 65);
insert into userTag (userId, userTagId)
values (77, 38);
insert into userTag (userId, userTagId)
values (52, 87);
insert into userTag (userId, userTagId)
values (37, 43);
insert into userTag (userId, userTagId)
values (89, 69);
insert into userTag (userId, userTagId)
values (66, 39);
insert into userTag (userId, userTagId)
values (16, 12);
insert into userTag (userId, userTagId)
values (90, 25);
insert into userTag (userId, userTagId)
values (34, 68);
insert into userTag (userId, userTagId)
values (76, 77);
insert into userTag (userId, userTagId)
values (69, 42);
insert into userTag (userId, userTagId)
values (35, 12);
insert into userTag (userId, userTagId)
values (84, 89);
insert into userTag (userId, userTagId)
values (84, 30);
insert into userTag (userId, userTagId)
values (87, 100);
insert into userTag (userId, userTagId)
values (85, 10);
insert into userTag (userId, userTagId)
values (75, 43);
insert into userTag (userId, userTagId)
values (19, 62);
insert into userTag (userId, userTagId)
values (81, 6);
insert into userTag (userId, userTagId)
values (42, 93);
insert into userTag (userId, userTagId)
values (77, 54);
insert into userTag (userId, userTagId)
values (65, 22);
insert into userTag (userId, userTagId)
values (61, 65);
insert into userTag (userId, userTagId)
values (90, 39);
insert into userTag (userId, userTagId)
values (72, 57);
insert into userTag (userId, userTagId)
values (47, 43);
insert into userTag (userId, userTagId)
values (53, 100);
insert into userTag (userId, userTagId)
values (38, 36);
insert into userTag (userId, userTagId)
values (52, 29);
insert into userTag (userId, userTagId)
values (4, 69);
insert into userTag (userId, userTagId)
values (76, 88);
insert into userTag (userId, userTagId)
values (8, 80);
insert into userTag (userId, userTagId)
values (79, 47);
insert into userTag (userId, userTagId)
values (77, 78);
insert into userTag (userId, userTagId)
values (33, 19);
insert into userTag (userId, userTagId)
values (44, 71);
insert into userTag (userId, userTagId)
values (22, 14);
insert into userTag (userId, userTagId)
values (53, 57);
insert into userTag (userId, userTagId)
values (79, 71);
insert into userTag (userId, userTagId)
values (31, 45);
insert into userTag (userId, userTagId)
values (59, 40);
insert into userTag (userId, userTagId)
values (54, 25);
insert into userTag (userId, userTagId)
values (43, 7);
insert into userTag (userId, userTagId)
values (75, 10);
insert into userTag (userId, userTagId)
values (36, 92);
insert into userTag (userId, userTagId)
values (57, 41);
insert into userTag (userId, userTagId)
values (73, 37);
insert into userTag (userId, userTagId)
values (45, 98);
insert into userTag (userId, userTagId)
values (30, 18);
insert into userTag (userId, userTagId)
values (79, 40);
insert into userTag (userId, userTagId)
values (58, 4);
insert into userTag (userId, userTagId)
values (60, 78);
insert into userTag (userId, userTagId)
values (69, 92);
insert into userTag (userId, userTagId)
values (62, 49);
insert into userTag (userId, userTagId)
values (25, 97);
insert into userTag (userId, userTagId)
values (61, 43);
insert into userTag (userId, userTagId)
values (84, 3);
insert into userTag (userId, userTagId)
values (36, 53);
insert into userTag (userId, userTagId)
values (28, 1);
insert into userTag (userId, userTagId)
values (21, 25);
insert into userTag (userId, userTagId)
values (100, 9);
insert into userTag (userId, userTagId)
values (52, 98);
insert into userTag (userId, userTagId)
values (97, 5);
insert into userTag (userId, userTagId)
values (61, 83);
insert into userTag (userId, userTagId)
values (92, 57);
insert into userTag (userId, userTagId)
values (59, 8);
insert into userTag (userId, userTagId)
values (26, 95);
insert into userTag (userId, userTagId)
values (87, 66);
insert into userTag (userId, userTagId)
values (75, 42);
insert into userTag (userId, userTagId)
values (84, 55);
insert into userTag (userId, userTagId)
values (40, 90);
insert into userTag (userId, userTagId)
values (66, 23);
insert into userTag (userId, userTagId)
values (92, 18);
insert into userTag (userId, userTagId)
values (2, 68);
insert into userTag (userId, userTagId)
values (11, 91);
insert into userTag (userId, userTagId)
values (28, 90);
insert into userTag (userId, userTagId)
values (97, 85);
insert into userTag (userId, userTagId)
values (72, 61);
insert into userTag (userId, userTagId)
values (65, 44);
insert into userTag (userId, userTagId)
values (6, 87);
insert into userTag (userId, userTagId)
values (26, 7);
insert into userTag (userId, userTagId)
values (81, 32);
insert into userTag (userId, userTagId)
values (57, 3);
insert into userTag (userId, userTagId)
values (85, 95);
insert into userTag (userId, userTagId)
values (78, 1);
insert into userTag (userId, userTagId)
values (47, 28);


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
       ('Dialogue: The Chemistry of Green Energy in Iceland', 'Iceland', 2, 3, '2024-02-01', '2024-07-01', FALSE, TRUE),
       ('Dialogue: Art and Culture of Italy', 'Italy', 34, 23, '2024-03-01', '2024-08-01', TRUE, FALSE),
       ('Dialogue: Environmental Sciences in Costa Rica', 'Costa Rica', 87, 45, '2024-04-01', '2024-09-01', FALSE,
        TRUE),
       ('Dialogue: The History of Ancient Greece', 'Greece', 65, 76, '2024-05-01', '2024-10-01', TRUE, FALSE),
       ('Dialogue: The Physics of Space Exploration in the USA', 'USA', 12, 90, '2024-06-01', '2024-12-01', FALSE,
        TRUE),
       ('Dialogue: Digital Transformation in Singapore', 'Singapore', 24, 33, '2024-07-01', '2025-01-01', TRUE, FALSE),
       ('Dialogue: Culinary Arts in France', 'France', 56, 49, '2024-08-01', '2025-02-01', FALSE, TRUE),
       ('Dialogue: Renewable Energy in Germany', 'Germany', 41, 67, '2024-09-01', '2025-03-01', TRUE, FALSE),
       ('Dialogue: Wildlife Conservation in South Africa', 'South Africa', 73, 89, '2024-10-01', '2025-04-01', FALSE,
        TRUE),
       ('Dialogue: Architecture and Design in Japan', 'Japan', 29, 34, '2024-11-01', '2025-05-01', TRUE, FALSE),
       ('Dialogue: Literature and Storytelling in Ireland', 'Ireland', 88, 19, '2024-12-01', '2025-06-01', FALSE, TRUE),
       ('Dialogue: The Robotics Revolution in South Korea', 'South Korea', 45, 78, '2025-01-01', '2025-07-01', TRUE,
        FALSE),
       ('Dialogue: Marine Biology in Australia', 'Australia', 53, 44, '2025-02-01', '2025-08-01', FALSE, TRUE),
       ('Dialogue: The Evolution of Music in Brazil', 'Brazil', 69, 21, '2025-03-01', '2025-09-01', TRUE, FALSE),
       ('Dialogue: Public Health Innovations in Sweden', 'Sweden', 18, 99, '2025-04-01', '2025-10-01', FALSE, TRUE),
       ('Dialogue: Engineering the Future in Canada', 'Canada', 36, 55, '2025-05-01', '2025-11-01', TRUE, FALSE),
       ('Dialogue: Film and Media Studies in the UK', 'UK', 77, 11, '2025-06-01', '2025-12-01', FALSE, TRUE),
       ('Dialogue: Anthropology in Mexico', 'Mexico', 31, 46, '2025-07-01', '2026-01-01', TRUE, FALSE),
       ('Dialogue: Astronomy in Chile', 'Chile', 94, 62, '2025-08-01', '2026-02-01', FALSE, TRUE),
       ('Dialogue: AI and Ethics in Finland', 'Finland', 25, 10, '2025-09-01', '2026-03-01', TRUE, FALSE),
       ('Dialogue: Urban Planning in the Netherlands', 'Netherlands', 32, 58, '2025-10-01', '2026-04-01', FALSE, TRUE),
       ('Dialogue: Sustainable Agriculture in New Zealand', 'New Zealand', 14, 77, '2025-11-01', '2026-05-01', TRUE,
        FALSE),
       ('Dialogue: Innovations in Education in Norway', 'Norway', 89, 54, '2025-12-01', '2026-06-01', FALSE, TRUE),
       ('Dialogue: History of the Silk Road in China', 'China', 42, 83, '2026-01-01', '2026-07-01', TRUE, FALSE),
       ('Dialogue: Renewable Resources in Denmark', 'Denmark', 51, 67, '2026-02-01', '2026-08-01', FALSE, TRUE),
       ('Dialogue: Biodiversity in the Amazon', 'Brazil', 61, 45, '2026-03-01', '2026-09-01', TRUE, FALSE),
       ('Dialogue: Archaeology in Egypt', 'Egypt', 13, 28, '2026-04-01', '2026-10-01', FALSE, TRUE),
       ('Dialogue: Biotechnology in Switzerland', 'Switzerland', 27, 39, '2026-05-01', '2026-11-01', TRUE, FALSE),
       ('Dialogue: Political History in Washington D.C.', 'USA', 34, 26, '2026-06-01', '2026-12-01', FALSE, TRUE),
       ('Dialogue: Volcanoes and Earth Sciences in Hawaii', 'USA', 76, 11, '2026-07-01', '2027-01-01', TRUE, FALSE),
       ('Dialogue: Wildlife Ecology in Kenya', 'Kenya', 29, 93, '2026-08-01', '2027-02-01', FALSE, TRUE),
       ('Dialogue: Space Engineering in Russia', 'Russia', 81, 40, '2026-09-01', '2027-03-01', TRUE, FALSE),
       ('Dialogue: Climate Studies in Antarctica', 'Antarctica', 68, 15, '2026-10-01', '2027-04-01', FALSE, TRUE),
       ('Dialogue: Creative Writing in Scotland', 'Scotland', 17, 92, '2026-11-01', '2027-05-01', TRUE, FALSE),
       ('Dialogue: Sports Science in Spain', 'Spain', 53, 74, '2026-12-01', '2027-06-01', FALSE, TRUE),
       ('Dialogue: Gender Studies in Argentina', 'Argentina', 22, 66, '2027-01-01', '2027-07-01', TRUE, FALSE),
       ('Dialogue: Traditional Medicine in India', 'India', 12, 97, '2027-02-01', '2027-08-01', FALSE, TRUE),
       ('Dialogue: Astronomy in Namibia', 'Namibia', 84, 21, '2027-03-01', '2027-09-01', TRUE, FALSE),
       ('Dialogue: Advanced Robotics in Japan', 'Japan', 38, 85, '2027-04-01', '2027-10-01', FALSE, TRUE),
       ('Dialogue: Historical Architecture in Turkey', 'Turkey', 90, 31, '2027-05-01', '2027-11-01', TRUE, FALSE),
       ('Dialogue: Performing Arts in Austria', 'Austria', 24, 55, '2027-06-01', '2027-12-01', FALSE, TRUE),
       ('Dialogue: Cultural Anthropology in Indonesia', 'Indonesia', 33, 47, '2027-07-01', '2028-01-01', TRUE, FALSE),
       ('Dialogue: Glacier Studies in Greenland', 'Greenland', 5, 63, '2027-08-01', '2028-02-01', FALSE, TRUE),
       ('Dialogue: Urban Technology in the UAE', 'UAE', 7, 88, '2027-09-01', '2028-03-01', TRUE, FALSE),
       ('Dialogue: Food Science in Thailand', 'Thailand', 20, 78, '2027-10-01', '2028-04-01', FALSE, TRUE),
       ('Dialogue: Linguistics in Quebec', 'Canada', 11, 95, '2027-11-01', '2028-05-01', TRUE, FALSE),
       ('Dialogue: Energy Storage in Nevada', 'USA', 6, 18, '2027-12-01', '2028-06-01', FALSE, TRUE),
       ('Dialogue: Social Innovation in Israel', 'Israel', 19, 22, '2028-01-01', '2028-07-01', TRUE, FALSE),
       ('Dialogue: Cybersecurity in Estonia', 'Estonia', 37, 16, '2028-02-01', '2028-08-01', FALSE, TRUE),
       ('Dialogue: Creative Arts in the Philippines', 'Philippines', 49, 50, '2028-03-01', '2028-09-01', TRUE, FALSE),
       ('Dialogue: Agriculture Technology in Vietnam', 'Vietnam', 9, 79, '2028-04-01', '2028-10-01', FALSE, TRUE),
       ('Dialogue: Oceanography in Fiji', 'Fiji', 28, 64, '2028-05-01', '2028-11-01', TRUE, FALSE),
       ('Dialogue: Philosophy in Germany', 'Germany', 44, 3, '2028-06-01', '2028-12-01', FALSE, TRUE),
       ('Dialogue: Cultural Studies in South Korea', 'South Korea', 41, 72, '2028-07-01', '2029-01-01', TRUE, FALSE),
       ('Dialogue: Environmental Policy in Australia', 'Australia', 26, 87, '2028-08-01', '2029-02-01', FALSE, TRUE),
       ('Dialogue: Music Production in Sweden', 'Sweden', 30, 69, '2028-09-01', '2029-03-01', TRUE, FALSE),
       ('Dialogue: Entrepreneurship in Brazil', 'Brazil', 80, 43, '2028-10-01', '2029-04-01', FALSE, TRUE),
       ('Dialogue: Veterinary Science in New Zealand', 'New Zealand', 71, 94, '2028-11-01', '2029-05-01', TRUE, FALSE),
       ('Dialogue: Renewable Energy in Chile', 'Chile', 35, 56, '2028-12-01', '2029-06-01', FALSE, TRUE);

INSERT INTO post (postAuthor, title, body, programId, userId)
VALUES ('Dr. Smith', 'Dialogue: The Mathematical Heritage of Hungary',
        'This is an introduction to computer science courses.', 1, 1),
       ('White Apple Snow', 'Dialogue: The Chemistry of Green Energy in Iceland',
        'Explore the world of finance and business opportunities in Iceland.', 2, 3),
       ('Professor Johnson', 'Dialogue: Art and Culture of Italy',
        'Join us in Italy to study its rich art and cultural heritage.', 34, 25),
       ('Dr. Maria Lopez', 'Dialogue: Environmental Sciences in Costa Rica',
        'Learn about biodiversity and sustainability in Costa Rica.', 87, 42),
       ('Dr. Alan Brown', 'Dialogue: The History of Ancient Greece',
        'Uncover the secrets of ancient Greek civilization.', 65, 78),
       ('Emily Clark', 'Dialogue: The Physics of Space Exploration in the USA',
        'Discuss groundbreaking advancements in space technology.', 12, 53),
       ('Dr. Henry Yang', 'Dialogue: Digital Transformation in Singapore',
        'A comprehensive study on the digital age and its impact.', 24, 19),
       ('Dr. Eva Keller', 'Dialogue: Culinary Arts in France',
        'A culinary journey through France’s finest cuisines.', 56, 7),
       ('Prof. Michael Reed', 'Dialogue: Renewable Energy in Germany',
        'Explore sustainable energy solutions in Germany.', 41, 61),
       ('Dr. Lily Chen', 'Dialogue: Wildlife Conservation in South Africa',
        'Conservation techniques and strategies in Africa.', 73, 44),
       ('Anna Harper', 'Dialogue: Architecture and Design in Japan',
        'Experience cutting-edge architecture and design.', 29, 33),
       ('Dr. Frank Murphy', 'Dialogue: Literature and Storytelling in Ireland',
        'Dive into the rich literary history of Ireland.', 88, 22),
       ('Dr. Samantha Kim', 'Dialogue: The Robotics Revolution in South Korea',
        'Learn about advancements in robotics and AI.', 45, 77),
       ('Mr. Daniel Perez', 'Dialogue: Marine Biology in Australia',
        'Study marine ecosystems and their conservation.', 53, 14),
       ('Dr. Rose Carter', 'Dialogue: The Evolution of Music in Brazil',
        'A study of Brazil’s diverse musical traditions.', 69, 31),
       ('Dr. Julia Collins', 'Dialogue: Public Health Innovations in Sweden',
        'Discover public health systems and their efficiencies.', 18, 63),
       ('Dr. Eric Johnson', 'Dialogue: Engineering the Future in Canada',
        'Explore innovations shaping tomorrow’s engineering.', 36, 90),
       ('Dr. Claire Wilson', 'Dialogue: Film and Media Studies in the UK',
        'Discover the history and trends of UK’s film industry.', 77, 49),
       ('Dr. Oliver Grant', 'Dialogue: Anthropology in Mexico',
        'Study ancient cultures and modern anthropology.', 31, 68),
       ('Dr. Nora Schmidt', 'Dialogue: Astronomy in Chile',
        'Uncover the mysteries of the universe.', 94, 8),
       ('Dr. Victoria Brooks', 'Dialogue: AI and Ethics in Finland',
        'Explore ethical implications of AI technologies.', 25, 21),
       ('Dr. Ryan Mitchell', 'Dialogue: Urban Planning in the Netherlands',
        'Learn about innovative urban design strategies.', 32, 76),
       ('Prof. David Patel', 'Dialogue: Sustainable Agriculture in New Zealand',
        'A practical guide to sustainable farming.', 14, 36),
       ('Dr. Helen Garcia', 'Dialogue: Innovations in Education in Norway',
        'Study advanced teaching methodologies.', 89, 15),
       ('Dr. James Rivera', 'Dialogue: History of the Silk Road in China',
        'Follow the historical trade routes of Asia.', 42, 81),
       ('Dr. Sarah Turner', 'Dialogue: Renewable Resources in Denmark',
        'Study renewable energy and sustainable practices.', 51, 45),
       ('Dr. Alex Mason', 'Dialogue: Biodiversity in the Amazon',
        'Discover the unique ecosystems of the Amazon rainforest.', 61, 12),
       ('Prof. Robert Foster', 'Dialogue: Archaeology in Egypt',
        'Explore ancient wonders and archaeological sites.', 13, 71),
       ('Dr. Lucy Porter', 'Dialogue: Biotechnology in Switzerland',
        'Learn about genetic engineering and innovation.', 27, 91),
       ('Dr. Kevin Adams', 'Dialogue: Political History in Washington D.C.',
        'Dive into the history of American politics.', 34, 18),
       ('Dr. Lisa Meyer', 'Dialogue: Volcanoes and Earth Sciences in Hawaii',
        'Study the geology of volcanic landscapes.', 76, 59),
       ('Dr. Monica Wright', 'Dialogue: Wildlife Ecology in Kenya',
        'Experience wildlife conservation in Africa.', 29, 85),
       ('Dr. George Baker', 'Dialogue: Space Engineering in Russia',
        'Explore innovations in space engineering and technology.', 81, 4),
       ('Dr. Emily Thomas', 'Dialogue: Climate Studies in Antarctica',
        'Understand the impact of climate change.', 68, 37),
       ('Dr. Rachel Simmons', 'Dialogue: Creative Writing in Scotland',
        'Master the art of storytelling.', 17, 50),
       ('Dr. Thomas Stewart', 'Dialogue: Sports Science in Spain',
        'Study physical performance and sports management.', 53, 32),
       ('Dr. Amanda Lewis', 'Dialogue: Gender Studies in Argentina',
        'Explore the sociology of gender and identity.', 22, 11),
       ('Dr. Charles Bennett', 'Dialogue: Traditional Medicine in India',
        'Study the rich history of Indian medicinal practices.', 12, 43),
       ('Dr. Megan Hill', 'Dialogue: Astronomy in Namibia',
        'Investigate the cosmos through advanced telescopes.', 84, 29),
       ('Dr. Brian Carter', 'Dialogue: Advanced Robotics in Japan',
        'Learn about cutting-edge robotics and AI.', 38, 60),
       ('Dr. Katie Hughes', 'Dialogue: Historical Architecture in Turkey',
        'Explore the architectural wonders of Turkey.', 90, 26),
       ('Dr. Rebecca Scott', 'Dialogue: Performing Arts in Austria',
        'A journey into the world of theater and performance.', 24, 72),
       ('Dr. Philip Edwards', 'Dialogue: Cultural Anthropology in Indonesia',
        'Study cultural diversity and societal structures.', 33, 97),
       ('Dr. Laura Young', 'Dialogue: Glacier Studies in Greenland',
        'Explore the dynamics of polar ice sheets.', 5, 64),
       ('Dr. Steven Lee', 'Dialogue: Urban Technology in the UAE',
        'Discover innovations in urban development.', 7, 88),
       ('Dr. Teresa Brooks', 'Dialogue: Food Science in Thailand',
        'Explore advancements in food processing.', 20, 70),
       ('Dr. Patrick Reed', 'Dialogue: Linguistics in Quebec',
        'Understand the evolution of language and dialects.', 11, 19),
       ('Dr. Olivia Murphy', 'Dialogue: Energy Storage in Nevada',
        'Study sustainable energy solutions and storage.', 6, 84),
       ('Dr. Sophia Torres', 'Dialogue: Social Innovation in Israel',
        'Learn about community-driven change.', 19, 38),
       ('Dr. Matthew Bell', 'Dialogue: Cybersecurity in Estonia',
        'Explore methods to secure digital systems.', 37, 56),
       ('Dr. Samuel King', 'Dialogue: Creative Arts in the Philippines',
        'Develop creative thinking and artistic skills.', 49, 67),
       ('Dr. Jessica White', 'Dialogue: Agriculture Technology in Vietnam',
        'Learn about modern farming innovations.', 9, 74),
       ('Dr. John Davis', 'Dialogue: Oceanography in Fiji',
        'Explore marine ecosystems and ocean life.', 28, 92),
       ('Dr. Ella Rivera', 'Dialogue: Philosophy in Germany',
        'Delve into classical and modern philosophy.', 44, 30),
       ('Dr. Ryan Phillips', 'Dialogue: Cultural Studies in South Korea',
        'Explore Korean history and contemporary culture.', 41, 48),
       ('Dr. Ashley Martinez', 'Dialogue: Environmental Policy in Australia',
        'Learn about global environmental strategies.', 26, 66),
       ('Dr. Ethan Wright', 'Dialogue: Music Production in Sweden',
        'Discover the art of music production and composition.', 30, 93),
       ('Dr. Abigail Ward', 'Dialogue: Entrepreneurship in Brazil',
        'Explore strategies for starting a successful business.', 80, 53),
       ('Dr. Rachel Morgan', 'Dialogue: Veterinary Science in New Zealand',
        'Learn about animal health and care practices.', 71, 94),
       ('Dr. Natalie Carter', 'Dialogue: Renewable Energy in Chile',
        'Study innovative energy solutions.', 35, 79),
       ('Dr. Anthony Flores', 'Dialogue: Global Trade in Singapore',
        'Learn about international business practices.', 46, 21),
       ('Dr. Ella Rivera', 'Dialogue: Human Rights Advocacy in South Africa',
        'Explore strategies to protect human rights.', 54, 87),
       ('Dr. Michael Gonzales', 'Dialogue: Literature in the Modern Era',
        'Discover the evolution of global literature.', 33, 11),
       ('Dr. Andrew Nelson', 'Dialogue: AI Applications in Everyday Life',
        'Learn how AI is transforming industries.', 66, 43),
       ('Dr. Olivia Bennett', 'Dialogue: Renewable Futures in Europe',
        'Discover innovative solutions for a greener future.', 92, 54);


INSERT INTO postTagParent (tagName, category)
VALUES
('Fall 2024', 'Time'),
('Spring 2025', 'Time'),
('Data Science', 'Major'),
('Mechanical Engineering', 'Major'),
('Artificial Intelligence', 'Field'),
('Cybersecurity', 'Field'),
('Renewable Energy', 'Field'),
('Urban Planning', 'Field'),
('Cultural Studies', 'Subject'),
('Environmental Science', 'Subject'),
('Astronomy', 'Subject'),
('Philosophy', 'Subject'),
('Germany', 'Location'),
('Brazil', 'Location'),
('Japan', 'Location'),
('Antarctica', 'Location'),
('Full-Time', 'Program Type'),
('Part-Time', 'Program Type'),
('Internship', 'Program Type'),
('Dialogue', 'Program Type'),
('Advanced Robotics', 'Topic'),
('Marine Biology', 'Topic'),
('AI Ethics', 'Topic'),
('Space Exploration', 'Topic'),
('Hiking', 'Activity'),
('Cultural Immersion', 'Activity'),
('Field Research', 'Activity'),
('Studio Art', 'Activity'),
('Human Rights', 'Cause'),
('Climate Action', 'Cause'),
('Wildlife Conservation', 'Cause'),
('Education Equity', 'Cause'),
('Networking', 'Goal'),
('Skill Development', 'Goal'),
('Academic Excellence', 'Goal'),
('Language Proficiency', 'Goal'),
('Semester Abroad', 'Experience Type'),
('Research Project', 'Experience Type'),
('Service Learning', 'Experience Type'),
('Capstone Course', 'Experience Type'),
('Online', 'Delivery Method'),
('In-Person', 'Delivery Method'),
('Hybrid', 'Delivery Method'),
('Weekend Program', 'Delivery Method'),
('Technology', 'Industry'),
('Healthcare', 'Industry'),
('Finance', 'Industry'),
('Entertainment', 'Industry'),
('Undergraduate', 'Education Level'),
('Graduate', 'Education Level'),
('Doctoral', 'Education Level'),
('Professional Development', 'Education Level'),
('Scholarship', 'Funding'),
('Grant', 'Funding'),
('Self-Funded', 'Funding'),
('Employer-Sponsored', 'Funding'),
('Leadership', 'Skill'),
('Collaboration', 'Skill'),
('Critical Thinking', 'Skill'),
('Innovation', 'Skill'),
('Sustainability', 'Focus Area'),
('Globalization', 'Focus Area'),
('Cultural Diversity', 'Focus Area'),
('Economic Development', 'Focus Area'),
('Introductory', 'Course Level'),
('Intermediate', 'Course Level'),
('Advanced', 'Course Level'),
('Specialized', 'Course Level'),
('Research', 'Outcome'),
('Publication', 'Outcome'),
('Thesis', 'Outcome'),
('Conference Presentation', 'Outcome'),
('Winter Break', 'Time'),
('Summer 2', 'Time'),
('Civil Engineering', 'Major'),
('Biotechnology', 'Major'),
('Machine Learning', 'Field'),
('Blockchain', 'Field'),
('Sustainable Design', 'Field'),
('Healthcare Management', 'Field'),
('Psychology', 'Subject'),
('Geology', 'Subject'),
('Anthropology', 'Subject'),
('Performing Arts', 'Subject'),
('Italy', 'Location'),
('Canada', 'Location'),
('Thailand', 'Location'),
('South Africa', 'Location'),
('Weekend Workshops', 'Program Type'),
('Certificate Program', 'Program Type'),
('Crisis Management', 'Topic'),
('Digital Marketing', 'Topic');

INSERT INTO postTag (postId, postTagId)
VALUES
(1, 1),
(2, 2),
(3, 25),
(4, 45),
(5, 33),
(6, 12),
(7, 77),
(8, 90),
(9, 66),
(10, 41),
(11, 50),
(12, 81),
(13, 35),
(14, 19),
(15, 57),
(16, 68),
(17, 21),
(18, 73),
(19, 89),
(20, 9),
(21, 60),
(22, 42),
(23, 88),
(24, 7),
(25, 32),
(26, 28),
(27, 55),
(28, 3),
(29, 40),
(30, 74),
(31, 13),
(32, 53),
(33, 15),
(34, 44),
(35, 85),
(36, 16),
(37, 69),
(38, 2),
(39, 36),
(40, 11),
(41, 62),
(42, 92),
(43, 37),
(44, 79),
(45, 86),
(46, 22),
(47, 30),
(48, 4),
(49, 47),
(50, 48),
(51, 54),
(52, 6),
(53, 75),
(54, 23),
(55, 5),
(56, 26),
(57, 63),
(58, 71),
(59, 49),
(60, 34),
(61, 31),
(62, 14),
(63, 87),
(64, 46),
(65, 76),
(66, 70),
(67, 20),
(68, 10),
(69, 59),
(70, 43),
(71, 67),
(72, 84),
(73, 52),
(74, 56),
(75, 29),
(76, 27),
(77, 64),
(78, 8),
(79, 61),
(80, 18),
(81, 72),
(82, 58),
(83, 17),
(84, 39),
(85, 38),
(86, 51),
(87, 24),
(88, 80),
(89, 78),
(90, 65),
(91, 91),
(92, 83),
(93, 82),
(94, 93),
(95, 95),
(96, 99),
(97, 98),
(98, 96),
(99, 100),
(100, 94);


INSERT INTO application (userId, programId, applied, accepted, denied)
VALUES (1, 1, TRUE, FALSE, FALSE),
       (4, 2, TRUE, TRUE, FALSE);


# Persona 1: Student
#1.1
INSERT INTO application (userId, programId, applied, accepted, denied)
VALUES
(1, 1, TRUE, FALSE, FALSE),
(4, 2, TRUE, TRUE, FALSE),
(7, 5, TRUE, FALSE, FALSE),
(12, 8, TRUE, TRUE, FALSE),
(15, 10, TRUE, FALSE, TRUE),
(20, 12, TRUE, FALSE, FALSE),
(25, 18, TRUE, TRUE, FALSE),
(30, 21, TRUE, FALSE, TRUE),
(35, 23, TRUE, TRUE, FALSE),
(40, 29, TRUE, FALSE, TRUE),
(45, 31, TRUE, TRUE, FALSE),
(50, 34, TRUE, FALSE, FALSE),
(55, 38, TRUE, TRUE, FALSE),
(60, 41, TRUE, FALSE, TRUE),
(65, 47, TRUE, TRUE, FALSE),
(70, 50, TRUE, FALSE, TRUE),
(75, 52, TRUE, TRUE, FALSE),
(80, 56, TRUE, FALSE, FALSE),
(85, 60, TRUE, TRUE, FALSE),
(90, 63, TRUE, FALSE, TRUE),
(2, 65, TRUE, FALSE, FALSE),
(5, 67, TRUE, TRUE, FALSE),
(8, 70, TRUE, FALSE, TRUE),
(11, 72, TRUE, TRUE, FALSE),
(14, 76, TRUE, FALSE, TRUE),
(18, 80, TRUE, TRUE, FALSE),
(22, 82, TRUE, FALSE, FALSE),
(26, 85, TRUE, TRUE, FALSE),
(29, 87, TRUE, FALSE, TRUE),
(33, 90, TRUE, TRUE, FALSE),
(37, 94, TRUE, FALSE, FALSE),
(41, 98, TRUE, TRUE, FALSE),
(44, 100, TRUE, FALSE, TRUE),
(48, 3, TRUE, TRUE, FALSE),
(52, 6, TRUE, FALSE, TRUE),
(56, 9, TRUE, TRUE, FALSE),
(60, 13, TRUE, FALSE, FALSE),
(64, 16, TRUE, TRUE, FALSE),
(68, 20, TRUE, FALSE, TRUE),
(72, 24, TRUE, TRUE, FALSE),
(76, 27, TRUE, FALSE, TRUE),
(80, 30, TRUE, TRUE, FALSE),
(84, 33, TRUE, FALSE, FALSE),
(88, 36, TRUE, TRUE, FALSE),
(91, 39, TRUE, FALSE, TRUE),
(95, 42, TRUE, TRUE, FALSE),
(3, 44, TRUE, FALSE, TRUE),
(6, 48, TRUE, TRUE, FALSE),
(9, 51, TRUE, FALSE, FALSE),
(13, 55, TRUE, TRUE, FALSE),
(16, 58, TRUE, FALSE, TRUE),
(20, 62, TRUE, TRUE, FALSE),
(24, 64, TRUE, FALSE, TRUE),
(28, 68, TRUE, TRUE, FALSE),
(32, 71, TRUE, FALSE, FALSE),
(36, 74, TRUE, TRUE, FALSE),
(39, 77, TRUE, FALSE, TRUE),
(43, 79, TRUE, TRUE, FALSE),
(47, 83, TRUE, FALSE, FALSE),
(51, 86, TRUE, TRUE, FALSE),
(54, 88, TRUE, FALSE, TRUE),
(58, 91, TRUE, TRUE, FALSE),
(62, 95, TRUE, FALSE, TRUE),
(66, 99, TRUE, TRUE, FALSE),
(69, 2, TRUE, FALSE, TRUE),
(73, 4, TRUE, TRUE, FALSE),
(77, 7, TRUE, FALSE, FALSE),
(81, 11, TRUE, TRUE, FALSE),
(85, 15, TRUE, FALSE, TRUE),
(89, 19, TRUE, TRUE, FALSE),
(92, 22, TRUE, FALSE, FALSE),
(96, 26, TRUE, TRUE, FALSE),
(100, 28, TRUE, FALSE, TRUE),
(4, 32, TRUE, TRUE, FALSE),
(8, 35, TRUE, FALSE, FALSE),
(12, 37, TRUE, TRUE, FALSE),
(16, 40, TRUE, FALSE, TRUE),
(20, 43, TRUE, TRUE, FALSE),
(24, 46, TRUE, FALSE, TRUE),
(28, 49, TRUE, TRUE, FALSE),
(32, 53, TRUE, FALSE, FALSE),
(36, 57, TRUE, TRUE, FALSE),
(40, 61, TRUE, FALSE, TRUE),
(44, 66, TRUE, TRUE, FALSE),
(48, 69, TRUE, FALSE, TRUE),
(52, 73, TRUE, TRUE, FALSE),
(56, 75, TRUE, FALSE, TRUE),
(60, 78, TRUE, TRUE, FALSE),
(64, 81, TRUE, FALSE, FALSE),
(68, 84, TRUE, TRUE, FALSE),
(72, 89, TRUE, FALSE, TRUE),
(76, 92, TRUE, TRUE, FALSE),
(80, 96, TRUE, FALSE, TRUE);


#1.2
DELETE
FROM application
WHERE userId = 5
  AND programId = 1;

#1.3
SELECT p.postAuthor, p.title, p.body, p.programId, p.userId
FROM post AS p
         JOIN postTag AS pt ON p.postId = pt.postId
         JOIN postTagParent pTP ON pt.postTagId = pTP.postTagId
WHERE pt.postTagId = 2;

#1.4
SELECT a.userId, p.programId, p.title, p.location, a.applied, a.accepted, a.denied
FROM application AS a
         JOIN program AS p ON a.programId = p.programId
WHERE a.userId = 5;

#1.5
SELECT p.programId,
       p.title,
       p.location,
       schoolId,
       professorId,
       p.programStart,
       p.programEnd,
       COUNT(a.accepted) AS totalApplications
FROM program p
         JOIN application a on p.programId = a.programId
GROUP BY p.programId;

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
SELECT p.programId, COUNT(a.applicationId) AS totalApplications
FROM program AS p
         LEFT JOIN application AS a ON p.programId = a.programId
WHERE p.professorId = (SELECT userId
                       FROM user
                       WHERE email = 'smith@example.edu')
GROUP BY p.programId;

#2.5
INSERT INTO application (userId, programId, applied, accepted, denied)
VALUES (1, 2, TRUE, FALSE, FALSE);

#2.6
UPDATE profile
SET bio        = 'Updated bio about courses taught, qualifications, etc.',
    middleName = 'Eras'
WHERE userId = (SELECT userId
                FROM user
                WHERE email = 'taylor@example.edu');

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
WHERE roleId = (SELECT r.roleId
                FROM (SELECT roleId FROM role WHERE name = 'Professor') AS r);

#3.5
DELETE
FROM user
WHERE firstName = 'Ben'
  AND lastName = 'June';

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
INSERT INTO program (title, location, schoolId, professorId, programStart, programEnd, approved, awaiting)
VALUES ('Dialogue: International Business Strategies', 'Japan', 2, 4, '2024-06-01', '2024-09-01', FALSE, TRUE);

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
FROM user u
         JOIN application a on u.userId = a.userId
WHERE schoolId = 2
  AND denied = true;