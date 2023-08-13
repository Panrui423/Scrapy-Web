# -*- coding: utf-8 -*-

import requests
import pandas as pd
import datetime
#import openpyxl

def get_category():
    url = 'https://api-v2.segari.id//v1/frontend-category-sortings?experimentVariant=new-categorization-two-line-without-auto-scroll'
    url = 'https://api-v2.segari.id//v1/frontend-categories/details/product-tags'
    res = requests.get(url).json()['data']
    print(res)
    df = pd.DataFrame(res)
    print(df)

def product_list():
    url = 'https://api-v2.segari.id/v1.1/products/price'
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    dt = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    print(dt)

    data_list = []
    for i in range(100):
        print(i)
        content = dict(
            agentId=311,
            size=40,
            page=i,
            paginationType='slice',
            deliveryDate=dt,
            deliveryServiceType='NEXT_DAY_DELIVERY',
        )
        res = requests.get(url, params=content).json()

        data = res['data']['data']

        data_nums = len(data)
        if data_nums == 0:
            break

        data_list = data_list + data

    df = pd.DataFrame(data_list)
    print(df)
    df2 = pd.DataFrame(list(df['productDTO']))
    print(df2)

    df = pd.concat([df2, df], axis=1, sort=False)
    print(df)
    print(df.columns)

    df.to_excel('segari_products_{}.xlsx'.format(today))




def main():
    """
        主函数

    """
    product_list()


if __name__ == '__main__':
    main()