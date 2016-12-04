import scrapy

from baseballscraper.items import GameItem

class GameSpider(scrapy.Spider):
    name = "game"
    allowed_domains = ["cpbl.com.tw"]
    
    def __init__(self, team=None, syear=None, *args, **kwargs):
        super(GameSpider, self).__init__(*args, **kwargs)
        self.team = team
        self.syear = syear
        self.start_urls = ['http://www.cpbl.com.tw/web/team_dayscore.php?&gameno=01&team=%s&syear=%s' % (team, syear)]

    def parse(self, response):
        
        y_game_no = [self.syear + '-' + no for no in response.css('table.mix_x tr td:nth-child(1)::text').extract()]
        stadium = response.css('table.mix_x tr td:nth-child(2)::text').extract()
        
        d = response.css('table.mix_x tr td:nth-child(3)::text').extract()
        t = response.css('table.mix_x tr td:nth-child(4)::text').extract()
        
        date = []
        for i in range(0, len(d)):
            date.append(d[i] + ' ' + t[i])
        
        away_team = response.css('table.mix_x tr td:nth-child(5) a::text').extract()
        away_team_score = response.css('table.mix_x tr td:nth-child(6)::text').extract()
        
        home_team = response.css('table.mix_x tr td:nth-child(7) a::text').extract()
        home_team_score = response.css('table.mix_x tr td:nth-child(8)::text').extract()
        
        
        win_team = response.css('table.mix_x tr td:nth-child(9)::text').extract()
        win_team = [w.strip() for w in win_team]
        
        
        for i in range(0, len(d)):
            g = GameItem(
                y_game_no=y_game_no[i], 
                stadium=stadium[i], 
                date=date[i], 
                away_team=away_team[i], 
                away_team_score=away_team_score[i],
                home_team=home_team[i], 
                home_team_score=home_team_score[i], 
                win_team=win_team[i]  
            )
            
            try:
                g.save()
            except:
                continue
        #return gameItemList