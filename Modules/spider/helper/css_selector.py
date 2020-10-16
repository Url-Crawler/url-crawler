from scrapy.selector import Selector

class CssSelector():
    
    def extracting_href(self,response):
        
        href = response.css('a:not([href^="http"])')
        href = href.css('a:not([href^="partners"])')
        href = href.css('a:not([href^="#"])')
        href = href.css('a:not([href="/mobil"])')
        href = href.css('a:not([href^="{"])')
        href = href.css('a:not([href^="//js"])')
        href = href.css('a:not([href^="/www"])')
        href = href.css('a:not([href^="//www"])')
        href = href.css('a:not([href=""])')
        href = href.css('a:not([href^="mailto:"])')
        href = href.css('a:not([href^="Javascript:"])')
        #href = href.xpath('//a[not(contains(@href, ":"))]')
        href = href.css('a:not([href^="//"])')
        href = href.css('a:not([href^="javascript"])::attr(href)')

        return href