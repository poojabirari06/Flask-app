from app import db, app

# Assuming your Flask app is initialized in your_flask_app_file.py
# and your SQLAlchemy database instance is named db

def create_database_tables():
    with app.app_context():
        # This will create all tables as defined in your models
        db.create_all()

if __name__ == '__main__':
    create_database_tables()
    print("All tables created successfully!")
