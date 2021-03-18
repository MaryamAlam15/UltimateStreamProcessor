class MongoConfig:
    WRITE_FORMAT = 'com.mongodb.spark.sql.DefaultSource'
    MODE_TO_WRITE = 'append'

    DATABASE_OPTIONS = {
        # hostname 'mongodb' is defined in docker-compose file.
        'uri': 'mongodb://mongodb:27017/',
        'database': 'ultimate_db',
        'collection': 'tweets'
    }
