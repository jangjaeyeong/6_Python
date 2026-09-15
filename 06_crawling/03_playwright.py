import requests
from config import BASE, TIMEOUT, HEADERS
from parsers import parse_stocks

ssr = requests.get(f"{BASE}/stocks", headers= HEADERS, timeout= TIMEOUT)
csr = requests.get(f"{BASE}/csr/stocks", headers= HEADERS, timeout= TIMEOUT)

print(f"{'경로':<20} {'상태':<8} {'본문 길이':>12}")
print(f"{'/stocks (SSR)' :<20} {ssr.status_code:<8} {len(ssr.text):>12}")
print(f"{'/csr/stocks (CSR)' :<20} {ssr.status_code:<8} {len(csr.text):>12}")

for line in csr.text.strip().split("\n") :
    print(f"{line}")
    
KEYWORD = 'IT서비스'
print(f"ssr --> {KEYWORD in ssr.text}")
print(f"csr --> {KEYWORD in csr.text}")
print("=" * 60)


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
    
    page.goto(f"{BASE}/csr/stocks", wait_until='domcontentloaded')
    
    page.wait_for_selector("tr.stock-row")
    count = page.locator("tr.stock-row").count()
    
    print(f" 랜더링 후 가져온 행의 개수: {count}")
    
    html = page.content()
    # print(f" page.content : {html}")
    
    items = parse_stocks(html)
    browser.close()
    
for data in items[:5] :
    print(f"{data['code']} : {data['name']} : {data['price']}")
    
    