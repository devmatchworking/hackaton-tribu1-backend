async def check_mongo_connection(client):
    try:
        await client.server_info()
        return True
    except Exception:
        return False