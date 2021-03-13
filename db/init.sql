CREATE DATABASE userdb;
use userdb;

CREATE TABLE githubcredentials (
  uid INTEGER,
  token VARCHAR(50)
);

INSERT INTO githubcredentials
  (uid, token)
VALUES
  (1, '5047627c3b3b98bb7da1dded546933c0f2bebd86');
