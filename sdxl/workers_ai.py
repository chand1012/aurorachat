import io
import os
import asyncio
import base64

from loguru import logger as log
import httpx


class WorkersSDAPIAsync:
    def __init__(self, account_id: str | None = None, api_key: str | None = None, api_email: str | None = None, model_name='@cf/stabilityai/stable-diffusion-xl-base-1.0'):
        if account_id is None:
            account_id = os.getenv('CLOUDFLARE_ACCOUNT_ID')
        if api_key is None:
            api_key = os.getenv('CLOUDFLARE_API_KEY')
        if api_email is None:
            api_email = os.getenv('CLOUDFLARE_API_EMAIL')
        self.base_url = f'https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{model_name}'
        self.api_key = api_key
        self.client = httpx.AsyncClient(timeout=None)
        self.api_email = api_email

    async def generate_image(self, prompt: str, negative_prompt: str = '', guidance_scale: float = 7.5, height: int = 1024,
                             num_inference_steps: int = 20, width: int = 1024) -> io.BytesIO:
        if num_inference_steps > 20:
            log.warning(
                f"Greater than 20 inference steps is not supported. Setting to 20.")
            num_inference_steps = 20
        if guidance_scale != 7.5:
            log.warning(
                'Guidance scale is currently not supported and will be ignored.')
        if width > 2048 or height >= 2048:
            log.warning(
                'Width and height greater than 2048 are not supported. Setting to 1024.')
            width = 2048
            height = 2048

        payload = {
            'prompt': prompt,
            'num_steps': num_inference_steps
        }

        if negative_prompt:
            payload['negative_prompt'] = negative_prompt

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}',
        }

        response = await self.client.post(self.base_url, json=payload, headers=headers)

        if response.status_code != 200:
            log.error(f"Error generating image: {response.text}")
            raise Exception(f"Error generating image: {response.text}")

        # if flux is in the model name, the response is base 64 encoded and needs to be decoded
        if 'flux' in self.base_url:
            image = io.BytesIO(base64.b64decode(response.json()['result']['image']))
            image.seek(0)
            return image

        # this returns a png
        image = io.BytesIO(response.content)
        image.seek(0)
        return image
    
async def testing():
    from dotenv import load_dotenv
    load_dotenv()
    workers = WorkersSDAPIAsync(model_name='@cf/bytedance/stable-diffusion-xl-lightning')
    image = await workers.generate_image("A cat in a field of flowers.", num_inference_steps=4)
    with open("cat.png", "wb") as f:
        f.write(image.read())


if __name__=="__main__":
    asyncio.run(testing())
