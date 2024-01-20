import os

from httpx import AsyncClient

from bot.helpers.functions import random_string


async def msCreate(message: str) -> str:
    try:
        headers = {
            'authority': 'designerapp.officeapps.live.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,gu;q=0.8',
            'audiencegroup': 'Production',
            'authorization': 'Bearer eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkExMjhDQkMtSFMyNTYiLCJ4NXQiOiJUWWRVektQcVBCVGRSN0NlTExvZ2hsVk9kRjgiLCJ6aXAiOiJERUYifQ.iH-Kz1wRIautMBshy_Izc7sn6ruYHQTkX6p3wSkkAdwDVDWt2SO6eHv7OxQMN7kmXtMQzPs3rHPNET07l4ak8GdOs6grM85K2MZOytsrKGdwN64veM085_WWrW40HIPSJQbXMRo12mhxrScrc1ev5sdSxPsklzYlC1wCchfdO-bn_yKL28HlgPbCxzNXsrCylhCxNxLHoMMvjzb0pLKyuXOSg1yQ1pNIkCHUJ3OizxproHv7jiokhNnAjmTarF0GVeq7D13RJtjQzj1NC_8bVhhrfNgGy5puDg6k8QbYiVhuS8AEIGJoSyU_QJ-zQhrGK49IcD_gPGDMMxr7_gTboA.ksvjJV-yecmHtb4imOYI3Q.3XmrU0NmJaAQrHjOEQ0Tnlp5hn1yQTg-33DN31uK5evbpnG4kLFmIgSgngXigLiQoaPVuA4cltM_iCQAppivdc6TvEiyrvapsQLQaGtScP-fcUyfo3pr1BCoJ0rp-YWzTsss_iz-3104FDQro8FxjKhD36AeZct5HofNmI2YSeVYMH9gA40rRS_lDE_PXvYJiWumNvGZbr6UDw-PGe_b5dBu5upoEG80Xi8O4WuZK-SDH76nKNKqtMQ04P8Au8Pp2l-lFGvfVeJH5HYe8n_WYg6xEgoLSktqbzD9g6wdWJLd9PkaNAi7U3cdvj21sdrpf8rWCQX1keSxnzMQa91SY_g-B-EWHGofTYWRbFhQyvFw1AGuBEW__-HZqh0C6OSTZhzvUSRTl4nXJTtVXMxkY8NxwlQAgINWdbQzQPF3aa4JRy6L4V9S-ChX0NJHtHmi71uQUXpcpOQFxyMI-EiXMZc2660s31-08KDQp0OozVGE46rfNnJ0ky2PyBWaA6VZHU1QZ58Kkh6viPRUjzaTsVcqVMaXTVEYNH2o5i6einq_cpLu1zr7j5dtzNNH6zD-bN-0kTIyfnr5QPn81Le92EQuHdaN7bqwHrQPMfA7diB-h9aHUcoGdi9qOnUvGV_LkIz45rybn7LR2gUCH65_yiVwANmkqiUXVPysq3Xaud_840N-S2tvO1zqltHOvEz3vGo0OgEtcjO_NTMY2JSvHaOMe12djUOocUCDrufqY1vt2CNOzvi5w7PpjkhU2Pbxar1MejCEVzOED28z3BcaWJBdzSdV7tD7vp8Cj45_U341Xu9c5bUt5clBdkEqFnhs4BCogriyHWf3ycm1a_DWhKFK9qcJ_gRyNcrTr0yJDUjBVdCNgfYJB-Ga9xieuD_sVhtDYsz_-6DVJhS8zg2rUVejD-q9S_A-ykXAiAI5hft8ZeETZzGbHzCFNn-jlBkkH1YkmYLq3sObCSuF7r6cDfmEGMUd0QvfM_wqdBwqAbyj4MvLbIRwPPZtShxRT90Nb0CnQEasJdzje70AgMmTRKmkngxW5fCgj-rrsiPeFHOrm_7Xy43Hvb6Xeg6Q3-_iGJitjkfXj3VqK9owMZRe5H8TWnsIyGq0CZUj4-EyjXsw9-dT3Euzmd2s0Kzzcuq9JY60ffE6gVd-D4cvm_PhEkX6XbXSDbRYUgDEf-l1NEGYsdjlRP4N4O_r1bu5UOat53Yw6JInfOWBPktQJwXcdVmD6k5aZ0qlfR4FfCfhBjADDTM7rz6UsOCGqR6_wayt-EXVbcpTV9UbaEas5Sic4gQspaHplRuRhRTksu_KyJoYkM4xEFBInrsNz6YjKduNMKmOV_ZYvJoempv4hHmMRASnsyY09pp0l0U71VRPsoAa9rBgBhJ1swZS8UwL7aLzQ4NrC0YpP5IDDR98Vo-XwD8SuHs7Xv56qhzHIEFyg2o.5pUI3iVScu-CkxkEiUH29w',
            'cache-control': 'no-cache',
            'caller': 'DesignerApp',
            'clientbuild': '1.0.20240118.13',
            'clientid': '7531be36-4ab1-463a-90ed-5dfd4901681a',
            'clientname': 'DesignerApp',
            'containerid': '66c3fa85-4741-4078-90c3-ec30ebb7c793',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryzdakYnMWm0iQFcfO',
            'dnt': '1',
            'filetoken': '6d4b6b5d-ab5b-4b57-b6c5-d19ffa8e8394',
            'hostapp': 'DesignerApp',
            'issignedinuser': 'true',
            'origin': 'https://designer.microsoft.com',
            'platform': 'Web',
            'pragma': 'no-cache',
            'referer': 'https://designer.microsoft.com/',
            'releasechannel': '',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'sessionid': 'd5b3d77e-5e67-475f-8960-d837135e3d41',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'userid': 'dbf260747391f780',
            'usertype': 'MSA',
            'x-correlation': '531d1d9c-99be-4881-9860-6050175a02fd',
            'x-dc-hint': 'IndiaCentral',
            'x-req-start': '1918993.6999999993',
        }


        params = {
        'action': 'GetDallEImagesCogSci',
        }

        data = f'------WebKitFormBoundaryzdakYnMWm0iQFcfO\r\nContent-Disposition: form-data; name="dalle-caption"\r\n\r\n{message}\r\n------WebKitFormBoundaryzdakYnMWm0iQFcfO\r\nContent-Disposition: form-data; name="dalle-scenario-name"\r\n\r\nTextToImage\r\n------WebKitFormBoundaryzdakYnMWm0iQFcfO\r\nContent-Disposition: form-data; name="dalle-batch-size"\r\n\r\n1\r\n------WebKitFormBoundaryzdakYnMWm0iQFcfO\r\nContent-Disposition: form-data; name="dalle-image-response-format"\r\n\r\nUrlWithBase64Thumbnail\r\n------WebKitFormBoundaryzdakYnMWm0iQFcfO\r\nContent-Disposition: form-data; name="dalle-seed"\r\n\r\n112\r\n------WebKitFormBoundaryzdakYnMWm0iQFcfO--\r\n'
        client = AsyncClient(headers=headers)
        response = await client.post(
            'https://designerapp.officeapps.live.com/designerapp/DallE.ashx',
            params=params,
            data=data,
            timeout=60
        )
        img = await client.get(response.json()['image_urls_thumbnail'][0]['ImageUrl'])
        await client.aclose()
        with open(f"images/{random_string(5)}.jpg", "wb") as f:
            f.write(img.content)
            f.close()
        return os.path.abspath(f.name)

    except Exception as e:
        return str(e)
