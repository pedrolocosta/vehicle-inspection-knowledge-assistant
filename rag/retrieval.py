"""Retrieve source passages without invoking a language model."""

import argparse
from llama_index.core import StorageContext, load_index_from_storage
from rag.local import STORAGE_DIR, create_embedding


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("question", nargs="?", help="Pergunta tecnica")
    args = parser.parse_args()
    if not (STORAGE_DIR / "index_store.json").is_file():
        raise SystemExit("Crie o indice primeiro: python -m rag.indexing")
    question = args.question or input("Pergunta tecnica: ")
    if not question.strip():
        raise SystemExit("Digite uma pergunta para buscar trechos.")
    index = load_index_from_storage(
        StorageContext.from_defaults(persist_dir=str(STORAGE_DIR)),
        embed_model=create_embedding(),
    )
    results = index.as_retriever(similarity_top_k=3).retrieve(question)
    for number, result in enumerate(results, start=1):
        print(f"\n--- RESULTADO {number} ---")
        print("Score de similaridade (nao e confianca):", result.score)
        print("Arquivo:", result.node.metadata.get("file_name", "indisponivel"))
        print("Pagina:", result.node.metadata.get("page_label", "indisponivel"))
        print(result.node.get_content())
    print("\nTrechos experimentais; vigencia e aplicabilidade nao foram validadas pelo RT.")


if __name__ == "__main__":
    main()
