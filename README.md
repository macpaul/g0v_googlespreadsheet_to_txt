# g0v_googlespreadsheet_to_txt
g0v hackathon project list to youtube video subjects

Goal
 - Automatic convert project (presentation) list from google spreadsheet to a list of youtube video subjects.
 - Currently the initial python version is attached. We need Firefox and Chrome plug-in in the future.

Usage
 - Python
  - Download project list as a Google spreadsheat file and save it as an excel.
  - Run this command to generate the video lists:  python g0v_hackmd_to_videolist.py "hackath54n 第伍拾肆次兔兔黑客松暨零時小學校專案孵化競賽決選日 專案列表 .xlsx" 54 "兔兔黑客松"
  - The 1st paramater is the excel file name, the 2nd parameter is number of the order, the 3rd paramter is the name of the hackathon.
