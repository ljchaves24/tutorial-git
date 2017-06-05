import time
from scrapy.cmdline import execute
from scrapy.crawler import CrawlerProcess, CrawlerRunner, Crawler
from scrapy.settings import Settings
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from scrapy import signals, log
from twisted.internet import defer
from twisted.internet import reactor

from xoftix_spider.spiders.s_abogados import SAbogadosSpider
from xoftix_spider.spiders.s_colpsic import SColpsicSpider
from xoftix_spider.spiders.s_copnia import SCopniaSpider
from xoftix_spider.spiders.s_copnia_sanciones import SCopniaSancionesSpider
from xoftix_spider.spiders.s_cpae import SCpaeSpider
from xoftix_spider.spiders.s_dian import SDianSpider
from xoftix_spider.spiders.s_docsrec import SDocsrecSpider
from xoftix_spider.spiders.s_ejercito import SEjercitoSpider
from xoftix_spider.spiders.s_icetex import SIcetexSpider
from xoftix_spider.spiders.s_lista_clinton import SListaClintonSpider
from xoftix_spider.spiders.s_policia import SPoliciaSpider
from xoftix_spider.spiders.s_procuraduria import SProcuraduriaSpider
from xoftix_spider.spiders.s_ramajudicial import SRamajudicialSpider
from xoftix_spider.spiders.s_registraduria import SRegistraduriaSpider
from xoftix_spider.spiders.s_ruaf import SRuafSpider
from xoftix_spider.spiders.s_sena import SSenaSpider
from xoftix_spider.spiders.s_simit import SSimitSpider
from xoftix_spider.spiders.s_sisben import SSisbenSpider
from xoftix_spider.spiders.s_sispro import SSisproSpider
from xoftix_spider.spiders.s_votacion import SVotacionSpider

list_id=['79370274','1016050122','1074185299','51883340','38460425','3227987', '8266340', '70085071',
'45762585','52833687', '1062304263', '3227987','52833687', '1062304263','342573','347277', '358674',
         '358674','7120755', '12991321', '15816239', '18904273', '21070556', '22605456', '24344642',
         '24581985', '24581985', '24581985', '33115532', '36753340', '43576318', '52796865', '60443604',
         '73194220', '98712903', '1000062609', '1000105096', '1000136301', '1000136301', '1000193401',
         '1000211307', '1000396853', '1000405044', '1000405044', '1000456019', '1000570111', '1000726483',
         '1000780562', '1000785538', '1000785538', '1000791799', '1000791799', '1000791799', '1000832689',
         '1000932616', '1000933280', '1000948333', '1001013859', '1001013859', '1001058314', '1001137338',
         '1001137338', '1001168433', '1001199461']
'''list_id = ['79370274','1016050122','1074185299']'''


configure_logging()
settings = Settings()
settings.set('ITEM_PIPELINES', {
    'xoftix_spider.pipelines.XoftixSpiderPipeline': 100
})
process = CrawlerRunner(settings)
@defer.inlineCallbacks
def crawl():
    for i in list_id:
        #yield process.crawl(SRuafSpider, id=i)
        yield process.crawl(SSimitSpider, id=i)
        yield process.crawl(SSisbenSpider, id=i)
        yield process.crawl(SVotacionSpider, id=i)
        yield process.crawl(SSenaSpider, id=i)
        yield process.crawl(SDianSpider, id=i)
        yield process.crawl(SIcetexSpider, id=i)
        yield process.crawl(SListaClintonSpider, id=i)
        yield process.crawl(SEjercitoSpider, id=i)
        yield process.crawl(SRegistraduriaSpider, id=i)
        yield process.crawl(SCopniaSpider, id=i)
        yield process.crawl(SCopniaSancionesSpider, id=i)
        yield process.crawl(SSisproSpider, id=i)
        yield process.crawl(SColpsicSpider, id=i)
        yield process.crawl(SCpaeSpider, id=i)
        yield process.crawl(SDocsrecSpider, id=i)
        yield process.crawl(SProcuraduriaSpider, id=i)
        yield process.crawl(SAbogadosSpider, id=i)
        yield process.crawl(SPoliciaSpider, id=i)
        yield process.crawl(SRamajudicialSpider, id=i)
    reactor.stop()
crawl()
reactor.run()


