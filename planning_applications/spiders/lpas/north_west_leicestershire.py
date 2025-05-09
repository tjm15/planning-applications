from typing import List

from planning_applications.spiders.idox import IdoxSpider


class NorthWestLeicestershireSpider(IdoxSpider):
    name: str = "north_west_leicestershire"
    domain: str = "plans.nwleics.gov.uk"
    allowed_domains: List[str] = [domain]
    start_url: str = f"https://{domain}/public-access/search.do"
    arcgis_url: str = f"https://{domain}/server/rest/services/PALIVE/LIVEUniformPA_Planning/FeatureServer/2/query"
