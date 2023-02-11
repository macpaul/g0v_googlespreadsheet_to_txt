# g0v_projectlist_to_videolist
g0v hackathon project list to youtube video subjects

Goal
 - Automatic convert project (presentation) list from google spreadsheet to a list of youtube video subjects.
 - Currently the initial python version is attached. We need Firefox and Chrome plug-in in the future.

Usage
 - Python
  - Download project list as a Google spreadsheat file and save it as an excel.
  - Run this command to generate the video lists:  python g0v_projectlist_to_videolist.py "https://docs.google.com/spreadsheets/d/[Google Spreadsheet ID]" 54 "兔兔黑客松"
  - The 1st paramater is the excel file name, the 2nd parameter is number of the order, the 3rd paramter is the name of the hackathon.
