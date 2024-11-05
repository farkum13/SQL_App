from sqlalchemy import create_engine, text, URL, CreateEnginePlugin
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base

# Database URL
conn_string = "host='localhost' dbname='my_database' user='postgres' password='secret'"
DATABASE_URL = "postgresql://jsqapp:3mta3@localhost:5432/postgres"
#DATABASE_URL = "jdbc:postgresql://localhost:5432/postgress"  # Update this line
# jdbc:postgresql://localhost:5432/jsq
# jsqapp
# 3mta3

# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def check_connection():
    """Check if the database connection is successful."""
    try:
        # Create a connection
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))  # Use text() to create an executable object
        print("Database connected successfully.")
    except OperationalError as e:
        print(f"Database connection failed: {e}")

def get_db():
    """Dependency that provides a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Create database tables."""
    Base.metadata.create_all(bind=engine)