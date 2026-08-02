-- Initial database initialization script if needed
SELECT 'CREATE DATABASE aios_db' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'aios_db')\gexec
