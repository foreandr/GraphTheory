SELECT * FROM dbo.MODEL;
DROP TABLE dbo.MODEL;

CREATE TABLE dbo.MODEL(
	Modal_id INT IDENTITY(1,1) NOT NULL,
	Local_File_PATH varchar(200) NULL,
	Date_Time datetime NULL,
	Foreign_File_id int NULL,
	Uploader varchar(200) NULL,
	FOREIGN KEY (Foreign_File_id) REFERENCES FILES(File_id),
	FOREIGN KEY (Uploader) REFERENCES USERS(Username),
	PRIMARY KEY (Modal_id)
)

-- demo insert
INSERT INTO dbo.MODEL(Local_File_PATH, Date_Time, Foreign_File_id, Uploader) -- can be png or jpg, or mp4
VALUES ('/PATH.JPG', GETDATE(), 2, 'foreandr') 

GO
CREATE PROCEDURE dbo.CUSTOM_MODEL_INSERT
	@model_path varchar(200),
	@foreign_file_id INT,
	@personal_username varchar(200)
AS
INSERT INTO dbo.MODEL(Local_File_PATH, Date_Time, Foreign_File_id, Uploader) -- can be png or jpg, or mp4
VALUES (@model_path, GETDATE(), @foreign_file_id, @personal_username) 
GO