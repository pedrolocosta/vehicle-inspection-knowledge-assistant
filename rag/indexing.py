from pathlib import Path
from dotenv import load_dotenv

from llama_index.core import(
    simpleDirectoryReader,
    VectorStoreIndex,
)
from llama_index.embeddings.openai import OpenAIEmbedding

load_dotenv()

DATA_DIR = Path("data/samples/public_regulations")
STORAGE_DIR = Path("storage/miv_pilot")

documents = SimpleDirectoryReader(
    input_dir=str(DATA_DIR),
    required_exts=[".pdf"],
).load_data()

if not documents:
    raise ValueError("Nenhum PDF encontrado.")

embedding = OpenAIEmbedding(
    model="text-embedding-3-small"
)

index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embedding,
    show_progress=True,
)

index.storage_context.persist(
    persist_dir=str(STORAGE_DIR)
)

print(f"Documentos carregados: {len(documents)}")
print("Índice RAG salvo com sucesso.")
