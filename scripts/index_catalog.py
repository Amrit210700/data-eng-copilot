"""Day 14 entrypoint: index the metadata catalog into Chroma.

Usage: python scripts/index_catalog.py
"""

from app.config import settings
from app.retrieval.catalog_indexer import index_catalog

if __name__ == "__main__":
    index_catalog(catalog_dir="data/catalog", persist_dir=settings.chroma_persist_dir)
