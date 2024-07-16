import re

from httpx import AsyncClient


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
