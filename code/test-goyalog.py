from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options, executable_path='/opt/chrome/chromedriver')

url = 'https://blog.12jz0105.net/'
driver.get(url)

elements = driver.find_elements_by_css_selector('article.post.type-post h1.entry-title')
for elem in elements:
    # 属性の取得
    href = elem.find_element_by_tag_name('a').get_attribute('href')
    print('{}<{}>'.format(elem.text, href))

driver.quit()