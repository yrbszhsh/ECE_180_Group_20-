import pandas as pd
import matplotlib.pyplot as plt

#total volumes - year

df = pd.read_csv('sandiego_trafficdata.csv')
total_2011 = sum(df['2011'])
total_2012 = sum(df['2012'])
total_2013 = sum(df['2013'])
total_2014 = sum(df['2014'])
total_2015 = sum(df['2015'])
total = [total_2011,total_2012,total_2013,total_2014,total_2015]
year = [2011,2012,2013,2014,2015]

#plot

plt.xlabel('Year')
plt.ylabel('Total Volume')
plt.bar(year,total,facecolor='blue',width=0.5)
plt.legend()
plt.show()

#top 5 different streets with high volume

name = []
for i in range(len(df)):
    name.append(df['Primary Street'][i]+'\n('+df['1st Cross Street'][i]+' - '+df['2nd Cross Street'][i]+')')

highest_2011 = df.sort_values(by='2011')
highest_2012 = df.sort_values(by='2012')
highest_2013 = df.sort_values(by='2013')
highest_2014 = df.sort_values(by='2014')
highest_2015 = df.sort_values(by='2015')

top_2011 = [0,0,0,0,0]
top_2012 = [0,0,0,0,0]
top_2013 = [0,0,0,0,0]
top_2014 = [0,0,0,0,0]
top_2015 = [0,0,0,0,0]

name_2011 = [0,0,0,0,0]
name_2012 = [0,0,0,0,0]
name_2013 = [0,0,0,0,0]
name_2014 = [0,0,0,0,0]
name_2015 = [0,0,0,0,0]


for i in range(5):
    top_2011[i] = df['2011'][highest_2011.index[-(i+1)]]
    name_2011[i] = name[highest_2011.index[-(i+1)]]
    top_2012[i] = df['2012'][highest_2012.index[-(i+1)]]
    name_2012[i] = name[highest_2012.index[-(i+1)]]
    top_2013[i] = df['2013'][highest_2013.index[-(i+1)]]
    name_2013[i] = name[highest_2013.index[-(i+1)]]
    top_2014[i] = df['2014'][highest_2014.index[-(i+1)]]
    name_2014[i] = name[highest_2014.index[-i]]
    top_2015[i] = df['2015'][highest_2015.index[-(i+1)]]
    name_2015[i] = name[highest_2015.index[-(i+1)]]


top = [top_2011, top_2012, top_2013, top_2014, top_2015]
namel = [name_2011, name_2012, name_2013, name_2014, name_2015]

for i in range(5):
    plt.title('201%d' %(i+1))
    plt.xlabel('Street')
    plt.ylabel('Volume')
    plt.xticks(rotation = 60)
    plt.bar(namel[i],top[i],facecolor='blue',width=0.5)
    plt.legend()
    plt.show()
    
# statistics for the streets appear as top5 in different years
    
top5 = list(set(name_2011+name_2012+name_2013+name_2014+name_2015))

for i in range(5):
    for j in top5:
        if j in namel[i]:
            print j
    print '-------NEXT-------'
    




    
    
    
    
    
    