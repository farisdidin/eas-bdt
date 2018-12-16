CREATE USER 'monitor'@'%' IDENTIFIED BY 'monitorpassword';
GRANT SELECT on sys.* to 'monitor'@'%';
FLUSH PRIVILEGES;

-- CREATE USER 'playgrounduser'@'%' IDENTIFIED BY 'playgroundpassword';
-- GRANT ALL PRIVILEGES on playground.* to 'playgrounduser'@'%';
-- FLUSH PRIVILEGES;

CREATE USER 'didin'@'%' IDENTIFIED BY 'didin';
GRANT ALL PRIVILEGES on easbdt.* to 'didin'@'%';
FLUSH PRIVILEGES;