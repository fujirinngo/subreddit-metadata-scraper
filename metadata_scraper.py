import praw
import csv
import json
from datetime import datetime
import sys

from typing import Dict

reddit = praw.Reddit(client_id="CLIENT ID HERE", client_secret="CLIENT SECRET HERE",
                     user_agent="APP NAME HERE") # replace these with your app's client ID, client secret, and name

def get_subr_data(subr_name :str) -> Dict[str, str]:
    subreddit = reddit.subreddit(subr_name)
    print(f"Currently processing {subreddit}")
    widgets = subreddit.widgets
    for widget in widgets.sidebar:
        if isinstance(widget, praw.models.RulesWidget):
            rules_widget = widget
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    print("timestamp:", timestamp)
    return {"sub": subr_name, "date": timestamp, "rules": rules_widget.data, "subscribers": subreddit.subscribers,
                      "created_utc": subreddit.created_utc, "lang": subreddit.lang}

def scrape_metadata(subr_list_csv :str) -> None:
    failed_subr_list = []
    with open(sys.argv[2], "w") as output:
        with open(subr_list_csv) as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                try:
                    metadata_jsonl = get_subr_data(row[0].strip())
                    json.dump(metadata_jsonl, output)
                    output.write("\n")
                except:
                    failed_subr_list.append(row[0].strip()) # puts the subreddit name that didn't return data into a list
            output.write(f"Failed Subreddit List: {failed_subr_list}")


if __name__ == "__main__":
    scrape_metadata(sys.argv[1])