SELECT * FROM dbo.CONNECTIONS;
drop table dbo.CONNECTIONS;

CREATE TABLE dbo.CONNECTIONS
(
	Friendship_Id INT IDENTITY(1, 1),
	User_Id1 INT,
	User_Id2 INT,
	
	FOREIGN KEY (User_Id1) REFERENCES USERS(User_Id),
	FOREIGN KEY (User_Id2) REFERENCES USERS(User_Id),
	PRIMARY KEY (Friendship_Id, User_Id1, User_Id2)
);

select conn.*, us1.username as 'USERNAME1', us2.username as 'USERNAME2'
from dbo.CONNECTIONS conn
inner join users us1
on conn.User_Id1 = us1.User_Id
inner join users us2
on conn.User_Id2 = us2.User_Id


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