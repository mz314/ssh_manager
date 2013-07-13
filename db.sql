PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE ssh(id int primary key asc,un varchar(255),pw text,host varchar(255),title varchar(255));
INSERT INTO "ssh" VALUES(1,'testusr','testpass','testhost','testtitle');
COMMIT;
