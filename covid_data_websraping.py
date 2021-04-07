from selenium import webdriver
import time
import pandas as pd
cd="C:\\Users\\Pranati\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
driver = webdriver.Chrome(cd)
url = "https://www.mohfw.gov.in/"
driver.get(url)
time.sleep(10)
button = driver.find_element_by_xpath('//*[@id="state-data"]/div/div/div/h2/a')
button.click()

column_name = ['Seral_no', 'Name_of_State/UT', 'Active Cases', 'AC_Change','Cured','Cured_Change','Deaths', 'Death_Change']
df = pd.DataFrame(columns=column_name)

for i in range(1,36):
    d={}
    for j in range(1,9):
        w=driver.find_element_by_xpath('//*[@id="state-data"]/div/div/div/div/table/tbody/tr['+str(i)+']/td['+str(j)+']')
        d[df.columns[j-1]]=w.text
    df=df.append(d,ignore_index=True) 

df.to_csv(("C:\\Users\\Pranati\\covid19_data.csv"), index = False)
