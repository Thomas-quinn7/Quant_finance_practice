import pandas as pd

unames=['user_id','Gender','Age','Occupation','zip']
users = pd.read_table("C:/Users/tq343/PycharmProjects/"
                      "Quant_finance_practice/data analysis/ml-1m/users.dat",
                      sep='::',engine='python',header=None,names=unames,encoding='ISO-8859-1')

rnames=['user_id','movie_id','rating','timestamp']
ratings = pd.read_table("C:/Users/tq343/PycharmProjects/"
                      "Quant_finance_practice/data analysis/ml-1m/ratings.dat",
                      sep='::',engine='python',header=None,names=rnames,encoding='ISO-8859-1')

mnames=['movie_id','Title','Genre']
movies = pd.read_table("C:/Users/tq343/PycharmProjects/"
                      "Quant_finance_practice/data analysis/ml-1m/movies.dat",
                      sep='::',engine='python',header=None,names=mnames,encoding='ISO-8859-1')

data = pd.merge(pd.merge(ratings, users), movies)

mean_rating = data.pivot_table('rating',
                               index='Title',columns='Gender',aggfunc='mean')

print(mean_rating[:5])

rating_by_title = data.groupby('Title').size()
print(rating_by_title[:5])

active_titles = rating_by_title.index[rating_by_title >= 250]
print(active_titles)

mean_rating = mean_rating.loc[active_titles]
female_top_titles = mean_rating.sort_values(by='F',ascending=False)
print(female_top_titles[:5])
mean_rating['diff']=mean_rating['M']-mean_rating['F']
sorted_diff=mean_rating.sort_values(by='diff',ascending=True)
print(sorted_diff[:5])
