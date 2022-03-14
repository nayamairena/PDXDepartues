# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

#Utilize https://scrapy.org/ library to scrape info from PDX website
#Data pulled from: https://www.flypdx.com/Flights#/type/Arrivals/day/Today/timerange
#My plan is to pull only the departure times for the D gates
#My job is located in the D concourse and every morning the times are printed out
#But were manually copied and pasted, so I want to create this program so that it is an easier process
#By pulling all the data and putting it in a file ready to print. 


import scrapy


class PdxtimesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
