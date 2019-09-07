import argparse
import logging
import urllib.request
import urllib.error
from datetime import datetime

def downloadData(url):
    """Function that connects to a Url and returns the data to the caller
    :param url: string representing a Url containing data
    :return html: binary data read line by line from the Url
    """
    # open Url and read the response into html variable to return to caller
    with urllib.request.urlopen(url) as response:
        html = response.readlines()
    return html


def processData(html):
    """Function that processes the data passed in by arg html and returns a dictionary with valid data
    :param html: response passed in from the Url containing csv file
    :return csvDict: dictionary with person's processed csv data
    """
    # dictionary that will be used to store each person's details
    csvDict = {}

    # counter variable to store the line number being processed
    counter = 0

    # loop through each item stored in html arg
    for line in html:
        # data is binary, so decode it, strip it of spaces, and then split by comma value
        decoded_line = line.decode('ascii').strip().split(',')

        # set key and value variables to corresponding index values
        key = decoded_line[0]
        value1 = decoded_line[1]
        value2 = decoded_line[2]

        # increment counter by 1 to account for current line being processed
        counter += 1

        # try to set the birthday as a datetime object
        try:
            new_value2 = datetime.strptime(value2, '%d/%m/%Y').date()
        except ValueError:
            # write to log file if unable to convert string to datetime object
            logger.error('Error processing line #{} for ID #{}'.format(counter, key))
        else:
            # add key as type int and values to dictionary if successful
            csvDict[int(key)] = (value1, new_value2)
    return csvDict


def displayPerson(id, personData):
    """Function that prints Person's name and birthday using id provided by user
    :param id: Int value representing ID of person to look up
    :param personData: Dictionary that will be used for the lookup
    """
    # dictionary keys are stored as strings, so convert id first then check if a key matches
    if id not in personData.keys():
        print('\nNot user found with that id\n')
    else:
        print('\nPerson #{} is {} with a birthday of {} \n'.format(id, personData[id][0], personData[id][1]))


def main():
    """Function that drives the order of the application. """

    # initialize a parser, add param url, and parse param as an argument
    parser = argparse.ArgumentParser(description='Data Url CSV Processor')
    parser.add_argument('url', type=str, help='Url where CSV file is stored')
    args = parser.parse_args()

    # call download data function and pass in the url arg, print message to screen if there is an issue and exit
    try:
        csvData = downloadData(args.url)
    except urllib.error.HTTPError as e:
        print('The server couldn\'t fulfill the request. Please check your url!\n')
        print('Error code: ', e.code)
    except urllib.error.URLError as e:
        print('We are unable to reach the server. Please check your url!\n')
        print('Reason: ', e.reason)
    except ValueError:
        print('This is url seems to be missing the HTTP protocol. Please verify that it\'s correct.')
    else:
        # try to pass the data to processData function, print message to screen and exit if issue
        try:
            personData = processData(csvData)
        except:
            print('The application is unable to finish because the data from the url can\'t be processed.\n'
                  'Please check that the url contains a csv file with the proper setup.')
            exit()
        else:
            # variable to represent whether or not to keep application running
            running = True

            # loop to keep the application running until user wants to exit
            while running:
                print('** Entering a number equal to or less than 0 will exit the program. **')

                # loop to make sure that a valid choice is entered
                while True:
                    try:
                        choice = int(input('Please enter the ID for the person you want to look up: '))
                    except ValueError:
                        print('\nYour choice is not valid!\n')
                    else:
                        break

                # check to see if display function should be called or if application should exit
                if choice > 0:
                    # call display function and pass in user's choice and processed dictionary
                    displayPerson(choice, personData)
                else:
                    # update running to exit the application
                    running = False


if __name__ == '__main__':

    # create logger assignment2 and set level to ERROR
    logger = logging.getLogger('assignment2')
    logger.setLevel(logging.ERROR)

    # create formatter
    formatter = logging.Formatter('%(name)s:%(message)s')

    # create file handler with external file error.log
    file_handler = logging.FileHandler('errors.log')
    file_handler.setFormatter(formatter)

    # add the file handler to the logger
    logger.addHandler(file_handler)

    # call main function
    main()
