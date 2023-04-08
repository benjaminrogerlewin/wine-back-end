-- settings.sql
CREATE DATABASE thevine;
CREATE USER thevineuser WITH PASSWORD 'thevine';
GRANT ALL PRIVILEGES ON DATABASE thevine TO thevineuser;