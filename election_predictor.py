# election predictor model and results

import sys
#states = ['MI', 'NH', 'PA', 'WI', 'FL', 'MN', 'NV', 'ME', 'AZ', 'NC', 'CO', 'CA', 'TX', 'SC']  <--- add back in when we have data
states = ['MI', 'NH', 'PA', 'MN', 'NV', 'ME', 'AZ', 'NC', 'CO', 'CA', 'TX', 'SC']

# polling data takes the form "trump percentage", "biden percentage" (doesn't add up to 100 because of the "other" category)

# this data comes from the latest poll for each state at https://www.270towin.com/2020-polls-biden-trump/

pd = {}
pd['MI'] = [.42, .47]
pd['NH'] = [.46, .44]
pd['PA'] = [.47, .45]
pd['WI'] = [.46, .47]

pd['FL'] = [.44, .47]
pd['MN'] = [.38, .50]
pd['NV'] = [.39, .47]

pd['ME'] = [.42, .52]
pd['AZ'] = [.43, .52]
pd['NC'] = [.48, .45]
pd['CO'] = [.45, .55]

pd['CA'] = [.29, .67]
pd['TX'] = [.45, .49]
pd['SC'] = [.40, .52]

# percent users

users = {}
users['MI'] = .221
users['NH'] = .214
users['PA'] = .227
users['WI'] = .215

users['FL'] = .233
users['MN'] = .232
users['NV'] = .241

users['ME'] = .24
users['AZ'] = .236
users['NC'] = .212
users['CO'] = .226

# replace these with real approximations
users['TX'] = .22
users['CA'] = .22
users['SC'] = .22

# main algorithm 

if __name__ == '__main__': 

    # sentiment analysis data 

    sa_data = {}
    for state in states: 
        sa_data[state] = {}

    f = open('sentiment_data.txt', 'r')
    for line in f: 
        words = line.split(' ')
        state = words[0]
        candidate = words[1][0]
        if candidate not in sa_data[state]:
            ratings = words[2].strip().split(",")
            sa_data[state][candidate] = int(ratings[0][1:])  # collecting only positive ratings
        else: 
            ratings = words[2].strip().split(",")
            sa_data[state][candidate] += int(ratings[0][1:])

    # print(sa_data)

    trump_total = 0
    biden_total = 0

    for state in states:           
        trump_current = users[state]*sa_data[state]['t'] + pd[state][0]*(1 - users[state])
        biden_current = users[state]*sa_data[state]['b'] + pd[state][1]*(1 - users[state])
        trump_total += trump_current
        biden_total += biden_current

    final_t = trump_total / len(states)
    final_b = biden_total / len(states)

    if final_t > final_b:
        print("Trump predicted to win!")
    else: 
        print("Biden predicted to win!")

    print(f"final trump percentage: {trump_total / len(states)}")
    print(f"final biden percentage: {biden_total / len(states)}")


