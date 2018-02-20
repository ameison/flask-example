
SECRET_KEY = "q7^7_i@oo3iwbp-sfts-89k_ch8f687%!io*tz_n^t0t!0=p@h"
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@192.168.1.2:5432/osf_dev'


class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}