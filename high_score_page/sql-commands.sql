CREATE TABLE scores (  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  score int NOT NULL);


INSERT INTO 
    scores (name, score)
VALUES
    ('annie', 2000), 
    ('bettie Aviv', 1300),
    ('cennie', 1500);



SELECT * FROM scores;