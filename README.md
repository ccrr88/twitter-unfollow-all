# Twitter Unfollow All Friends

(forked from ozzie-eu and adapted to unfollow all friends (except those specified in doNotUnfollow.csv). Debugged and tested for a test account)

## Twitter API keys
Before calling the twitter API, you must have a Twitter Developer account and a set of keys and tokens. All this should only take 10 minutes or so.

Make a developer account here: https://developer.twitter.com/en/portal/dashboard

After you have your developer account, do the following:
In developer portal, select your project. User authentication settings -> edit
-> OAuth 1.0a, choose read-write. 

Fill in the following: Callback url: http://localhost:3000 , Website url: just filled in smth random (e.g. my facebook page yikes ..)

Under keys and tokens:
take note of 
- API key and secret
- generate your access token and secret

-> fill these in into config.ini (without quotes !!)

## Script Configuration
The project comes with a config.ini file that you can use to fill with your own Twitter API credentials.

!! Use no quotes around the parameters

```
### Configuration parameters
* API.Key and API.Secret
* Access.Token and Access.Secret
* General.ScreenName: your twitter account screen name without the @, e.g. xyz
* General.BatchSize: the maximum number of friend accounts you wish to be able to remove on each run. 
```

(Regarding BatchSize: Probably best to not delete all friends you are following at once. It might be that twitter limits the number of friends you can unfollow during a certain time, not sure about that.)

## Exceptions: accounts that you don't want to unfollow
In the csv file doNotUnfollow.csv you can list the accounts that you don't want to unfollow (screen name without the @)

## Python
Obviously you need Python to run this: https://www.python.org/downloads/

## Files
put all files (config.ini, requirements.txt, program.py, doNotUnfollow.csv) in the same folder 

## Install required packages
The required dependencies are on the **requirements.txt** file. To install them run the following in the command line (in the folder where you put all the files):
```
python3 -m pip install --user -r requirements.txt
```

## Run program
(run on command line)
```
python3 program.py
```
