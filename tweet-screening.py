tweet = input('Write your tweet\n')
banned = 'government','president','buhari','sars'

if len(tweet) >= 60:
    print('''
    ERROR: We couldn\'t publish your tweet.
    Tweet lenght is more than 60 characters!
    ''')
else:
    checks = []
    for word in banned:
        if word in tweet.lower():
            checks.append('Yes')
        else:
            checks.append('No')
        
    if 'Yes' in checks:
        print('''
            ERROR: We couldn\'t publish your tweet.
            Tweet contains one or more banned words!
            ''')
    else:
        print(f'''
        TWEET PUBLISHED!
        {tweet}
        ''')
