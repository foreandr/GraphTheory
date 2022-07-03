-- INSERTIONS

-- USERS
INSERT INTO dbo.USERS
(username, password, email)
VALUES
('foreandr', 'cooldood', 'foreandr@gmail.com'),
('andrfore', '77734381', 'andrfore@gmail.com'),
('cheatsie', 'doodmanman', 'cheatsieog@gmail.com'),
('dnutty', 'helloworld', 'dnutty@gmail.com'),
('bigfrog', 'helloworld', 'bigfrog@gmail.com');

-- CONNECTIONS
DELETE FROM dbo.CONNECTIONS;
INSERT INTO dbo.CONNECTIONS
(User_Id1, User_Id2)
VALUES
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(2, 3),
(2, 4),
(2, 5),
(3, 4);


-- IMAGES
INSERT INTO dbo.IMAGES(Image_Type, Image_PATH, UserId)
VALUES ('profile', 'GraphTheory\#DemoData', (SELECT User_Id from USERS WHERE User_Id = 17));

-- POSTS
INSERT INTO dbo.POSTS(Title,  UserId)
VALUES ('DemoTitle', (SELECT User_Id from USERS WHERE User_Id = 17));

-- LIKES 
INSERT INTO dbo.lLIKES(User_Id,  Post_Id, Comment_Id)
VALUES (dbo.SELECT_ID(10), dbo.SELECT_POST_ID(10), dbo.SELECT_COMMENT_ID(10));



-- COMMENTS

SELECT * FROM dbo.USERS;
SELECT * FROM dbo.IMAGES;
SELECT* FROM dbo.POSTS;
DELETE FROM dbo.USERS;
