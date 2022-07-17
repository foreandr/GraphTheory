-- USERS

SELECT * FROM dbo.USERS;

DELETE FROM dbo.USERS;



SELECT * 
FROM USERS
WHERE email = 'foreandr@gmail.com'
AND password = 'cooldood'

SELECT users.username 
FROM dbo.USERS users;

DROP TABLE dbo.USERS;

CREATE TABLE dbo.USERS
(
	User_Id INT IDENTITY(1, 1),
	username varchar(200) UNIQUE,
	password varchar(200),
	email varchar(200),
	PRIMARY KEY (User_Id)
);

INSERT INTO dbo.USERS
(username, password, email)
VALUES
('foreandr', 'cooldood', 'foreandr@gmail.com'),
('andrfore', '77734381', 'andrfore@gmail.com'),
('cheatsie', 'doodmanman', 'cheatsieog@gmail.com'),
('dnutty', 'helloworld', 'dnutty@gmail.com'),
('bigfrog', 'helloworld', 'bigfrog@gmail.com');

