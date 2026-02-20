import os
from azure.cosmos import CosmosClient
from dotenv import load_dotenv


class DatabaseService:

    def __init__(self):
        load_dotenv()

        endpoint = os.getenv("COSMOS_ENDPOINT")
        key = os.getenv("COSMOS_KEY")
        database_name = os.getenv("COSMOS_DB")
        container_name = os.getenv("COSMOS_CONTAINER")

        self.client = CosmosClient(endpoint, key)
        self.database = self.client.get_database_client(database_name)
        self.container = self.database.get_container_client(container_name)

    def create_entry(self, entry: dict):
        return self.container.create_item(body=entry)

    def get_all_entries(self):
        query = "SELECT * FROM c"
        items = list(self.container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))
        return items

    def get_entry_by_id(self, entry_id: str):
        try:
            return self.container.read_item(item=entry_id, partition_key=entry_id)
        except Exception:
            return None
