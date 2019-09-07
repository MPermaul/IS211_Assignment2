# IS211_Assignment2
Week 2 Assignment 2

Author: Moses Permaul
Personal Email: moses.permaul@hotmail.com
CUNY SPS Email: moses.permaul13@spsmail.cuny.edu

Application Details:

1) This application is designed to run via command line and will try to read a csv file via a url.

2) The script requires a url argument when running. Entering no argument will exit the script.
    
	ex: 
		Good:	python assignment2.py https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv)
		
		Bad:	python assignment2.py
		
			Message displayed:
				usage: assignment2.py [-h] url
				assignment2.py: error: the following arguments are required: url

3) The application will try to open the url, read the csv data, process the data, and then allow 
a user to lookup the names and birthdays of the people stored in the data by their ID numbers.

4) The log fie "errors.log" will be created to store the details of persons who can't be processed by
the application due to incorrect birthday formats in the csv file data.

5) A message will be displayed in the console if there are issues with the url.
	
	ex: 
		The url is invalid --> passed in https://s3.amazonaws.co
		b) Message displayed --> "We are unable to reach the server. Please check your url!"

6) A message will be displayed in the console if the url is valid and there is nothing to process.

7) A message will be displayed in the console if the url is valid, but the csv data can't be process.

8) Once the data has been processed, a prompt will be displayed asking for an ID. Either the name of the 
person and their birthday or a message saying the the ID entered is invalid will be displayed.

9) The application will keep running until the end user exits it.

10) To Exit the application, enter the number 0 (zero) or any negative number as the ID.

