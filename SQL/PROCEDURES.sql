SELECT name AS procedure_name   
    ,SCHEMA_NAME(schema_id) AS schema_name  
    ,type_desc  
    ,create_date  
    ,modify_date  
FROM sys.procedures;  

DROP PROCEDURE SELECT_COMMENT_ID;  
GO 
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

WHERE User_Id1 = @user_id
GO


EXECUTE GET_FRIENDS 1 ;