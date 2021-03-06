SELECT * FROM dbo.CSV_VOTES;
DROP TABLE CSV_VOTES;

GO
CREATE TABLE dbo.CSV_VOTES(
	CSV_Vote_Id INT IDENTITY(1, 1),
	File_id INT,
	Voter_Username varchar(50) UNIQUE, -- so there can only be one vote per person
	FOREIGN KEY (File_id) REFERENCES FILES(File_id),
	PRIMARY KEY (CSV_Vote_Id)
)
GO

GO
ALTER PROCEDURE dbo.ENTER_CSV_VOTE
	@file_id BIGINT,
	@voter VARCHAR(200)
-- VOTES
AS
INSERT INTO dbo.CSV_VOTES(File_id, Voter_Username)
VALUES(@file_id, @voter)
GO

