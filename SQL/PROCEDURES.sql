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
SELECT conn.*, users.username
FROM dbo.CONNECTIONS conn
INNER JOIN dbo.USERS users
ON conn.User_Id2 = users.User_id
WHERE User_Id1 = @user_id

GO


EXECUTE GET_FRIENDS 1 ;