import httpx


class AthenaDB:
    def __init__(self, base_url: str, namespace: str | None = None):
        self.base_url = base_url
        self.namespace = namespace
        self.client = httpx.AsyncClient()

    async def insert(self, input: str | None = None, inputs: list[str] = [], namespace=None):
        namespace = namespace or self.namespace
        if not namespace:
            raise ValueError("Namespace must be provided.")
        url = f"{self.base_url}/{namespace}/insert"
        text_data = {'input': input} if input is not None else {
            'inputs': inputs}
        response = await self.client.post(url, json=text_data)
        response.raise_for_status()
        return response.json()

    async def query(self, input: str | None = None, inputs: list[str] = [], namespace: str | None = None, limit: int = 5, vector: bool = False, db_id: bool = False):
        namespace = namespace or self.namespace
        if not namespace:
            raise ValueError("Namespace must be provided.")
        url = f"{self.base_url}/{namespace}/query?limit={min(limit, 20)}"
        if vector:
            url += "&vector=true"
        if db_id:
            url += "&db_id=true"
        query_data = {'input': input} if input is not None else {
            'inputs': inputs}
        response = await self.client.post(url, json=query_data)
        response.raise_for_status()
        return response.json()

    async def get_by_id(self, uuid: str, namespace: str | None = None, vector: bool = False, db_id: bool = False):
        namespace = namespace or self.namespace
        if not namespace:
            raise ValueError("Namespace must be provided.")
        url = f"{self.base_url}/{namespace}/{uuid}"
        if vector:
            url += "?vector=true"
        if db_id:
            url += "?db_id=true"
        response = await self.client.get(url)
        response.raise_for_status()
        return response.json()

    async def get(self, limit=10, offset=0, namespace: str | None = None, vector: bool = False, db_id: bool = False):
        namespace = namespace or self.namespace
        if not namespace:
            raise ValueError("Namespace must be provided.")
        url = f"{self.base_url}/{namespace}?limit={limit}&offset={offset}"
        if vector:
            url += "&vector=true"
        if db_id:
            url += "&db_id=true"
        response = await self.client.get(url)
        response.raise_for_status()
        return response.json()

    async def delete(self, uuid: str, namespace: str | None = None):
        namespace = namespace or self.namespace
        if not namespace:
            raise ValueError("Namespace must be provided.")
        url = f"{self.base_url}/{namespace}/{uuid}"
        response = await self.client.delete(url)
        response.raise_for_status()
        return response.status_code

    async def generate_embeddings(self, text: str):
        url = f"{self.base_url}/embeddings"
        response = await self.client.post(url, json={'text': text})
        response.raise_for_status()
        return response.json()

    async def test_endpoint(self):
        url = f"{self.base_url}/test"
        response = await self.client.get(url)
        response.raise_for_status()
        return response.text

    async def close(self):
        await self.client.aclose()
