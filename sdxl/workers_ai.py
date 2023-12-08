import io
import os

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
        if negative_prompt != '':
            log.warning(
                'Negative prompt is currently not supported and will be ignored.')
        if guidance_scale != 7.5:
            log.warning(
                'Guidance scale is currently not supported and will be ignored.')
        if width != 1024 or height != 1024:
            log.warning(
                'Width and height are currently not supported and will be ignored.')

        payload = {
            'prompt': prompt,
            'num_steps': num_inference_steps
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}',
        }

        response = await self.client.post(self.base_url, json=payload, headers=headers)

        if response.status_code != 200:
            log.error(f"Error generating image: {response.text}")
            raise Exception(f"Error generating image: {response.text}")

        # this returns a png
        image = io.BytesIO(response.content)
        image.seek(0)
        return image
