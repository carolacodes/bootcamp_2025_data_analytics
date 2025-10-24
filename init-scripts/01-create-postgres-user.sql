DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'postgres') THEN
        CREATE USER postgres WITH SUPERUSER PASSWORD '${POSTGRES_PASSWORD}';
    END IF;
END
$$;
