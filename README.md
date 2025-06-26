# aScXMLreader
Generates a CSV from aSc to iSAMS and ManageBac

Dependencies:
os, pandas, xml.etree.ElementTree

Variable modifications:
1. Change xml_file to your aSc's xml exported file name (Line 7)
2. Change mb_name and isams_name to whichever export name you'd like (Lines 11 and 12)
   Note: same name will override the first export.
3. Change week_array to the name of your school weeks if you have a two week schedule (Line 19)
   Note: don't change asc_weeks, unless you are working with more than two weeks / one week schedule will ignore this definition.
4. OPTIONAL: change day_array if you prefer different day names (Line 23)
5. Change the destination folder variable (dest_folder) to your liking (line 26)

Setup:
1. Install Anaconda (or Miniconda - if you know how to set it up)
   https://www.anaconda.com/download
3. Install Visual Studio Code
   https://code.visualstudio.com/download
5. Download the repository to your computer and unzip it
6. within the unzipped project folder, add your exported xml file from aSc
7. From VS Code > open a new Terminal > navigate to the project folder
8. Type and run the following command: python3 xmlreader.py
   (The program will execute and produce two CSVs: one for iSAMS and the other for ManageBac)
9. Adjust your spreadsheets as per system requirements (e.g. on iSAMS you'll need to convert your periods to match the period ID from iSAMS)
10. Proceed to uploading the timetables
