To install this on your machine, please follow the following steps:
1. Install Postgresql, gdal-bin, postgis from package manager.
2. Set up the database as seen on smarttourist.settings-> Make touristdbuser superuser by 'ALTER ROLE touristdbuser SUPERUSER;;'
3. If GDAL is not installed, you can ignore it.
4. Run makemigrations and migrate then.
5. To populate database, run the todb.py file.