# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from flask import Flask, render_template, redirect
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import re

def init_browser():
    executable_path = {'executable_path': 'chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser=init_browser()
    mars_dict={}

    # URL of page to be scraped
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html=browser.html
    soup=bs(html,'html.parser')


    # Retrieve the latest news title
    news_title=soup.find_all('div', class_='content_title')[0].text
    # Retrieve the latest news paragraph
    news_p=soup.find_all('div', class_='article_teaser_body')[0].text
    news_title
    news_p

    # JPL Mars Space Images - Featured Image
    jpl_url="https://spaceimages-mars.com/"
    browser.visit(jpl_url)
    html=browser.html
    soup=bs(html,'html.parser')
    image_url=str(soup.find_all('img', class_='headerimage')[0])
    image_url=str(image_url.split(" ")[3])
    image_url=re.findall('"([^"]*)"',image_url)[0]
    featured_image_url=jpl_url + image_url
    featured_image_url

    # Scrape Mars facts 
    url='https://galaxyfacts-mars.com/'
    tables=pd.read_html(url)
    tables

    mars_fact=tables[0]
    mars_fact=mars_fact.rename(columns={0:"Profile",1:"Value"},errors="raise")
    mars_fact.set_index("Profile",inplace=True)
    mars_fact

    fact_table=mars_fact.to_html()
    fact_table

    fact_table.replace('\n','')

    # Scrape Mars hemisphere title and image
    mars_url='https://marshemispheres.com/'
    browser.visit(mars_url)
    html=browser.html
    soup=bs(html,'html.parser')

    # Extract hemispheres item elements
    mars_hems=soup.find('div',class_='collapsible results')
    mars_item=mars_hems.find_all('div',class_='item')
    hemisphere_image_urls=[]

    # Loop through each hemisphere item
    for item in mars_item:
        # Error handling
        try:
            # Extract title
            hem=item.find('div',class_='description')
            title=hem.h3.text
            # Extract image url
            hem_url=hem.a['href']
            browser.visit(mars_url+hem_url)
            html=browser.html
            soup=bs(html,'html.parser')
            image_src=soup.find('li').a['href']
            if (title and image_src):
                # Print results
                print('-'*50)
                print(title)
                print(image_src)
            # Create dictionary for title and url
            hem_dict={
                'title':title,
                'image_url': mars_url + image_src
            }
            hemisphere_image_urls.append(hem_dict)
        except Exception as e:
            print(e)

    # Create dictionary for all info scraped from sources above
    mars_dict={
        "news_title":news_title,
        "news_p":news_p,
        "featured_image_url":featured_image_url,
        "fact_table":fact_table,
        "hemisphere_images":hemisphere_image_urls
    }

    mars_dict

    # Close the browser after scraping
    browser.quit()
    return mars_dict
    