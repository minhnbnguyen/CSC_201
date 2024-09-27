"""
Name: Minh Nguyen
CSC 201
Project 1

The program calculates n the number of medals a specific country won in the Olympics and the relative success of the different sports.

Document Assistance:
    https://www.geeksforgeeks.org/check-multiple-conditions-in-if-statement-python/
    I looked up how to add multiple conditions in 1 if statement.
    
    I gave assistance to Chau Tran about the multiple conditions in if statement on this project.

"""
def main():
    # get input from the user
    print('*** Welcome to Olympic Medal Tally System ***')
    print()
    country_name = input('Enter country name: ')
    sport_num = int(input(f'How many sports did *** {country_name} *** participate in? '))
    print ()
    
    #assign variables for later calculations
    country_medal = 0
    medal_sport = 0
    no_medal = 0
    highest_rate = 0
    highest_score = 0
    lowest_score = 100
    highest_rate_sport = ' '
    highest_score_sport = ' '
    lowest_score_sport = ' '
    
    # get detailed input from the user
    for num in range (sport_num):
        sport_name = input(f'Enter name of ** Sport {num + 1} **: ')
        participant = int(input(f'Enter number of participants in ** {sport_name} **: '))
        gold = int(input(f'    Enter number of GOLD medals won in ** {sport_name} **: '))
        silver = int(input(f'    Enter number of SILVER medals won in ** {sport_name} **: '))
        bronze = int(input(f'    Enter number of BRONZE medals won in ** {sport_name} **: '))
    
    # use assignment statements to compute values
        total_medal = gold + silver + bronze
        val = 0.6 * gold + 0.3 * silver + 0.1 * bronze
        weighted_score = round(val, 3)
        country_medal = country_medal + total_medal
        success_rate = round(((total_medal / participant) * 100),3)
        
        if total_medal >= 1:
            medal_sport = medal_sport + 1
        if total_medal == 0:
            no_medal = no_medal + 1
        if highest_rate < success_rate:
            highest_rate = success_rate
            highest_rate_sport = sport_name
        if highest_score < weighted_score:
            highest_score = weighted_score
            highest_score_sport = sport_name
        if (total_medal >= 1) and (lowest_score > weighted_score):
            lowest_score = weighted_score
            lowest_score_sport = sport_name
     
     # use print to give the results
        print()
        print(f'Total number of medals = {total_medal} with a weighted score of {weighted_score}')        
        if success_rate > 50:
            print(f'Exceptional success rate per participant of {success_rate}%!')
        elif success_rate > 25:
            print(f'Great success rate per participant of {success_rate}%!')
        elif success_rate > 0:
            print(f'With a success rate per participant of {success_rate}%, your sport made it on the podium!')
        else:
            print('No medals :( Better luck next time.')
        print()
    
    # use assignment statements to compute the values
    val_2 = country_medal/sport_num
    country_avg = round(val_2, 3)
    
    # use print to give the results
    print('***** OVERALL STATISTICS *****')
    print(f'Number of sports that got a medal: {medal_sport}')
    print(f'Number of sports with no medal: {no_medal}')
    print(f'Total medals = {country_medal} with average of {country_avg} medals per sport')
    print()
    
    if (country_medal >= 1) and (sport_num > 1):
        print('***** AWARD CEREMONY *****')
        print(f'Award for highest success rate per participant goes to {highest_rate_sport}')
        print(f'Award for highest weighted score goes to {highest_score_sport}')
        print(f'Recognition award to {lowest_score_sport} for just making it with a weighted score of {lowest_score}')
        
# call function to main
main()
