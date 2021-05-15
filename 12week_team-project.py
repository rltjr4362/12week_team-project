import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


url = 'https://www.op.gg'

driver = webdriver.Chrome('chromedriver')
driver.get(url)
driver.implicitly_wait(3)

driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[5]/a').click()


data = driver.page_source

soup = BeautifulSoup(data, 'html.parser')

df = pd.read_html(soup.prettify())[1]
print(df)

driver.quit()

a=input('게임"리그 오브 레전드" 내의 챔피언 랭킹 중 알고 싶은 순위를 입력하세요(승률,플레이수,평점,CS,골드): ')

df_1=df.loc[:,["챔피언.1",a]]
new_df=df_1.sort_values(by=[a],ascending=False)
print(new_df)

champion=list(np.array(new_df.loc[:,"챔피언.1"].tolist()))
b=list(np.array(new_df.loc[:,a].tolist()))
if a == '평점':
    for i in b:
        b+=float(i.split(':')[0])
        del b[0]
elif a== '승률':
    for i in b:
        b+=float(i.split('%')[0])
        del b[0]


print(champion)
print(b)



font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()

rc('font', family=font_name, size = 6)
x=np.arange(len(champion))
plt.figure(figsize=(20,5))
plt.bar(x,b)
plt.xticks(x,champion,rotation='vertical')
plt.title('LOL 챔피언 %s 순위'%a)
plt.show()