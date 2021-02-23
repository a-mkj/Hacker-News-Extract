# Hacker-News-Extract

This repository contains code that uses the [HackerNews](https://news.ycombinator.com) API to extract several categories of articles. These are saved in an Excel file, with functions that open tagged files in bulk. 

Functions include:
* extract_story uses the article's identifying number to return relevant metadata.
* extract_recent allows the user to extract metadata on the N most recent articles published on the site.
* extract_all_hn extracts metadata on newest, top and best rated stories on HackerNews and returns dataframes containing this information.
* save_all_hn saves metadata on the newest, best and top rated stories in an Excel spreadsheet. Spreadsheet is formatted in sepia tones and font/size is chosen for optimal readability.
* open_hn_web uses the spreadsheet saved above to open all links for selected articles, from a tab (new, best or top) input provided by the user. Articles are tagged to be opened by entering a 1 in the Status column. This enables users to quickly parse through and tag articles of interest for later consumption.
