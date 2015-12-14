Step-by-Step Setup Instructions (Run all instructions as root where applicable)

1) Create instance with only 10GB root using ucbw205_complete_plus_postgres_PY2.7
	Ports: 4040, 50070, 8080, 22, 10000, 8020, 8088
2) Follow Appendix instructions to install Python 2.7 (Bottom of page 10)
3) Follow Appendix instructions to install Streamparse (Page 9)
4) Run pip install psycopg2
5) Run pip install tweepy
6) Run wget https://s3.amazonaws.com/ucbdatasciencew205/setup_ucb_complete_plus_postgres.sh
7) Run bash setup_ucb_complete_plus_postgres.sh /dev/xvdb (or a different last argument if /dev/xvdb is not the name of your disk)
8) Clone my git repository: 
	SSH: git@github.com:eperkins1/exercise_2.git
	OR
	HTTPS: https://github.com/eperkins1/exercise_2.git
9) Create Postgres database “tcount”
	Run the following commands to create Tcount database:
		psql -U postgres
		CREATE DATABASE Tcount;
		\q
10) Run stream:
	cd into exercise_2 repo
	cd into EX2Tweetwordcount folder, and run “sparse run”
	Keep it running for as long as you’d like to build up the table
11) Run either of the python files, with option argument for finalresults.py:
	histogram.py
	finalresults.py
12) To create the Plot.png, import matplotlib and numpy by running the following commands, in the EX2Tweetwordcount directory:
	mkdir /usr/local/lib/temph/
	mv /usr/local/lib/libpython2.7.a /usr/local/lib/temph/
	pip install numpy
	pip install matplotlib
	mv /usr/local/lib/temph/libpython2.7.a /usr/local/lib/
	python t20plot.py
