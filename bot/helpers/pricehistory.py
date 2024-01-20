import os
import re

from httpx import AsyncClient
from plotly import graph_objects as go
from plotly.subplots import make_subplots

from bot.helpers.functions import random_string


async def get_price_history(message: str) -> str:
    headers = {'Host': 'price-history.in', 'Content-Type': 'application/json'}
    client = AsyncClient(headers=headers)
    try:
        response = await client.post('https://price-history.in/api/search',
                                     json={'url': message})
        match = re.search(r'([A-Za-z0-9]+)$', response.json()['code'])
        response_2 = await client.post(f'https://price-history.in/api/price/{match.group(1)}')
        await client.aclose()
        data = response_2.json()['History']['Price']
        x = [i['x'] for i in data]
        y = [i['y'] for i in data]
        data_2 = response_2.json()['Price']
        y_1 = [data_2['Price'], data_2['MRP'], data_2['MinPrice'], data_2['MaxPrice'], data_2['OfferPrice'],
               data_2['MinOfferPrice']]
        x_1 = [data_2['UpdatedOn'], data_2['MinOfferPriceOn'], data_2['MinPriceOn'], data_2['MaxPriceOn'],
               data_2['UpdatedOn'], data_2['MinOfferPriceOn']]
        fig = make_subplots(rows=2, cols=1, shared_yaxes=True, start_cell="top-left",
                            x_title="Date", y_title="Price")
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Price History', line=dict(color='#274D61')), row=1,
                      col=1)
        fig.add_trace(
            go.Scatter(x=x_1, y=y_1, mode='markers+text', text=["Current", "MRP", "Min", "Max", "Offer", "MinO"],
                       textposition="middle right", name="Price", marker=dict(color='#69B0AC', size=10)), row=2, col=1)
        fig.update_layout(height=720, width=1080, title_text="Price History", title_x=0.5,
                          font=dict(family="Courier New, monospace", size=16, color="#7f7f7f"))
        path = os.getcwd() + f"images/{random_string(5)}.png"
        fig.write_image(path)
        yield path

    except Exception as e:
        yield f"Something went wrong while generating image. Error: {e}"


async def get_price_history_text(message: str) -> str:
    headers = {'Host': 'price-history.in', 'Content-Type': 'application/json'}
    client = AsyncClient(headers=headers)
    try:
        response = await client.post('https://price-history.in/https://price-history.in/api/search',
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
