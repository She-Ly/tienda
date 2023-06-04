class Config:
    SECRET_KEY='Indila1998'
class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_DB='tienda'

config ={
    'development' : DevelopmentConfig,
    'default':DevelopmentConfig
}