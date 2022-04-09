# Twitter Unfollow All Friends

## Twitter API keys
Before calling the twitter API, you must have a Twitter Developer account and a set of keys and tokens. 
https://developer.twitter.com/en/portal/dashboard
This should only take 5 minutes or so

In developer portal, select your project. User authentication settings -> edit
-> OAuth 1.0a, choose read-write. 

Callback url: http://localhost:3000 , Website url: just filled in smth random (e.g. my facebook page yikes ..)

Under keys and tokens:
take note of 
- API key and secret
- generate your access token and secret

-> fill these in into config.ini (without quotes !!)

## Script Configuration
The project comes with an config.ini file that you can use to fill with your own Twitter API credentials.
!! Use no quotes around the parameters

```
### Configuration parameters
* **API.Key and API.Secret**
* **Access.Token and Access.Secret
* **General.ScreenName**: your twitter account screen name, e.g. @xyz
* **General.BatchSize**: the maximum number of friend accounts you wish to be able to remove on each run. 
```

(Regarding BatchSize: Probably best to not delete all friends you are following at once. It might be that twitter limits the number of friends you can unfollow during a certain time, not sure about that.)

## Python
Obviously you need Python to run this: https://www.python.org/downloads/

## Files
put all files (config.ini, requirements.txt, program.py) in the same folder 

## Install required packages
The script works with the following python packages:
* Tweepy
* configmanager

The required dependencies are on the **requirements.txt** file. To install them run the following in the command line (in the folder where you put all the files):
```
python3 -m pip install --user -r requirements.txt
```

## Run program
(run on command line)
```
python3 program.py
```
