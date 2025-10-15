class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/blog_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "clave_secreta_123" 