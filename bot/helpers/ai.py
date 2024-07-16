import os
import re

import google.generativeai as genai
from httpx import AsyncClient
from openai import OpenAI

from bot.config import PALM_API_KEY, CF_API_KEY, NVIDIA_API_KEY, OPENAI_API_KEY
from bot.helpers.functions import random_string


async def openai_helper(message: str, model: str = "gpt-4-turbo", *args) -> str:
    client = OpenAI(api_key=OPENAI_API_KEY, timeout=60)

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
            model=model,
            prompt=message,
            size="1024x1024",
            quality="hd",
            n=1,
        )
        client_ = AsyncClient()
        image = await client_.get(response.data[0].url)
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
    return await cf(message, "@cf/meta/meta-ai", types="gen")


async def stableDiffusion(message: str) -> str:
    return await cf(message, "@cf/stabilityai/stable-diffusion-xl-base-1.0", types="img")


async def dreamShaper(message: str) -> str:
    return await cf(message, "@cf/lykon/dreamshaper-8-lcm", types="bin")


async def stableDiffusionIn(message: str) -> str:
    return await cf(message, "@cf/bytedance/stable-diffusion-xl-lightning", types="bin")


# ########################### NGC cloud
async def openai_ngc(message: str, model: str) -> str:
    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=f"{NVIDIA_API_KEY}"
    )

    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": f"{message}"}],
        temperature=0.75,
        top_p=0.7,
        max_tokens=1024,
        stream=False
    )
    return completion.choices[0].message.content


async def mistral(message: str) -> str:
    return await openai_ngc(message, "mistralai/mistral-large")


async def llama(message: str) -> str:
    return await openai_ngc(message, "meta/llama3-70b-instruct")


async def codellama_ngc(message: str) -> str:
    return await openai_ngc(message, "meta/codellama-70b")


async def codestral_ngc(message: str) -> str:
    return await openai_ngc(message, "mistralai/codestral-22b-instruct-v0.1")


async def granite_ngc(message: str) -> str:
    return await openai_ngc(message, "ibm/granite-34b-code-instruct")


async def snowflake_ngc(message: str) -> str:
    return await openai_ngc(message, "snowflake/arctic")


async def nemotron_ngc(message: str) -> str:
    return await openai_ngc(message, "nvidia/nemotron-4-340b-instruct")


async def mixtral_ngc(message: str) -> str:
    return await openai_ngc(message, "mistralai/mixtral-8x22b-instruct-v0.1")
