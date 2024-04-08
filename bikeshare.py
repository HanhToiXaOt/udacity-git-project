import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_flg = False
    while city_flg != True:
        city = str(input("Enter city name in ({})".format(",".join(CITY_DATA.keys())))).lower()
        if (city not in CITY_DATA.keys()) :
            print("That \'s not a valid city name")
        else:
            city_flg = True
            
    # Get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    month_flg = False
    while month_flg != True:    
        month = str(input("Enter month is empty string or  \'all\' or in ({})".format(",".join(months)))).lower()
        if month not in months and month != "" and month != 'all':
            print("That \'s not a valid month")
        else:
            month_flg = True
            
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day_flg = False
    while day_flg != True:    
        day = str(input("Enter day is empty string or  \'all\' or in ({})".format(",".join(days)))).lower()
        if day not in days and day != '' and day != 'all':
            print("That \'s not a valid day")
        else:
            day_flg = True


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    if month != 'all' and month != "":
       months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
       month = months.index(month) + 1
       df = df.query('month == "' + str(month) + '"')
    
    if day != 'all' and day != '':
       df = df.query('day == "' + day.title() + '"')
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month: {}\n'.format(common_month))
    
    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print('The most common day: {}\n'.format(common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour: {}\n'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station: {}\n'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station: {}\n'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Station'] = df['Start Station'].str.cat(df['Start Station'], sep=", ")
    common_start_end_station = df['Start End Station'].mode()[0]
    print('Most frequent combination of start station and end station trip: {}\n'.format(common_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = (df['Trip Duration'].dropna().sum())/60
    print('Total travel time: {} hour \n'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = (df['Trip Duration'].mean())/60
    print('Mean travel time: {} hour \n'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].dropna().nunique()
    print('Counts of user types: {}\n'.format(user_type_count))

    if city != 'washington':
        # TO DO: Display counts of gender
        gender_count = df['Gender'].dropna().nunique()
        print('Counts of gender: {}\n'.format(gender_count))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].dropna().min()
        print('The earliest year of birth: {}\n'.format(int(earliest_birth_year)))

        most_recent_birth_year = df['Birth Year'].dropna().max()
        print('The most recent year of birth: {}\n'.format(int(most_recent_birth_year)))

        most_common_birth_year = df['Birth Year'].dropna().mode()[0]
        print('The most common year of birth: {}\n'.format(int(most_common_birth_year)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    print('\nGet raw data...\n')
    start_time = time.time()
    stop_flg = False
    see_cnt = 0
    while stop_flg != True:
        if see_cnt == 0:
            see_raw_answer = str(input('\nWould you like see first 5 raw data ? Enter yes or no.\n')).lower()
        else:
            see_raw_answer = str(input('\nWould you like see more raw data ? Enter yes or no.\n')).lower()
        if see_raw_answer == 'yes':
            if (see_cnt + 1)*5 + 1 < len(df):
                    if see_cnt == 0:
                        print('First 5 row data :\n {}'.format(df.head()))
                    else:
                        print('More 5 row data :\n {}'.format(df[(see_cnt)*5:(see_cnt + 1)*5]))
                    see_cnt += 1
                    print("\nThis took %s seconds." % (time.time() - start_time))
                    print('-'*40)
            else :
                print('Last row data :\n {}'.format(df[(see_cnt)*5:(see_cnt + 1)*5]))
                print("\nThis took %s seconds." % (time.time() - start_time))
                print('-'*40)
                stop_flg = True
        else:
            stop_flg = True
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
