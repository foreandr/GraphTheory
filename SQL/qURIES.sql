-- TABLES
select * from USERS;
SELECT * FROM dbo.CONNECTIONS;
SELECT * FROM dbo.FILES;
SELECT * FROM information_schema.TABLES



select conn.*, us1.username as 'USERNAME1', us2.username as 'USERNAME2'
from dbo.CONNECTIONS conn
inner join users us1
on conn.User_Id1 = us1.User_Id
inner join users us2
on conn.User_Id2 = us2.User_Id



SELECT * 
FROM USERS
WHERE email = 'foreandr@gmail.com'
AND password = 'cooldood'


CREATE TABLE dbo.USERS
(
	User_Id INT IDENTITY(1, 1),
	username varchar(200) UNIQUE,
	password varchar(200),
	email varchar(200),
	PRIMARY KEY (User_Id)
);

CREATE TABLE dbo.CONNECTIONS
(
	Friendship_Id INT IDENTITY(1, 1),
	User_Id1 INT,
	User_Id2 INT,
	
	FOREIGN KEY (User_Id1) REFERENCES USERS(User_Id),
	FOREIGN KEY (User_Id2) REFERENCES USERS(User_Id),
	PRIMARY KEY (Friendship_Id, User_Id1, User_Id2)
);

CREATE TABLE dbo.IMAGES (
	Image_Id INT IDENTITY(1, 1),
	Image_Type varchar(200),      
	Image_PATH varchar(200),
	UserId INT NOT NULL,
	FOREIGN KEY (UserId) REFERENCES USERS(User_Id),
	PRIMARY KEY (Image_Id)
);

CREATE TABLE dbo.POSTS (
	Post_Id INT IDENTITY(1, 1),
	Title varchar(200), 
	UserId INT NOT NULL,
	FOREIGN KEY (UserId) REFERENCES USERS(User_Id),
	PRIMARY KEY (Post_Id)
);

CREATE TABLE dbo.COMMENTS (
	Comment_Id INT IDENTITY(1, 1),
	User_Id INT, 
	Post_Id INT, 
	FOREIGN KEY (User_Id) REFERENCES USERS(User_Id) ,
	FOREIGN KEY (Post_Id) REFERENCES POSTS(Post_Id),
	FOREIGN KEY (Comment_Id) REFERENCES COMMENTS(Comment_Id),
	PRIMARY KEY (Comment_Id)
);

CREATE TABLE dbo.LIKES (
	Like_Id INT IDENTITY(1, 1),
	User_Id INT, 
	Post_Id INT, 
	Comment_Id INT, 
	FOREIGN KEY (User_Id) REFERENCES USERS(User_Id),
	FOREIGN KEY (Post_Id) REFERENCES POSTS(Post_Id),
	FOREIGN KEY (Comment_Id) REFERENCES COMMENTS(Comment_Id),
	PRIMARY KEY (Like_Id)

);
ALTER TABLE dbo.LIKES
	ADD CONSTRAINT check_one_is_not_null
	CHECK (
		 (User_Id IS NOT NULL OR Post_Id IS  NOT NULL)
);

DROP TABLE FILES;
CREATE TABLE FILES
(
File_id INT IDENTITY(1, 1),   
File_PATH varchar(200),
UserId INT NOT NULL,
Date_Time DATETIME DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (UserId) REFERENCES USERS(User_Id),
PRIMARY KEY (File_id)
)

INSERT INTO dbo.FILES
(File_PATH, UserId)
VALUES
('no string', 1)


-- DROP ORDER
drop table dbo.IMAGES;
drop table dbo.LIKES;
drop table dbo.COMMENTS;
drop table dbo.POSTS;
drop table dbo.USERS;
drop table dbo.CONNECTIONS;
-- VISUALIZING TABLES
	-- Right-click the table or the view in the Object Explorer panel
	-- From the context menu choose Script Table as.../CREATE to.../< SomeDestination 