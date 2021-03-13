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
import requests

def read_urls(user_input):
    # news = {'bloomberg.com': bloomberg_com, 'nytimes.com': nytimes_com}

    header_dict = {
    # 'authority': 'www.bloomberg.com',
    # 'method': 'GET',
    # 'path': '/ europe',
    # 'scheme' : 'https',
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    # 'cache - control' : 'max - age = 0',
    # 'cookie': 'bb_geo_info={"country":"FR","region":"Europe","fieldD":"wanadoo.fr"}|1609367654521; _reg-csrf=s%3AHhJ9_7vIvON_nYk5ARc4YOXc.5xuPcXsPE1JOQ1SdtAzpKuhPyCksdh2La9zZo2yBCb8; agent_id=26f8be41-e373-48ef-8ae5-7c49a6d686e8; session_id=db7e691c-4d37-4373-b28b-3d0f25a95f65; session_key=874468897f6c165c0e57cb051c5b5722807d3750; _user-status=anonymous; _sp_v1_uid=1:203:75510f04-f4b2-4b1c-bc59-a0980715d72e; _sp_v1_csv=null; _sp_v1_lt=1:; _pxvid=f8ff9453-456e-11eb-a787-0242ac12000e; _ga=GA1.2.1029005812.1608762863; ccpaUUID=7d048a3f-c8e1-4091-8d99-28ebe22e8634; dnsDisplayed=true; ccpaApplies=true; signedLspa=false; _pxhd=748062ccd91e77df5dbef455a086d7a6b275494042e0ac85f707b593441b181c:f8ff9453-456e-11eb-a787-0242ac12000e; consentUUID=05fa7ddf-ba99-40a5-a670-86077f3df623; _sp_krux=true; euconsent-v2=CO_JeMvO_JeMvAGABCENBGCgAP_AAGPAAAqIGYIB5CpGCSFBKGh4AIsAEAQXwBAEAOAAAAABAAAAAAgQAIwCAEASAACAAAACAAAAIAIAAAAAEAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIEAAAAAAEAAABAAgAAAAAIAQAQLzgGgAhAB-AF8ARwBA4CDgIQAREAiwBdQDAgGvAOoAvMAwZAFABUAEwARwBHAF5iIAIAKgkBMABYAFQAMgAcABAACoAFoANIAiACKAEwAJ4AhABHAClAHeAPYAjgBKQGSBoAIAKhUAYAFQATABHAEcAU2AvMdAYAAWABUADIAHAAQAAqABaADSAIgAigBMACeAGIAQgAjgBMACjAFKAMoAd4A9gCOAEpAOoAyQcABAAuQgFgALAAyACoAJgAYgBHADKAHeARwAlIB1CUA4ABYAGQAOABEACYAGIAQgAjgBRgClAGUAO8AjgB1CQAEAC5SAoAAsACoAGQAOAAgABUAC0AGkARABFACYAE8AMQAhABRgClAGUAO8AjgBKQGSFAAIAFw.YAAAAAAAAAAA; _sp_v1_opt=1:login|true:last_id|11:; bbgconsentstring=req1fun1pad1; bdfpc=004.2142460795.1609183338903; _gcl_au=1.1.1351019313.1609183339; __gads=ID=bd4a22bc9aa1bc52:T=1609183314:S=ALNI_MZhq02GnkE4P6K2ZXxbmHt-piuruA; _gid=GA1.2.1192988317.1609183340; _scid=fd61e0e3-f7b4-4549-82dc-3c0a299f989b; __tbc=%7Bjzx%7Dt_3qvTkEkvt3AGEeiiNNgLVrlu-HHY_pokGp9QsaCWW7AVC5a0Uwh3iNJlFC7xlVEpBFbN2KJOdIJZjs_kHZGdFAUltppJgCX70uIsEeZtZO-D2WhINIcUXa8S8Lf4rNjylU0Z664w9lha1BgkmqDg; __pat=-18000000; _rdt_uuid=1609183340645.182c4f76-d9ab-433f-996e-0378327944fe; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.bloomberg.com/europe%22%2C%22sref%22:%22https://www.bloomberg.com/europe%22%2C%22sts%22:1609183340688%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=baf6011f2162831fabe7acf0d519b5c5%22%2C%22session_count%22:1%2C%22last_session_ts%22:1609183340688}; _li_dcdm_c=.bloomberg.com; _lc2_fpi=b1166d620485--01etnctaa9y7bj5g7nmp07y0cv; _fbp=fb.1.1609183341040.76110543; _cc_id=d9e90d8a0c764ce9defc874c5382f744; bbAbVisits=; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbKKxs_IAzEMamN1YpRSQcy80pwcILsErKC6lpoSSjqYjoKqGfIGxQIAFvgIHXEBAAA%3D; _sp_v1_consent=1!1:1:1:0:0:0; _sp_v1_data=2:265834:1608762845:0:14:0:14:0:0:_:-1; _uetsid=016b2eb0494211ebbdc791e400e55e35; _uetvid=016b8ed0494211eb8c54b943273597f1; __sppvid=95f1b7e4-a010-4ee9-8905-cf4380dddb60; __pvi=%7B%22id%22%3A%22v-2020-12-28-20-22-19-915-EV1jt0awudfizeqb-4dd4ed83ccd36866152464143bf11f79%22%2C%22domain%22%3A%22.bloomberg.com%22%2C%22time%22%3A1609184725837%7D; xbc=%7Bjzx%7DIq1IlO7CRHEP_X40S8GmOo0tqchf5QFCuiLN8SHBeEhL86BeMppHlmOOtrfUbSNP-eqwfilg18KQB0T_KZPMMfATRurNOFM-jICZPlPOdrknJ5If7F0Dp-JMmPC0csrAjDtVFpLDlCCuRMZfv4rc5H4AFcsOUng_eVDjufK3aGng2gSxn2DVBPISHTUx1UBQ8eKDxQC4Z2EIR_nycg3Xgn-XVwiGPrFhjtZ2mKw7ZZgyxQ9i7m-6KDh1TCw1Rd_OR4k97FuczBBQtDGrqy_2JWbbor8U1NusRqyh3FyD4DY; _px2=eyJ1IjoiODRlYjI5YTAtNDk0NC0xMWViLWI4NjktYTExNDg2OTBkMTM1IiwidiI6ImY4ZmY5NDUzLTQ1NmUtMTFlYi1hNzg3LTAyNDJhYzEyMDAwZSIsInQiOjE2MDkxODUxNzg2NDYsImgiOiIxMTMyY2MwNDVmMTVjZDZkY2Q3MTY2ZTNjZThjYjViZTYwMGYwM2ExNWZiZGU1MTE0ZjE4YWQ2OWIzYjM2ZTA4In0=; _px3=7a65067c3542fd7b85c9fa782325209a6028489bf627acbae0946aa103f469be:1yf1hTxiR6cKvWprX5oRO2s2DBrxekcSICDqy5nhdkvwsOmQG3vd2O6d8NWlofURBj4+7KXcOSWt3+aaoViWKA==:1000:WcZuTtxrSTGIiAP/xZ5aZhKYz0pixmQx+QrNN2ZhZDgY+ZJ8Ew6tPBu3zV1UVU2bmGeVOjAe8jcfe+GFDTPYiLEwG+qwjNvToQJ6YZFtt6xFWiyiCis0TU3XygzHNCNL9TJy7rkgYK91Xv/Ine46CiFiwLTFyfPSnktJss5KvDY=; _pxde=74e50f8f4ff74bb5a2e73c00bc41b16f56a06eece708fd82ca1f219e86d1dbf1:eyJ0aW1lc3RhbXAiOjE2MDkxODQ4Nzg2NDYsImZfa2IiOjAsImlwY19pZCI6W119; _reg-csrf-token=Ok50U3HH-98_jNsGdRty_pPHW3vsUGGESpp8',
    # 'if-none-match': 'W/"87de7-MJJQNacBG6CGNHTcNN536FPOvoA"',
    # 'sec-fetch-dest': 'document',
    # 'sec-fetch-mode': 'navigate',
    # 'sec-fetch-site': 'none',
    # 'sec - fetch - user' : '?1',
    # 'upgrade - insecure - requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    r = requests.get(user_input, headers=header_dict)
    # print(r.url)
    # print(r.status_code)
    if r.ok:
        file_name = user_input.lstrip('https://www.')[:user_input.index('.')]
        with open(os.path.join(args, file_name), 'w', encoding='utf-8') as f:
            for lines in r.text:
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
        user_input = input()
        if user_input == 'exit':
            sys.exit()
        elif user_input.count('.') > 2:
            print("The URL is invalid")
        elif user_input == 'back':
            try:
                inp = back_list[-2]
                read_urls(inp)
            except:
                pass
        elif user_input:
            website = 'https://' + user_input
            if requests.get(website).ok:
                read_urls(website)
            else:
                website = 'https://'+'www.' + user_input
                read_urls(website)
            back_list.append(website)
        else:
            print('404 error-This page does not exist')


        # elif user_input == 'nytimes.com' or user_input == 'bloomberg.com' or user_input == 'bloomberg' or user_input == 'nytimes' :
        #     back_list.append(user_input)
        #     read_urls(user_input)


args = sys.argv[1]
if not os.path.exists(args):
    os.mkdir(str(os.getcwd()).join({args}))

check_url()