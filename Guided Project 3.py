#!/usr/bin/env python
# coding: utf-8

# # Introduction

# This guided project by Dataquest is to analyze post on HackerNews speficically on AskHN and ShowHN posts. For this project, I would like to compare whether AskHN or ShowHN receive more comments on average. Besides that, I would like to know when to post in HackerNews in order to receive more comments on average. 

# # Import Data

# In[1]:


from csv import reader
opened_file = open("/Users/aimannazmi/Desktop/hacker_news.csv")
read_file = reader(opened_file)
hn = list(read_file)
hn_header = hn[0]
hn = hn[1:]

print(hn_header)
print(hn[3])


# # Group Data

# In[2]:


ask_posts = []
show_posts = []
other_posts = []

for row in hn:
    title = row[1]
    if title.lower().startswith("ask hn"):
        ask_posts.append(row)
    elif title.lower().startswith("show hn"):
        show_posts.append(row)
    else:
        other_posts.append(row)


# # Find Average Comments for AskHN Posts and ShowHN Posts

# In[3]:


total_ask_comments = 0

for row in ask_posts:
    num_comments = row[4]
    total_ask_comments += int(num_comments)
avg_ask_comments = total_ask_comments/ len(ask_posts)

total_show_comments = 0

for row in show_posts:
    num_comments = row[4]
    total_show_comments += int(num_comments)
avg_show_comments = total_show_comments/ len(show_posts)

print("Average for ask comments is " + str(avg_ask_comments))
print("Average for show comments is " + str(avg_show_comments))


# On average, we can see that AskHN posts will invite 14 comments while ShowHN posts will invite 10 comments. 

# # Analyse based on time

# In[4]:


import datetime as dt

result_list = []

for post in ask_posts:
    result_list.append(
        [post[6], int(post[4])]
    )

comments_by_hour = {}
counts_by_hour = {}
date_format = "%m/%d/%Y %H:%M"

for each_row in result_list:
    date = each_row[0]
    comment = each_row[1]
    time = dt.datetime.strptime(date, date_format).strftime("%H")
    if time in counts_by_hour:
        comments_by_hour[time] += comment
        counts_by_hour[time] += 1
    else:
        comments_by_hour[time] = comment
        counts_by_hour[time] = 1

comments_by_hour


# In[6]:


avg_by_hour = []

for hr in comments_by_hour:
    avg_by_hour.append([hr, comments_by_hour[hr] / counts_by_hour[hr]])

avg_by_hour


# In[7]:


swap_avg_by_hour = []

for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])
    
print(swap_avg_by_hour)

sorted_swap = sorted(swap_avg_by_hour, reverse=True)

sorted_swap


# In[8]:


print("Top 5 Hours for 'Ask HN' Comments")
for avg, hr in sorted_swap[:5]:
    print(
        "{}: {:.2f} average comments per post".format(
            dt.datetime.strptime(hr, "%H").strftime("%H:%M"),avg
        )
    )


# # Conclusion

# In conclusion, we can see Askpost will invite more comments in comparison to Showpost in HackerNews. Also, it is important to highlight that the best time to post Askpost is arounf 3.00 PM as it will invite 39 comments on average. Also, the time can be combined with 4.00 PM as it can get 16 comments on average for each post. 
