from sqlalchemy import create_engine
import os


def get_engine():
    """
    Create and return a SQLAlchemy engine for PostgreSQL database.
    Uses environment variables or defaults for connection.
    """
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5400")
    database = os.getenv("POSTGRES_DB", "northwind")

    connection_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(connection_string)

    return engine
