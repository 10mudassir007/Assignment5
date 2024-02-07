user_genre = input('Enter genre: ')
user_rating = float(input('Enter rating: '))
user_year = int(input('Enter year: '))

movie1_genre = 'Action'
movie1_rating = 8.7
movie1_year = 2010

movie2_genre = 'Thriller'
movie2_rating = 8.3
movie2_year = 2020

movie3_genre = 'Sci-Fi'
movie3_rating = 8.0
movie3_year = 2023

if user_genre == movie1_genre and user_rating == movie1_rating and user_year == movie1_year:
    print('Movie 1')
elif user_genre == movie2_genre and user_rating == movie2_rating and user_year == movie2_year:
    print('Movie 2')
elif user_genre == movie3_genre and user_rating == movie3_rating and user_year == movie3_year:
    print('Movie 3')

else:
    print('No movie available')

