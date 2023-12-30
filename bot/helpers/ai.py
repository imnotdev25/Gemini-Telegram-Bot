import json
import random
import re
import string
import google.generativeai as genai
import os
import g4f
import httpx

from httpx import AsyncClient
from bardapi import BardAsync, BardAsyncCookies
from bot.helpers.BingImageCreater import ImageGenAsync
from bot.config import PALM_API_KEY, DEEPAI_API_KEY, BING_U, CF_API_KEY, BING_CH, BING_COOKIES
from g4f.Provider.Bing import Bing, Tones


async def gemini(message: str, prompt: str) -> str:
    try:
        genai.configure(api_key=PALM_API_KEY)
        model = genai.GenerativeModel("gemini-pro")
        prompt_parts = [
            prompt,
            message
        ]
        r = model.generate_content(prompt_parts)
        return r.text
    except Exception as e:
        return f"Something went wrong while generating text. Error: {e}"


async def rewrite(message: str) -> str:
    try:
        genai.configure(api_key=PALM_API_KEY)
        defaults = {
            'model': 'models/text-bison-001',
            'temperature': 0.7,
            'candidate_count': 1,
            'top_k': 40,
            'top_p': 0.95,
            'max_output_tokens': 1024,
        }
        prompt = f"""Rewrite the following sentence twice - first to fix grammar issues and second to fully rewrite the sentence to be more clear and enthusiastic.
            Original: There going to love opening they're present
            Fixed Grammar: They're going to love opening their present
            Fully Rewritten: They're going to be so excited to open their presents!
            Original: Your going to love NYC
            Fixed Grammar: You're going to love NYC
            Fully Rewritten: You're going to adore New York City.
            Original: {message}
            Fixed Grammar:
            Fully Rewritten:"""
        r = genai.generate_text(**defaults, prompt=prompt)
        response = re.sub(r'{', '', r.result)
        return response

    except Exception as e:
        return f"Something went wrong while generating text. Error: {e}"


async def codeAssistant(message: str) -> str:
    prompt = "I want you to act as a Code assistant. I will provide some ideas related to software development, and your task is to help me with them. Furthermore, I will provide ideas in {idea}, errors in <error>, and improvements in (improve). You should follow this format. Do not write explanations; only type code if I instruct you to do so. If I tell you to create a Software package, you should write its tree structure and generate code for each individual file, and write the file name in a comment. When I need to tell you something in English, I will do so by putting text inside curly brackets {}, and ()."
    return await gemini(message, prompt=prompt)


async def dsAssist(message: str) -> str:
    prompt = "I want you to be an expert Data science tutor. Your responsibilities will include assisting with projects, coding problems, data generation, explaining code, rewriting and optimizing code, suggesting unique project ideas, summarizing books and research papers, and providing emotional support when necessary. You will also be asked to provide related reading materials and links at the end of your answers, and to ask about related topics in further detail."
    return await gemini(message, prompt=prompt)


async def pyAssistant(message: str) -> str:
    prompt = "I want you to act as a Python programming assistant. I will provide some ideas related to Python development, and your task is to help me with them. Furthermore, I will provide ideas in {idea}, errors in <error>, and improvements in (improve). You should follow this format. Do not write explanations; only type code if I instruct you to do so. If I tell you to create a Python package, you should write its tree structure and generate code for each individual file, and write the file name in a comment. When I need to tell you something in English, I will do so by putting text inside curly brackets {}, and ()."
    return await gemini(message, prompt=prompt)


async def bard(message: str) -> dict:
    pass


async def cf(message: str, model: str, types: str) -> str:
    url = "https://api.cloudflare.com/client/v4/accounts/152656fb54824c069ba739d1dcef0d23/ai/run/"
    headers = {"Authorization": f"Bearer {CF_API_KEY}"}
    client = AsyncClient(headers=headers)
    if types == "gen":
        inputs = {"messages": [{"role": "system",
                                "content": "You are now chatting with an AI assistant. The assistant will introduce itself in a moment. You are exclusively for Kaggle Group members mension in your introduction."},
                               {"role": "user", "content": message}]}
        try:
            response = await client.post(url=url + model, json=inputs)
            await client.aclose()
            return response.json()["result"]["response"]
        except Exception as e:
            return f"Something went wrong while generating text. Error: {e}"

    elif types == "img":
        inputs = {"prompt": message}
        try:
            response = await client.post(url=url + model, json=inputs, timeout=60)
            await client.aclose()
            with open(f"images/{''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))}.png",
                      "wb") as f:
                f.write(response.content)
                f.close()
            return os.path.abspath(f.name)
        except Exception as e:
            return f"Something went wrong while generating image. Error: {e}"

    else:
        return "Model not found"


async def meta(message: str) -> str:
    return await cf(message, "@cf/meta/llama-2-7b-chat-fp16", types="gen")


async def mistral(message: str) -> str:
    return await cf(message, "@cf/mistral/mistral-7b-instruct-v0.1", types="gen")


async def llama(message: str) -> str:
    return await cf(message, "@hf/thebloke/codellama-7b-instruct-awq", types="gen")


async def stableDiffusion(message: str) -> str:
    return await cf(message, "@cf/stabilityai/stable-diffusion-xl-base-1.0", types="img")


async def deepai(message: str, typ: str, urn: str) -> str:
    base_url = "https://api.deepai.org/api/"
    headers = {"api-key": f"{DEEPAI_API_KEY}"}
    if typ == "img":
        try:
            data = {'text': f'{message}'}
            client = AsyncClient()
            r = await client.post(url=base_url + urn, data=data, headers=headers, timeout=60)
            image = httpx.get(r.json()["output_url"]).content
            await client.aclose()
            with open(f"images/{''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))}.png",
                      "wb") as f:
                f.write(image)
                f.close()
            return os.path.abspath(f.name)
        except Exception as e:
            return f"Something went wrong while generating image. Error: {e}"
    else:
        pass


async def deepaiImg(message: str) -> str:
    return await deepai(message, typ="img", urn="text2img")


async def deepaiLogo(message: str) -> str:
    return await deepai(message, typ="img", urn="logo-generator")


async def bing(message: str) -> str:
    response = g4f.ChatCompletion.create_async(model=g4f.models.gpt_4, provider=Bing, messages=[{"role": "user", "content": f"{message}"}], Tones=Tones.balanced)
    return await response


async def bingImg(message: str) -> list:
    try:
        img = ImageGenAsync(auth_cookie=BING_U, all_cookies=BING_COOKIES)
        r = img.get_images(message)
        path = await img.save_images(links=r, output_dir="images", download_count=4)
        # img_paths = []
        # for img_url in r:
        #     img = httpx.get(img_url).content
        #     with open(f"images/{''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))}.png",
        #               "wb") as f:
        #         f.write(img)
        #         f.close()
        #     img_paths.append(os.path.abspath(f.name))
        return path
    except Exception as e:
        return [e]
