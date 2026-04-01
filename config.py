class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tutor.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "chave_secreta"