## UltimateStreamProcessor

This app is to demonstrate the way we could process live stream data (example: Twitter) and store it in some DB.
It also merges tweets with total coronavirus cases as displayed on [worldometers](https://www.worldometers.info/coronavirus/).

### How it works:
- The app reads the live tweets from Twitter Stream via socket and buffers them upto 15mins.
- After fetching the tweets, it then cleans them. i.e remove '#', 'RT:' and any urls included.
- The app also fethes the total coronavirus cases as mentioned on [worldometers](https://www.worldometers.info/coronavirus/).
- cleaned tweets are merged with coronavirus total cases along with the timestamp.

#### An Example of final record:
~~~
{
   "_id":"ObjectId(""6053dfa3c99e3f43208409da"")",
   "time_stamp":"ISODate(""2021-03-18T23:17:30Z"")",
   "total_case_count":"122,331,822",
   "content":[
      "It showed a lady fitted out with a fur hat and fur boa who sat upright, raising a heavy fur muff that covered the whole of her lower arm towards the viewer.",
      "A collection of textile samples lay spread out on the table - Samsa was a travelling salesman - and above it there hung a picture that he had recently cut out of an illustrated magazine and housed in a nice, gilded frame.",
      "It wasn't a dream.",
      "It wasn't a dream.",
      "Gregor then turned to look out the window at the dull weather.",
      "\"What's happened to me?\" he thought.",
      "It showed a lady fitted out with a fur hat and fur boa who sat upright, raising a heavy fur muff that covered the whole of her lower arm towards the viewer."
   ]
}
~~~

#### TechStack:
 - python3.8
 - Pyspark
 - Mongo DB
 
### How to run:
The app is dockerized and can be build as:
> docker compose-up --build

If you just want to run:
> docker compose-up
