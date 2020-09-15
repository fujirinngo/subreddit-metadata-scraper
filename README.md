# Subreddit Metadata Scraper
A scraper that uses PRAW (Python Reddit API Wrapper) to return a .jsonl file of  metadata for subreddits that use the Subreddit Rules Widget (see: https://mods.reddithelp.com/hc/en-us/articles/360010364372-Sidebar-Widgets)

## Contents
**2020-07-31-top50.csv**: list of the top 50 subreddits as of July 31, 2020 to be used for testing (pulled from https://redditmetrics.com/list-all-subreddits)

**70k-subreddits.csv**: a list of ~70,000 subreddits that used the Rules Widget in Sept. 2019

**metadata_scraper.py**: the scraper; takes in a .csv file with a list of subreddits as its first column and outputs a .jsonl file with the metadata for each subreddit
- metadata extracted: subreddit name, scraped date (as a unix timestamp), rules, subscriber count, created date (as a unix timestamp), and language
- a list of subreddits that could not be scraped (due to not having rules widget or being quarantined/banned) added at the end

**sample_output.jsonl**: example of what output file will look like; result of passing **2020-07-31-top50.csv** through the scraper

## Prerequisites 
### Packages
Required packages: **praw**

If this scraper is being used on a local machine run: 

<code>pip install praw</code>

If this scraper is being run on an Ubuntu server run:

<code>$ sudo apt-get update -y</code>

<code>$ sudo apt-get install -y python3-praw</code>

(Source: https://zoomadmin.com/HowToInstall/UbuntuPackage/python3-praw

### Set-up for PRAW
Since PRAW uses the Reddit API, the following steps are necessary: 
1) Access a Reddit account (if you do not have one sign up at https://reddit.com)
2) Follow this guide to create an application and get a client ID and client secret. 
3) Replace the strings "CLIENT ID HERE", "CLIENT SECRET HERE", "APP NAME HERE" in lines 9 and 10 of **metadata_scraper.py** with your client ID, client secret, and app name in step 2 

## Running the Scraper
The scraper requires two command line arguments: (1) the .csv file with the list of subreddits (2) a name for the output file.

Example:
<code>$ python metadata_scraper.py 2020-07-31-top50.csv top50-output.jsonl</code>

Running this on the command line will scrape the subreddits in **2020-07-31-top50.csv** and write the output in a file named **top50-output.jsonl**.

