from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
html=(root/'slides/deck.html').read_text(encoding='utf-8')
results=[]
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for label,width,height in [('desktop',1440,900),('tablet',820,1180),('mobile',390,844)]:
  page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
  errors=[]
  page.on('pageerror',lambda error:errors.append(str(error)))
  page.set_content(html,wait_until='load')
  assert page.locator('.slide.active').count()==1
  assert '01 / 12' in page.locator('#counter').inner_text()
  page.locator('#next').click()
  assert page.locator('#counter').inner_text()=='02 / 12'
  page.keyboard.press('ArrowRight')
  assert page.locator('#counter').inner_text()=='03 / 12'
  page.keyboard.press('ArrowLeft')
  assert page.locator('#counter').inner_text()=='02 / 12'
  page.locator('#sourceButton').click()
  assert 'open' in page.locator('#sourceDetails').get_attribute('class')
  page.locator('#sourceClose').click()
  assert 'open' not in page.locator('#sourceDetails').get_attribute('class')
  page.locator('#goHome').click()
  assert page.locator('#counter').inner_text()=='01 / 12'
  overflow=[]
  for i in range(12):
   page.evaluate('i=>window.location.hash="#slide-"+(i+1)',i)
   page.wait_for_timeout(60)
   extent=page.locator('.slide.active').evaluate('(el)=>({scroll:el.scrollHeight,client:el.clientHeight,width:el.scrollWidth,inner:el.clientWidth})')
   if extent['width']>extent['inner']+2:overflow.append((i+1,'horizontal',extent))
   if extent['scroll']>extent['client']+15:overflow.append((i+1,'vertical scroll',extent))
   if i in (0,2,6,8,11):
    page.screenshot(path=str(root/'reports'/f'screenshot-{label}-{i+1:02}.png'))
  results.append((label,errors,overflow))
  page.close()
 browser.close()
for label,err,overflow in results:
 print(label,'JS errors=',err,'overflow=',overflow)
