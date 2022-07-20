SELECT * FROM dbo.MODEL;
DROP TABLE dbo.MODEL;

CREATE TABLE dbo.MODEL(
	Model_id INT IDENTITY(1,1) NOT NULL,
	Local_File_PATH varchar(200),
	Model_Description varchar(400),
	Date_Time datetime NULL,
	Foreign_File_id int NULL,
	Uploader varchar(200) NULL,
	FOREIGN KEY (Foreign_File_id) REFERENCES FILES(File_id),
	FOREIGN KEY (Uploader) REFERENCES USERS(Username),
	PRIMARY KEY (Model_id)
)

-- demo insert
INSERT INTO dbo.MODEL(Local_File_PATH, Date_Time, Foreign_File_id, Uploader) -- can be png or jpg, or mp4
VALUES ('/PATH.JPG', GETDATE(), 2, 'foreandr') 

GO
ALTER PROCEDURE dbo.CUSTOM_MODEL_INSERT
	@model_path varchar(200),
	@model_description 	VARCHAR(400),
	@foreign_file_id INT,
	@personal_username varchar(200)

AS
INSERT INTO dbo.MODEL(Local_File_PATH, Date_Time,Model_Description, Foreign_File_id, Uploader) -- can be png or jpg, or mp4
VALUES (@model_path, GETDATE() ,@model_description, @foreign_file_id, @personal_username) 
GO

EXECUTE dbo.CUSTOM_MODEL_INSERT '/PATH.JPG', 'desc', 2 , 'foreandr';



GO
ALTER PROCEDURE dbo.GET_MODELS_BY_FILE_ID
		@file_id INT
	AS
	BEGIN
		SELECT 
			model.Model_id,
			model.Local_File_PATH,
			model.Model_Description,
			model.Date_Time,
			model.Foreign_File_id,
			model.Uploader as 'MODEL UPLOADER',
			users.User_Id AS 'MODEL USER ID', 
			files.File_PATH AS 'CSV FILE PATH', 
			files.File_size, files.Description, 
			files.UserId AS 'CSV USER ID', 
			files.Date_Time AS 'CSV UPLOAD DATE',
			COUNT(mod_votes.Voter_Username) AS 'NUM VOTES'
		FROM dbo.MODEL model
		INNER JOIN dbo.USERS users
		ON model.Uploader = users.username
		INNER JOIN dbo.FILES files
		ON model.Foreign_File_id = files.File_id
		INNER JOIN dbo.MODEL_VOTES mod_votes
		ON model.Model_id = mod_votes.Model_id

		WHERE files.File_id = @file_id
	END
GO

EXECUTE dbo.GET_MODELS_BY_FILE_ID 2




