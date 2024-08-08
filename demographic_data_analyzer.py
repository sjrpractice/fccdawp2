import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    csv_url = "https://github.com/freeCodeCamp/boilerplate-demographic-data-analyzer/raw/1fed7bb013559779ec8e23a0809644b1581df072/adult.data.csv"
    df = pd.read_csv(csv_url)
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = format(df['race'].value_counts(),".2f")

    # What is the average age of men?
    average_age_men = format(df[df['sex']=="Male"]['age'].mean(),".2f")

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = format(((len(df[df['education']=="Bachelors"])*100))/(len(df)),".2f")

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education_rich = format(len(df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate') & (df['salary']==">50K")]) / len(df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')])*100,".2f")

    # What percentage of people without advanced education make more than 50K?
    higher_education_rich = format(len(df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate') & (df['salary']==">50K")]) / len(df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')])*100,".2f")

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = format(len(df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]) / len(df)*100,".2f")
    lower_education = format(len(df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]) / len(df)*100,".2f")

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = format(df['hours-per-week'].min(),".2f") 

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = format(len(df[(df['hours-per-week'] == 1) & df['salary']==">50K"])  /  len(df[(df['hours-per-week'] == 1)])*100,".2f")

    rich_percentage = format(((len(df[df['salary']==">50K"])*100))/(len(df)),".2f")

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = df[df['salary'] == ">50K"]['native-country'].value_counts(normalize=True).idxmax()
    highest_earning_country_percentage = format(df[df['salary'] == ">50K"]['native-country'].value_counts(normalize=True).max() * 100,".2f")

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['salary'] == ">50K") & (df['native-country'] == 'India')]['occupation'].value_counts(normalize=True).idxmax()

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