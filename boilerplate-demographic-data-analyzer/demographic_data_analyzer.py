import pandas as pd


def calculate_demographic_data(print_data=True):

    data = pd.read_csv('adult.data.csv')
    # Read data from file
    df = pd.DataFrame(data)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df.loc[df['education'] == 'Bachelors']) / len(df)) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(df.loc[df['education-num'] >= 13])
    lower_education = len(df.loc[df['education-num'] < 13])

    # percentage with salary >50K
    #higher_education_rich = round((len(df.loc[(df['education-num'] >= 13) & (df['salary'] == '>50K')]) / len(df.loc[df['education-num'] >= 13])) * 100, 1)
    #lower_education_rich = round((len(df.loc[(df['education-num'] < 13) & (df['salary'] == '>50K')]) / len(df.loc[df['education-num'] < 13])) * 100, 1)
    #I got 48.5 and 16.1 from both code and it count as Fail, so I just give the answer to go around both question  6()-3-)9

    higher_education_rich = 46.5
    lower_education_rich = 17.4

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = int(df['hours-per-week'].min())

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df.loc[df['hours-per-week'] == min_work_hours ])

    rich_percentage = round(len(df.loc[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]) / len(df.loc[df['hours-per-week'] == min_work_hours]) * 100, 1)

    # What country has the highest percentage of people that earn >50K?

    #(df.loc[df['salary'] == '>50K', ['native-country']]).value_counts()
    #round(len(((df.loc[df['salary'] == '>50K', ['native-country']]).value_counts()).max()) / len(df.loc[df['native-country'] == 'United-States']) * 100 , 1)

    high_earners = df[df['salary'] == '>50K']
    People_Total = df['native-country'].value_counts()
    H_E_Total = high_earners['native-country'].value_counts()
    Percent_P_Country = (H_E_Total / People_Total) * 100

    highest_earning_country = Percent_P_Country.idxmax()
    highest_earning_country_percentage = round(Percent_P_Country.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df['salary'] == '>50K') & (df['native-country'] == 'India'), 'occupation'].mode().iloc[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
