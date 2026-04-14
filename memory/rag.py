from memory.vector_store import search_vectors


async def retrieve_context(query: str):
    """
    RAG retrieval entrypoint
    """
    return search_vectors(query)
