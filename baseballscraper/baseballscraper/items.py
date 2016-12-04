# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy_djangoitem import DjangoItem
from game.models import Game

class GameItem(DjangoItem):
    django_model = Game

"""
class GameItem(scrapy.Item):
    game_no = scrapy.Field()
    stadium = scrapy.Field()
"""