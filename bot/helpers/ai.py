import os
import re
import g4f
import google.generativeai as genai
import httpx

from g4f.client import Client as BingClient
from httpx import AsyncClient
from typing import Dict
# from bot.helpers.BingImageCreater import ImageGenAsync
from bot.config import PALM_API_KEY, DEEPAI_API_KEY, CF_API_KEY, NVIDIA_API_KEY, OPENAI_API_KEY
from bot.helpers.functions import random_string
from openai import OpenAI


async def openai_helper(message: str, model: str = "gpt-4-turbo", *args) -> str:
    client = OpenAI(api_key=OPENAI_API_KEY, timeout=10)

    if args[0] == "gen":
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ]
        )
        return response.choices[0].message.content
    if args[0] == "img":
        response = client.images.generate(
            model="dall-e-3",
            prompt=message,
            size="1024x1024",
            quality="hd",
            n=1,
        )
        client_ = AsyncClient()
        image = await client_.get(response.images[0].url)
        await client_.aclose()
        with open(f"images/{random_string(10)}.png", "wb") as f:
            f.write(image.content)
            f.close()
        return os.path.abspath(f.name)


async def chatgpt4(message: str) -> str:
    response = await openai_helper(message, "gpt-4-turbo", "gen")
    return response


async def chatgpt4o(message: str) -> str:
    response = await openai_helper(message, "gpt-4o", "gen")
    return response


async def dall_e(message: str) -> str:
    response = await openai_helper(message, "dall-e-3", "img")
    return response


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
            """
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


async def cf(message: str, model: str, types: str) -> str:
    url = "https://api.cloudflare.com/client/v4/accounts/152656fb54824c069ba739d1dcef0d23/ai/run/"
    headers = {"Authorization": f"Bearer {CF_API_KEY}"}
    client = AsyncClient(headers=headers)
    if types == "gen":
        inputs = {"messages": [{"role": "system",
                                "content": "You are friendly AI assistant. Answer users query"},
                               {"role": "user", "content": message}]}
        try:
            response = await client.post(url=url + model, json=inputs, timeout=60)
            await client.aclose()
            return response.json()["result"]["response"]
        except Exception as e:
            return f"Something went wrong while generating text. Error: {e}"

    elif types == "img":
        inputs = {"prompt": message}
        try:
            try:
                os.mkdir("images")
            except:
                pass
            response = await client.post(url=url + model, json=inputs, timeout=60)
            await client.aclose()
            with open(f"images/{random_string(10)}.png",
                      "wb") as f:
                f.write(response.content)
                f.close()
            return os.path.abspath(f.name)
        except Exception as e:
            return f"Something went wrong while generating image. Error: {e}"

    elif types == "bin":
        inputs = {"prompt": message}
        try:
            response = await client.post(url=url + model, json=inputs, timeout=60)
            await client.aclose()
            with open(f"images/{random_string(10)}.png",
                      "wb") as f:
                f.write(response.content)
                f.close()
            return os.path.abspath(f.name)

        except Exception as e:
            return f"Something went wrong while generating text. Error: {e}"

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


async def dreamShaper(message: str) -> str:
    return await cf(message, "@cf/lykon/dreamshaper-8-lcm", types="bin")


async def stableDiffusionIn(message: str) -> str:
    return await cf(message, "@cf/bytedance/stable-diffusion-xl-lightning", types="bin")


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
            with open(f"images/{random_string(10)}.png",
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
    bgc = BingClient()
    response = bgc.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"{message}"}],
    )
    return response.choices[0].message.content


async def claude(message: str) -> str:
    try:
        response = g4f.ChatCompletion.create_async(model=g4f.models.claude_v2,
                                                   messages=[{"role": "user", "content": f"{message}"}])
        return response
    except Exception as e:
        return f"Something went wrong while generating text. Error: {e}"


async def phinder(message: str) -> str:
    try:
        response = g4f.ChatCompletion.create_async(model=g4f.models.default, provider=g4f.Provider.Phind,
                                                   messages=[{"role": "user", "content": f"{message}"}])
        return response
    except Exception as e:
        return f"Something went wrong while generating text. Error: {e}"


# ########################### NGC cloud

async def baseNgc(message, func, payload: Dict):
    client = AsyncClient(headers={
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Accept": "application/json",
    })
    base_url = 'https://api.nvcf.nvidia.com/v2/nvcf/pexec/'
    func_url = base_url + 'functions/' + func
    fetch_url = f"{base_url}/status/"
    resp = await client.post(func_url, json=payload)
    while resp.status_code == 202:
        req_id = resp.headers.get("NVCF-REQID")
        fetch__url = fetch_url + req_id
        resp = await client.get(fetch__url)
    resp.raise_for_status()
    return resp.json()  # response['choices'][0]['message']['content']


async def codeLLM(message: str) -> str:
    resp = await baseNgc(message=message, func='2ae529dc-f728-4a46-9b8d-2697213666d8', payload={
        "messages": [
            {
                "content": f"{message}",
                "role": "user"
            }
        ],
        "temperature": 0.7,
        "top_p": 1,
        "max_tokens": 1024,
        "seed": 42,
        "stream": False
    })
    return resp['choices'][0]['message']['content']


async def starCoder(message: str) -> str:
    resp = await baseNgc(message=message, func='6acada03-fe2f-4e4d-9e0a-e711b9fd1b59', payload={
        "prompt": f"{message}",
        "temperature": 0.7,
        "top_p": 0.7,
        "max_tokens": 1024,
        "seed": 42,
        "bad": None,
        "stop": None,
        "stream": False
    })
    return resp['choices'][0]['text']
