create database imagerepo;
use imagerepo;
CREATE TABLE images (
  link VARCHAR(200),
  title VARCHAR(50),
  alt_text VARCHAR(200)
);
INSERT INTO images
  (link, title, alt_text)
VALUES
  ('https://kuviasuomesta.fi/wp-content/uploads/2022/02/polku-kuviasuomesta.fi-roine-piirainen-1-scaled.jpg', 'Finnish forest and pond','Wooden trail in finnish forest next to a pond, picture taken in summer.'),
  ('https://kuviasuomesta.fi/wp-content/uploads/2021/04/poro4-kuvia-suomesta-ksenia-senkova-scaled.jpg', 'Reindeer at winter', 'Reindeer taking a break.');