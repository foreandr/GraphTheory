-- INSERTIONS

-- USERS
INSERT INTO dbo.USERS
(username, password, email)
VALUES
('foreandr', 'cooldood', 'foreandr@gmail.com'),
('andrfore', '77734381', 'andrfore@gmail.com'),
('cheatsie', 'doodmanman', 'cheatsieog@gmail.com'),
('dnutty', 'helloworld', 'dnutty@gmail.com'),
('bigfrog', 'helloworld', 'bigfrog@gmail.com');

INSERT INTO dbo.IMAGES
(Image_Type, Image_PATH, UserId) --C:\Users\forea\PycharmProjects\GraphTheory\#DemoData
VALUES
('profile', 'GraphTheory\#DemoData', 1),
('profile', 'GraphTheory\#DemoData', 2),
('profile', 'GraphTheory\#DemoData', 3),
('profile', 'GraphTheory\#DemoData', 4),
('profile', 'GraphTheory\#DemoData', 5);



SELECT * FROM dbo.USERS;
DELETE FROM dbo.USERS;