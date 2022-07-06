SELECT name AS procedure_name   
    ,SCHEMA_NAME(schema_id) AS schema_name  
    ,type_desc  
    ,create_date  
    ,modify_date  
FROM sys.procedures;  

DROP PROCEDURE SELECT_COMMENT_ID;  
GO 
/*

GO
ALTER PROCEDURE dbo.GET_FRIENDS
@user_id INT
AS
SELECT conn.*, users1.username AS Host_Username ,users2.username AS Friend_Username
FROM dbo.CONNECTIONS conn

INNER JOIN dbo.USERS users1
ON conn.User_Id1 = users1.User_id

INNER JOIN dbo.USERS users2
ON conn.User_Id2 = users2.User_id

WHERE conn.User_Id1 = @user_id
GO
*/
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

EXECUTE dbo.GET_FILES foreandr;

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



EXECUTE  dbo.CUSTOM_INSERTION 1, 2 ;
EXECUTE  dbo.CUSTOM_INSERTION 1, 3 ;
EXECUTE  dbo.CUSTOM_INSERTION 1, 4 ;
EXECUTE  dbo.CUSTOM_INSERTION 1, 5 ;