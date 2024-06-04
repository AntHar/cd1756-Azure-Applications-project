import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = 'stanhacms'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'ENTER_BLOB_STORAGE_KEY'
    BLOB_CONTAINER = 'cms-images'

    SQL_SERVER = 'sql-cloud-developer-azure-cms-server-anha.database.windows.net'
    SQL_DATABASE = 'sqldb-cms-anha'
    SQL_USER_NAME = 'sa_anha'
    SQL_PASSWORD = '!*wt6ixtK%RR2tE%ZDY$Nux5bPV&n5Tgyth^h4f8'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
<<<<<<< HEAD
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or "ENTER_CLIENT_SECRET_HERE"
=======
    CLIENT_SECRET = "C0V8Q~QyRs_KNUDnjDLkId6ZEwkzOuTmlmV2ya3m"
>>>>>>> 614e547 (update config.py)
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    # AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/94089105-2be4-4fe5-8d3b-0601c50bb35c"

    CLIENT_ID = "bc6284ca-bb7a-43a4-a91a-23c3b4a41f2e"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
