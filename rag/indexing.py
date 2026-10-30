"""Build the local pilot index from public PDFs."""

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from transformers import AutoTokenizer

from rag.local import DATA_DIR, MODEL_NAME, MODEL_CACHE, STORAGE_DIR, create_embedding


def main():
    pdfs = sorted(DATA_DIR.glob("*.[pP][dD][fF]"))
    if not pdfs:
        raise SystemExit(f"Coloque um PDF publico em: {DATA_DIR}")
    documents = SimpleDirectoryReader(
        input_files=[str(path) for path in pdfs], raise_on_error=True,
    ).load_data()
    documents = [doc for doc in documents if doc.text.strip()]
    if not documents:
        raise SystemExit("Nenhum texto extraido. Use um PDF com texto selecionavel.")

    embedding = create_embedding()
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, cache_dir=str(MODEL_CACHE))
    splitter = SentenceSplitter(
        chunk_size=384, chunk_overlap=64,
        tokenizer=lambda text: tokenizer.encode(
            text, add_special_tokens=False, verbose=False,
        ),
    )
    index = VectorStoreIndex.from_documents(
        documents, embed_model=embedding, transformations=[splitter],
        show_progress=True,
    )
    index.storage_context.persist(persist_dir=str(STORAGE_DIR))
    print(f"PDFs carregados: {len(pdfs)}")
    print(f"Paginas com texto: {len(documents)}")
    print(f"Indice local salvo em: {STORAGE_DIR}")


if __name__ == "__main__":
    main()
