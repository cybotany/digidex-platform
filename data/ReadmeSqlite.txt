Instructions for ITIS Database Sqlite Download 

1. A Sqlite database library or command line shell is required 
   to use this data file. If you want this on your local system,
   download and install Sqlite database tools from
   http://www.sqlite.org/download.html. 

Note: Downloads and installation instructions are provided on 
      the Sqlite site. The ITIS staff doesn't provide 
      installation or usage support for Sqlite.

2. Download the latest ITIS Sqlite zip file (itisSqlite.zip)
   from http://www.itis.gov/downloads. This file is normally updated
    monthly on the last day of the month. 

3. Use an archive tool, Finder, or Windows Explorer to unzip
   the ITIS data file. This will create a folder containing
   the data installation files.


Installation Instructions for All Platforms.

Caution: If you copy this new ITIS Sqlite data over 
   any existing data named "ITIS.sqlite", that data
   will be permanently removed from your system and 
   the new data will replace it. If this is not what you
   want, you should investigate backup and/or data 
   preservation options prior to loading the new data.

1. Open a terminal or command prompt and navigate to 
   the folder where you unzipped the ITIS download file.

2. Copy the new ITIS.sqlite file to the folder where you want
   to store the ITIS data.

3. Change to the destination folder and enter the following:

      sqlite3 ITIS.sqlite
  
4. The sqlite command line shell will start and you will be able to 
   run SQL queries against the ITIS data.
