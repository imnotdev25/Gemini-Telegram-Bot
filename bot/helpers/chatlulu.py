import re

from httpx import AsyncClient

from bot.config import CHATLULU_COOKIE, CHATLULU_AUTH


async def ChatLulu(urm: str, question: str, group_id: str, model: str) -> str:
    url = "https://chat.chatlulu.com/go/api/"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,gu;q=0.8",
        "authorization": "EUj2ju2u9IMc7CJ20aisi+V6wfFFrMeQ7p5hV9H7+EU=",
        "content-type": "application/json",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "cookie": "_gcl_au=1.1.251614921.1705500578",
        "Referer": "https://chat.chatlulu.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    resp_headers = {
        "accept": "text/event-stream",
        "Connection": "keep-alive",
        "accept-language": "en-US,en;q=0.9,gu;q=0.8",
        "cache-control": "no-cache",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "cookie": f"_gcl_au={CHATLULU_COOKIE}",
        "Referer": "https://chat.chatlulu.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    question_id = 600030
    client = AsyncClient(headers=headers)
    r = client.post(url=url + urm, json={
        "version": "1.1.1",
        "os": "andriodH5",
        "language": "zh",
        "pars": {
            "user_id": "466544",
            "question": "{}".format(question),
            "group_id": "{}".format(group_id),
            "question_id": "",
            "server_id": "1",
            "model": "{}".format(model)
        }})
    if model == "gpt-3.5":
        resp = await client.get(
            url=url + f"event/see?question_id={question_id}&group_id={group_id}&user_id=466544&token={CHATLULU_AUTH}&server_id=1",
            headers=resp_headers, timeout=30)
        data_val = re.findall(r'"Data":"(.*?)"', resp.text)
        question_id += 1
        full_resp = " ".join(data_val)
        return re.sub(r'\s{2,}', ' ', full_resp)

    elif model == "gpt-4":
        try:
            resp = await client.get(
                url=url + f"event/gpt4?question_id={question_id}&group_id={group_id}&user_id=466544&token={CHATLULU_AUTH}&server_id=1&model=gpt-4",
                headers=resp_headers, timeout=30)
            data_val = re.findall(r'"Data":"(.*?)"', resp.text)
            question_id += 1
            full_resp = " ".join(data_val)
            return re.sub(r'\s{2,}', ' ', full_resp)
        except Exception as e:
            return str(e)

    elif model == "gpt-4-dalle":
        pass
        # resp = await client.get(url=url + f"event/gpt4?question_id={question_id}&group_id={group_id}&user_id=466544&token={CHATLULU_AUTH}&server_id=1&model=gpt-4-dalle", headers=resp_headers, timeout=60)
        # return resp.text

    else:
        return "Model not found"
