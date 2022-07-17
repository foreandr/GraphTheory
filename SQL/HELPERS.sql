-- HELPERS
GO
SELECT name AS procedure_name   
    ,SCHEMA_NAME(schema_id) AS schema_name  
    ,type_desc  
    ,create_date  
    ,modify_date  
FROM sys.procedures; 

SELECT * FROM information_schema.TABLES;

GO

GO
ALTER PROCEDURE dbo.GET_FRIENDS
@username VARCHAR(200)
AS
SELECT conn.*, users.*, users2.*
FROM dbo.CONNECTIONS conn

INNER JOIN dbo.USERS users
ON conn.User_Id1 = users.User_Id

INNER JOIN dbo.USERS users2
ON conn.User_Id2 = users2.User_id

where users.username = @username
EXECUTE dbo.GET_FRIENDS 'foreandr';

GO

GO
ALTER PROCEDURE dbo.GET_FILES
@username VARCHAR(200)
AS
SELECT files.*, users.*
FROM dbo.FILES files

INNER JOIN dbo.USERS users
ON files.UserId = users.User_Id

where users.username = @username
GO

GO
ALTER PROCEDURE dbo.CUSTOM_INSERTION
--parameters
@host_Id INT,
@other_Id INT
AS
INSERT INTO dbo.CONNECTIONS
(User_Id1, User_Id2)
VALUES
(@host_Id, @other_Id);

INSERT INTO dbo.CONNECTIONS
(User_Id1, User_Id2)
VALUES
(@other_Id, @host_Id);
GO

GO
ALTER PROCEDURE dbo.GET_USER_ID
@username varchar(200)
AS
SELECT users.User_Id 
FROM dbo.USERS users
WHERE users.username = @username
GO

GO
ALTER PROCEDURE dbo.GET_ALL_DATASETS_BY_DATE
	@top INT
AS
SELECT top (@top) users.username, files.File_PATH AS 'Path', files.Description AS 'Desc', files.Date_Time as 'Date', files.File_size as SIze
FROM dbo.USERS users
INNER JOIN dbo.FILES files
ON files.UserId = users.User_Id
ORDER BY files.Date_Time;
GO

GO
ALTER PROCEDURE dbo.CHANGE_PASSWORD_FOR_EMAIL
	@email VARCHAR(200),
	@password VARCHAR(200)
AS
UPDATE dbo.USERS
SET password = @password
WHERE dbo.USERS.email = @email;
GO

GO
ALTER PROCEDURE dbo.GET_FILE_VOTE_COUNT
	@file_id BIGINT
	AS
	SELECT COUNT(*)
	FROM dbo.CSV_VOTES
	WHERE File_id = @file_id
GO


EXECUTE GET_FRIENDS 'foreandr';
EXECUTE GET_FILES 'foreandr';
EXECUTE dbo.GET_ALL_DATASETS_BY_DATE 100

