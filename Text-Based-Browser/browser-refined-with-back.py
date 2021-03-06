nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

import argparse
import sys
import os
from collections import deque


def read_urls(user_input):
    news = {'bloomberg.com': bloomberg_com, 'nytimes.com': nytimes_com}
    if user_input == 'bloomberg.com' or user_input == 'nytimes.com':
        file_name = user_input[:user_input.index('.')]
        with open(os.path.join(args, file_name), 'w', encoding='utf-8') as f:
            for lines in news[user_input]:
                f.write(lines)
        with open(os.path.join(args, file_name), encoding='utf-8') as f2:
            print(f2.read())

    elif os.access(os.path.join(args, user_input), os.R_OK):
        with open(os.path.join(args, user_input)) as f2:
            print(f2.read())

    else:
        print('Error: Incorrect URL')


# write your code here
def check_url():
    back_list = deque()
    read_news = False
    while not read_news:
        user_input = input().lstrip('https://www.')

        if user_input == 'exit':
            sys.exit()
        elif user_input == 'nytimes.com' or user_input == 'bloomberg.com' or user_input == 'bloomberg' or user_input == 'nytimes':
            back_list.append(user_input)
            read_urls(user_input)
        elif user_input.count('.') > 1:
            print("The URL is invalid")
        elif user_input == 'back':
            try:
               inp = back_list[-2]
               read_urls(inp)
            except:
                pass
        else:
            print('404 error-This page does not exist')


args = sys.argv[1]
if not os.path.exists(args):
    os.mkdir(str(os.getcwd()).join({args}))

check_url()





