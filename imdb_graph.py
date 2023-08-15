import imdb as n
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
 
ia = n.IMDb()
 
series_name = input("Enter the name of a series: ")
series_ = ia.search_movie(series_name)
series = series_[0]
 
# adding new info set
ia.update(series, 'episodes')
 
# getting episodes of the series
episodes = series.data['episodes']
 
# printing the object i.e name
print(series)
 
print("=========")

##    max_sea = 0
##    max_ep = 0


avg_till = 0
last_ep = 1
total_ep = []
num = 0
plt.style.use("dark_background")

for sea_num in range(1, len(episodes) + 1):

    #getting next season
    episode_ratings = []
    try:
        season = episodes[sea_num]
        print(f"Season {sea_num}")
        
    except:
        print("oops")
        break

    #episode ratings of each season
    for n in range(1, len(season) + 1):
        try:
            print(f'Episode {n} \"{season[n].data["title"]}\": {round(season[n].data["rating"], 1)}')
            episode_ratings.append(round(season[n].data["rating"], 1))

        except KeyError:
            print(f"Episode {n}: Unrated.")
            
    coef = np.polyfit(list(range(last_ep, len(episode_ratings) + last_ep)), episode_ratings, 1)
    poly1d_fn = np.poly1d(coef) 
    
    #Plotting the graph for entire show
    plt.plot(list(range(last_ep, len(episode_ratings) + last_ep)), episode_ratings, 'o-', markersize = 4, linewidth = 1.2)

    plt.plot(list(range(last_ep, len(episode_ratings) + last_ep)), poly1d_fn(list(range(last_ep, len(episode_ratings) + last_ep))),
              markersize = 4, linewidth = 2, label = f"Season {sea_num}"
             )
    
    print()
    print("Average season rating:", round(sum(episode_ratings)/len(episode_ratings), 2))
    print()

    last_ep += len(episode_ratings)
    total_ep.extend(episode_ratings)
    num += 1
    
print("Average rating:", round(sum(total_ep)/len(total_ep), 2))
##    print("Average episode rating till episode watched:", avg_till)


print("*"*20, "\n\n")
season_len.append(len(total_ep))

plt.xlabel("Episode number")
plt.ylabel("Episode ratings")


##plt.grid(axis = 'y')
##plt.yticks(np.arange(0, 10, 1))
plt.xticks(np.arange(0, max(season_len), 5))
plt.yticks(np.arange(min(total_ep), 10.1, .2))
plt.title(f"IMDb rating of {series}")
plt.show()
