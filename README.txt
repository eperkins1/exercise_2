Step-by-Step Setup Instructions

1) Create instance with only 10GB root using ucbw205_complete_plus_postgres_PY2.7
	Ports: 4040, 50070, 8080, 22, 10000, 8020, 8088
2) Follow Appendix instructions to install Python 2.7 and streamparse, as root throughout this exercise
3) Run pip install psycopg2
4) Run pip install tweepy
5) Run wget https://s3.amazonaws.com/ucbdatasciencew205/setup_ucb_complete_plus_postgres.sh
6) Run bash setup_ucb_complete_plus_postgres.sh /dev/xvdb (or a different last argument if /dev/xvdb is not the name of your disk)
7) Clone my git repository: 
	SSH: git@github.com:eperkins1/exercise_2.git
	OR
	HTTPS: https://github.com/eperkins1/exercise_2.git
8) Create Postgres database “tcount”
	Run the following commands to create Tcount database:
		psql -U postgres
		CREATE DATABASE Tcount;
		\q
9) Run stream:
	cd into EX2Tweetwordcount folder, and run “sparse run”
	Keep it running for as long as you’d like to build up the table
10) Run any of the python files that will produce output required, including:
	histogram.py
	finalresults.py
	t20plot.py
