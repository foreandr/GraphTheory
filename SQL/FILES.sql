SELECT * FROM dbo.FILES;
DROP TABLE FILES;

GO
CREATE TABLE FILES
(
	File_id INT IDENTITY(1, 1),   
	File_PATH varchar(200),
	UserId INT NOT NULL,
	Date_Time DATETIME DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (UserId) REFERENCES USERS(User_Id),
	PRIMARY KEY (File_id)
)
GO


GO
ALTER PROCEDURE dbo.GET_FILE_ID
		@uploader_username varchar(200),
		@file_name varchar(200)
	AS
	BEGIN
		SELECT * 
		FROM dbo.FILES files
		INNER JOIN USERS users
		ON users.User_Id = files.UserId
		WHERE users.username = @uploader_username
		AND files.File_PATH LIKE '%' +  @file_name+ '%'
	END
GO

EXECUTE dbo.GET_FILE_ID 'foreandr', 'CSV1.csv';


