-- TABLES
select * from dbo.USERS;

CREATE TABLE dbo.USERS
(
	User_Id INT IDENTITY(1, 1),
	username varchar(200),
	password varchar(200),
	email varchar(200),
	PRIMARY KEY (User_Id)
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








-- DROP ORDER
drop table dbo.IMAGES;
drop table dbo.LIKES;
drop table dbo.COMMENTS;
drop table dbo.POSTS;
drop table dbo.USERS;
-- VISUALIZING TABLES
	-- Right-click the table or the view in the Object Explorer panel
	-- From the context menu choose Script Table as.../CREATE to.../< SomeDestination 