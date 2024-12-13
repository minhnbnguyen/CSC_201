'''
Name(s): Minh Nguyen
CSC 201
Lab 9

This program provides a menu of options analyzing the complaints from the
Consumer Financial Protection Bureau's Consumer Complaint Database. The user
chooses from a menu to:
    1) Look up the number of complaints for a particular company
    2) Look up the number of complaints in a particular state
    3) Look up the number of complaints in a particular month
    4) Display the top N companies based on the number of complaints
    5) Display the top N states based on the number of complaints

'''
import csv

DATA_FILE_NAME = 'consumer_complaints_2018_small_sample.csv'
#DATA_FILE_NAME = 'consumer_complaints_2018.csv'

MAX_MENU_CHOICE = 6

VALID_STATES = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
                'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
                'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
                'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
                'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

VALID_MONTHS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

def makeComplaintList():
    '''
    Makes a list of complaints using data from the Consumer Financial Protection
    Bureau's Consumer Complaint Database. Each complaint is a dictionary mapping
    from a complaint part to this complaint's value for that part.
    
   
    Returns:
        list: list of complaints where each complaint is a dictionary
    '''
    # DON'T MODIFY THIS FUNCTION!
    complaints = []
    with open(DATA_FILE_NAME, mode='r', encoding='cp1252') as csv_file:
#    with open(DATA_FILE_NAME, mode='r', encoding='ISO-8859-1') as csv_file:  # if you have a Mac computer and you get an encoding error message, use this one instead

        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            dictVersion = dict(row)
            complaints.append(dictVersion)
            
    return complaints

def lookUpCompany(complaintList):
    '''
    Prompts user to enter a company name and prints the number of complaints for that company
    
    Params:
        complaintList (list): list of complaints where each complaint is a dictionary
    '''
    # TODO: ADD YOUR CODE HERE
    companyName = input('Enter a company name: ')
    
    complaintCount = 0
    for complaintDict in complaintList:
        if complaintDict['Company'] == companyName:
            complaintCount = complaintCount + 1
    
    if complaintCount == 0:
        print(f'{companyName} not in list.')
    else:
        print(f'{complaintCount} complaints')
    
def lookUpState(complaintList):
    '''
    Prompts user to enter a state abbreviation and prints the number of complaints for that state
    
    Params:
        complaintList (list): list of complaints where each complaint is a dictionary
    '''
    # TODO: ADD YOUR CODE HERE
    state = input('Enter state abbreviation: ')
    while state not in VALID_STATES:
        print('Invalid. Try again.')
        state = input('Enter state abbreviation: ')

    complaintCount = 0
    for complaintDict in complaintList:
        if complaintDict['State'] == state:
            complaintCount = complaintCount + 1
    
    if complaintCount == 0:
        print(f'{state} had no complaints.')
    else:
        print(f'{complaintCount} complaints')
    

def lookUpMonth(complaintList):
    '''
    Prompts user to enter a month number and prints the number of complaints for received in that month.
    
    Params:
        complaintList (list): list of complaints where each complaint is a dictionary
    '''
    # TODO: ADD YOUR CODE HERE
    month = input('Enter a month number (1-12): ')
    while month not in VALID_MONTHS:
        print('Invalid. Try again.')
        month = input('Enter a month number (1-12): ')

    complaintCount = 0
    for complaintDict in complaintList:
        date = complaintDict['Date received']
        monthIndex = date.split('/')[0]
        if month == monthIndex:
            complaintCount = complaintCount + 1
    
    if complaintCount == 0:
        print(f'No complaints for month {month}.')
    else:
        print(f'{complaintCount} complaints')
    
            
def printTopN(countsDict, numValues):
    '''
    Prints the top N values in a dictionary with their corresponding keys
    in reverse order from largest to smallest.
    
    Params:
        countsDict (dict): a dictionary with values that are "sortable"
        numValues (int): the number of items to be displayed in the table
    '''
    # DON'T MODIFY THIS FUNCTION!    
    #
    # Note: since list.sort(...) sorts by the 1st item in each tuple first, we
    # make a list of tuples where the count comes first, and the key second.
    savedList = [(count,key) for key,count in countsDict.items()]
    savedList.sort(reverse = True)
    
    for count,key in savedList[:numValues]:
        print(f'{count:7}  {key}')


def printTopCompanies(complaintList):
    '''
    Prompts the user for the number of companies they want displayed in the
    table and prints a table with the companies having the most complaints.
    
    Params:
        complaintList (list): list of complaints where each complaint is a dictionary
    '''  
    # TODO: ADD YOUR CODE HERE
    companyNum = int(input('How many companies do you want to see? '))
    while companyNum < 1:
        print('Invalid. Try again.')
        companyNum = int(input('How many companies do you want to see? '))
    
    companyDict = {}
    
    for complaintDict in complaintList:
        companyName = complaintDict['Company']
        
        if companyName in companyDict:
            companyDict[companyName] += 1
        else:
            companyDict[companyName] = 1
    
    print('Companies with the most complaints:')
    printTopN(companyDict, companyNum)
        

def printTopStates(complaintList):
    '''
    Prompts the user for the number of states they want displayed in the
    table and prints a table with the states having the most complaints.
    
    Params:
        complaintList (list): list of complaints where each complaint is a dictionary
    ''' 
    # TODO: ADD YOUR CODE HERE
    stateNum = int(input('How many states do you want to see? '))
    while stateNum < 1:
        print('Invalid. Try again.')
        stateNum = int(input('How many states do you want to see? '))
    
    stateDict = {}
    
    for complaintDict in complaintList:
        state = complaintDict['State']
        
        if state in stateDict:
            stateDict[state] += 1
        else:
            stateDict[state] = 1
    
    print('States with the most complaints:')
    printTopN(stateDict, stateNum)
    
         
def displayMenu():
    ''' Prints menu of choices '''
    print('Choose from the following options\n')
    print('1  Get number of complaints for one company')
    print('2  Get number of complaints for one state')
    print('3  Get number of complaints for one month')
    print("4  Get companies with most complaints")
    print('5  Get states with most complaints')
    print('6  Quit')
    print()

def getMenuChoice():
    '''
    gets valid menu choice from the user

    Returns:
        str: valid menu choice
    '''
    choice = input('Enter choice: ')
    while not choice.isdigit() or int(choice) < 1 or int(choice) > MAX_MENU_CHOICE:
        print('Invalid. Try again')
        choice = input('Enter choice: ')
    return int(choice)

def main():
    complaintList = makeComplaintList() # Each element is a dictionary
    
    displayMenu()
    menuChoice = getMenuChoice()
    print()
    while menuChoice != MAX_MENU_CHOICE:
        if menuChoice == 1:
            lookUpCompany(complaintList)
        elif menuChoice == 2:
            lookUpState(complaintList)
        elif menuChoice == 3:
            lookUpMonth(complaintList)           
        elif menuChoice == 4:
            printTopCompanies(complaintList)
        else:
            printTopStates(complaintList)

        input("\nPress ENTER to return to the menu.\n")
        displayMenu()
        menuChoice = getMenuChoice()
        print()
    
if __name__ == '__main__':
    main()
        
        