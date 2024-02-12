import os
import re

import matplotlib.pyplot as plt
import seaborn as sns
from httpx import AsyncClient

from bot.helpers.functions import random_string, AsyncPlotter


async def get_price_history(message: str) -> str:
    headers = {'Host': 'price-history.in', 'Content-Type': 'application/json'}
    client = AsyncClient(headers=headers)
    try:
        response = await client.post('https://price-history.in/api/search',
                                     json={'url': message}, timeout=20)
        match = re.search(r'([A-Za-z0-9]+)$', response.json()['code'])
        response_2 = await client.post(f'https://price-history.in/api/price/{match.group(1)}', timeout=20)
        await client.aclose()
        data = response_2.json()['History']['Price']
        x = [i['x'] for i in data]
        y = [i['y'] for i in data]
        data_2 = response_2.json()['Price']
        y_1 = [data_2['Price'], data_2['MRP'], data_2['MinPrice'], data_2['MaxPrice'], data_2['OfferPrice'],
               data_2['MinOfferPrice']]
        x_1 = [data_2['UpdatedOn'], data_2['MinOfferPriceOn'], data_2['MinPriceOn'], data_2['MaxPriceOn'],
               data_2['UpdatedOn'], data_2['MinOfferPriceOn']]
        a = AsyncPlotter()
        plt.figure()
        plt.title("Price History")
        fig, axs = plt.subplots(2, 1)
        sns.lineplot(x=x, y=y, ax=axs[0], color='#274D61')
        sns.scatterplot(x=x_1, y=y_1, ax=axs[1], color="#69B0AC")
        labels = ["Current", "MRP", "Min", "Max", "Offer", "MinO"]
        for i, txt in enumerate(labels):
            axs[1].annotate(txt, (x_1[i], y_1[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10)
        path = os.getcwd() + f"images/{random_string(5)}.png"
        a.save(fig, path)
        a.join()
        return os.getcwd() + path

    except Exception as e:
        return f"Something went wrong while generating image. Error: {e}"


async def get_price_history_text(message: str) -> str:
    headers = {'Host': 'price-history.in', 'Content-Type': 'application/json'}
    client = AsyncClient(headers=headers)
    try:
        response = await client.post('https://price-history.in/api/search',
                                     json={'url': message})
        match = re.search(r'([A-Za-z0-9]+)$', response.json()['code'])
        response_2 = await client.post(f'https://price-history.in/api/price/{match.group(1)}')
        await client.aclose()
        data_2 = response_2.json()['Price']
        string_msg = f"""
        ** Price History **
        **Current Price** : {data_2['Price']} Date: {data_2['UpdatedOn']}
        **MRP** : {data_2['MRP']}
        **Min Price** : {data_2['MinPrice']} Date: {data_2['MinPriceOn']}
        **Max Price** : {data_2['MaxPrice']} Date: {data_2['MaxPriceOn']}
        **Offer Price** : {data_2['OfferPrice']} Date: {data_2['UpdatedOn']}
        **Min Offer Price** : {data_2['MinOfferPrice']} Date: {data_2['MinOfferPriceOn']}
        """
        return string_msg

    except Exception as e:
        return f"Something went wrong while generating text. Error: {e}"
