"""Shared embedding settings for indexing and retrieval."""

from pathlib import Path
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data/samples/public_regulations"
STORAGE_DIR = ROOT / "storage/miv_pilot_e5_small"
MODEL_CACHE = ROOT / "storage/models"
MODEL_NAME = "intfloat/multilingual-e5-small"


def create_embedding():
    return HuggingFaceEmbedding(
        model_name=MODEL_NAME, device="cpu", cache_folder=str(MODEL_CACHE),
        query_instruction="query: ", text_instruction="passage: ",
        normalize=True, embed_batch_size=8,
    )
