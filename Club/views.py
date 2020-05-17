from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib import auth
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from django.contrib.auth.decorators import login_required
from .models import *
import time

CLUB_NAMES = {

    "codingclubiitg":"Coding Club",
    'robotics.iitg':'Robotics',
    'electronics.iitg':'Electronics',
    'Aeroiitg':'Aeromodelling',
    'litsociitg':'LitSoc',
    'iitgai':'IITG.AI',
    'xpressionsiitg':'Xpressions',
    'cadence.iitg':'Cadence',
}

CLUB_PHOTO = {
    "codingclubiitg":"ico/CodingClub.ico",
    'robotics.iitg':"ico/robotics_club.ico",
    'electronics.iitg':"ico/electronics_club.ico",
    'Aeroiitg':"ico/aeromodelling_club.ico",
    'litsociitg':"ico/litsoc.ico",
    'iitgai':"ico/ai.ico",
    'xpressionsiitg':"ico/xpression.ico",
    'cadence.iitg':"ico/cadence.ico",
}

@login_required(login_url="/accounts")
def club_posts(request,club_name):

    club_photo = CLUB_PHOTO[club_name]
    club_oname  = CLUB_NAMES[club_name]
    posts       = Post.objects.filter(club_name__club_name = club_oname)
    return render(request,'css_post.html', {'posts': posts, 'club_name':club_oname, 'club_rel':club_name, 'club_photo':club_photo})



@login_required(login_url="/accounts")
def post_scraping(request,club_name):

    driver          = webdriver.Firefox(executable_path="/home/jatin/Selenium/geckodriver")#executable_path="/home/sourav18a/Downloads/geckodriver"

    driver.get("http://www.facebook.com")

    elem_email      = driver.find_element_by_id("email")
    elem_email.send_keys("###")
    elem_pass       = driver.find_element_by_id("pass")
    elem_pass.send_keys("###")

    elem_email.send_keys(Keys.RETURN)
    elem_pass.send_keys(Keys.RETURN)

    # wait for sometime for the sssion to know that you have logged in then fetch the club

    element         = WebDriverWait(driver,20).until(
	EC.presence_of_element_located((By.NAME,"q"))
	)

    # fetch the club url

    driver.get("https://www.facebook.com/pg/"+club_name+"/posts/")

    # the class _3ixn obscures see mroe link in facebook

    element         = WebDriverWait(driver,30).until(
	EC.invisibility_of_element_located((By.CLASS_NAME,"_3ixn"))
	)
    elem_see_mores  = driver.find_elements_by_class_name("see_more_link")
    for see_more in elem_see_mores:
        see_more.click()

    elem_full       = driver.find_elements_by_class_name("_5pcr")

    data={}
    for elem in elem_full:
        tmp         = elem.find_element_by_class_name("_5pcq")
        time        = tmp.text
        if "hrs" in time:
            time = time+" ago"
        src         = tmp.get_attribute("href")
        src_elems   = src.split('?')
        left        = src_elems[0]
        left_elems  = left.split('/')
        length      = len(left_elems)
        uid         = left_elems[length-1]
        if uid=="":
            uid = left_elems[length-2]
        # check if post has content (whether its an only image post)
        club_oname  = CLUB_NAMES[club_name]
        post_       = Post.objects.filter(club_name__club_name = club_oname, uid = uid)
        club_       = Club.objects.get(club_name = club_oname)

        # print(post_.content+'\n')
        # print('\n')
        if post_:
            for post in post_:
                if post.updated_on!=time:
                    post.updated_on=time
                    post.save()
            continue
        else:
            try:
                elem.find_element_by_class_name("_5pbx")
                content=elem.find_element_by_class_name("_5pbx")
                tmp2 = []
                title = content.text.split("\n")
                for tit in title:
                    tmp2.append(tit)
                s="\n";
                s = s.join(tmp2)
                new_post = Post.objects.create(
                    club_name = Club.objects.get(club_name = club_oname),
                    uid = uid,
                    updated_on = time,
                    content = s,
                )
                # new_post.save()
                # print(uid+'\n')
                # print(s+'\n')
                data[tmp.text]=tmp2
            except NoSuchElementException:
                continue


    driver.close()
    return redirect('club',club_name=club_name)


# Different methods of waiting in selenium
    # # invisibility_of_element_located
    # title_is
    # title_contains
    # presence_of_element_located
    # visibility_of_element_located
    # visibility_of
    # presence_of_all_elements_located
    # text_to_be_present_in_element
    # text_to_be_present_in_element_value
    # frame_to_be_available_and_switch_to_it
    # invisibility_of_element_located
    # element_to_be_clickable
    # staleness_of
    # element_to_be_selected
    # element_located_to_be_selected
    # element_selection_state_to_be
    # element_located_selection_state_to_be
    # alert_is_present

# this code piece was used for waiting before for see more links
    # element = WebDriverWait(driver,20).until(
	# EC.visibility_of_element_located((By.CLASS_NAME,"see_more_link"))
	# )

    # element = WebDriverWait(driver,30).until(
	# EC.element_to_be_clickable((By.CLASS_NAME,"see_more_link"))
	# )
    # element_to_be_clickable
    # element = WebDriverWait(driver,30)
    # continue_link = driver.find_elements_by_link_text('See More')


# This was the older code for post context retrieval then to add time stamp the new one was added
    # posts = ([])
    # elem_posts = driver.find_elements_by_class_name("_5pbx")
    # for post in elem_posts:
    #     tmp = []
    #     title = post.text.split("\n")
    #     for tit in title:
    #         tmp.append(tit)
    #     posts.append(tmp);

    # if not elem_posts:
    #     print("Nothing to show.")

# This code was used for psot,time_stamp retrieval from main post div but some posts did not have sub div of text _5pbx so try/except was added
        # content=elem.find_element_by_class_name("_5pbx")
        # if not content:
        #     continue
        # print('content above\n')
        # tmp2 = []
        # title = content.text.split("\n")
        # for tit in title:
        #     tmp2.append(tit)
        #     # print(tit)
        #     # print('\n')
        # data[tmp.text]=tmp2
        # print('\n\n\n')

