"""
    실습용 사이트에서 종목 메뉴 페이지(SSR) 의 섹터를 "IT 서비스"로 검색한 결과 데이터를 추출
    
    -요청 주소: ??
"""

import requests
from config import BASE, TIMEOUT, HEADERS
from parsers import parse_stocks

ssr = requests.get(f"{BASE}/stocks?sector=S08&market=&q=", headers= HEADERS, timeout= TIMEOUT)
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    context = browser.new_context(locale="ko-KR", viewport={"width": 1280, "height" : 720})
    
    page = context.new_page()
    
    page.route(
        "**/*",
        lambda route: route.abort() if route.request.resource_type in {"image", "font", "media"}
        else route.continue_()
    )
    
    page.goto(f"{BASE}/stocks?sector=S08&market=&q=", wait_until='domcontentloaded')
    
    page.wait_for_selector("tr.stock-row")
    count = page.locator("tr.stock-row").count()
    
    print(f" 랜더링 후 가져온 행의 개수: {count}")
    
    html = page.content()

    items = parse_stocks(html)
    browser.close()

print("코드 \t 종목 \t\t 섹터 \t 가격 \t 등락률   거래량")
for data in items :
    print(f"{data['code']} : {data['name']} : {data['sector']} : {data['price']} :  {data['rate']} : {data['volume']}")