"""
Author:Ravi Shah
Date: feb 8 2020
purpose: TO predict the stock price of the market.
"""

import numpy as np
from datetime import datetime
import smtplib
from selenium import webdriver
from sklearn.linear_model import LinearRegression
#from sklearn import preprocessing,svm,cross_validation
from sklearn import preprocessing, svm
from iexfinance.stocks import get_historical_data
from sklearn.model_selection import cross_validate
import chromedriver_binary

def getStocks(n):
    url = r"https://finance.yahoo.com/screener/predefined/aggressive_small_caps?offset=0&count=202"
    driver = webdriver.chrome()
    driver.get(url)
    stock_list = []
    n +=1
    #xpath=//*[@id=”scr-res-table”]/div[2]/table/tbody/tr[57]/td[1]/a

    for i in range(1,n):
        ticker = driver.find_element_by_xpath('//*[@id = “scr-res-table”]/div[2]/table/tbody/tr[‘ + str(i) +‘]/td[1]/a')
        stock_list.append((ticker))
    driver.quit()

    for i in stock_list:
        print('Data:')
        print (i)
    # for i in stock_list:
    #     try:
    #         predictData(i,5)
    #     except:
    #         print("Stock: " + i + " was not predicted")
    start = datetime(2019, 1, 1)
    end = datetime.now()
getStocks(45)