## UltimateStreamProcessor

This app is to demonstrate the way we could process live stream data (example: Twitter) and store it in some DB.
It also merges tweets with total coronavirus cases as displayed on [worldometers](https://www.worldometers.info/coronavirus/).

### How it works:
- The app reads the live tweets from Twitter Stream via socket and buffers them upto 15mins.
- After fetching the tweets, it then cleans them. i.e remove '#', 'RT:' and any urls included.
- The app also fethes the total coronavirus cases as mentioned on [worldometers](https://www.worldometers.info/coronavirus/).
- cleaned tweets are merged with coronavirus total cases along with the timestamp.

#### An Example of final record:

#### TechStack:
 - python3.8
 - Pyspark
 - Mongo DB
 
### How to run:
The app is dockerized and can be build as:
> docker compose-up --build

If you just want to run:
> docker compose-up
