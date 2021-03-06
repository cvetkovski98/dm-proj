# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Song(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field()
    title = scrapy.Field()
    artist = scrapy.Field()
    production_house = scrapy.Field()
    chart_position = scrapy.Field()
    count = scrapy.Field()


class SongUK(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field()
    title = scrapy.Field()
    artist = scrapy.Field()
    production_house = scrapy.Field()
    chart_position = scrapy.Field()
    week = scrapy.Field()
    weeks_on_chart = scrapy.Field()


class ShazamSong(scrapy.Item):
    country = scrapy.Field()
    title = scrapy.Field()
    artist = scrapy.Field()
    chart_position = scrapy.Field()
