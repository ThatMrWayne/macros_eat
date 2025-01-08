SELECT 'CREATE DATABASE macroseat'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'macroseat')\gexec