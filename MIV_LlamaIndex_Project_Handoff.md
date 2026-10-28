# MIV — LlamaIndex RAG: Project Handoff for VS Code

**Project:** Manual da Inspeção Veicular (MIV)  
**Repository:** https://github.com/pedrolocosta/vehicle-inspection-knowledge-assistant  
**Status:** Architecture agreed; initial local LlamaIndex setup is the next action.  
**Purpose of this file:** Portable project context and implementation instructions for continuing development in VS Code. This is a structured reconstruction of the conversation's decisions and instructions, **not a verbatim export of the ChatGPT conversation**.

## 1. Project vision

Build a technically traceable vehicle-inspection knowledge platform. Its first deliverable is a LlamaIndex-based document RAG for **Pedro**, the vehicle-inspection technical assistant. The knowledge platform will later support **Mike Ross**, a separate operational inspection agent, and eventually computer-vision-based inspection process analytics.

Long-term capabilities:

1. **Knowledge Intelligence (MIV):** technical standards, regulations, procedures, vehicle data, component knowledge, photo standards, document-validation rules.
2. **Operational Inspection Intelligence (Mike):** analyze individual inspection cases, work orders, client documents, FORM-TEC, inspection photos, MPI, nonconformities, and recordings.
3. **Process Intelligence (Analytics):** extract timestamped process events from real inspection videos, then calculate cycle times, wait times, bottlenecks, variability, rework, and other improvement KPIs.

**Architectural boundary:** MIV = what should be done and why; Mike = what occurred in an individual inspection; Analytics = what occurs systematically across the process.

## 2. Source-of-truth and data governance

- Google Drive MIV is the master repository of reusable technical knowledge.
- The **Inventário Mestre** is the source of truth for document identity, status, versions, provenance, applicability, and RT validation decisions.
- LlamaIndex is the ingestion/indexing/retrieval framework, **not** the normative authority or governance system.
- Do not assume the latest file is legally applicable: verify applicability, effective date, supersession, scope, and RT-approved interpretations.
- Always preserve source citations at the document and section/item level where possible.
- Do not put paid ABNT standards, internal proprietary documents, client data, `.env`, or private recordings in the public GitHub repository.
- Image retrieval and image model training are distinct: first build a governed multimodal reference collection; consider fine-tuning/classifiers only later if justified.

## 3. Agreed Google Drive logical architecture

```text
MIV DATA ARCHITECTURE/
├── 01_knowledge_sources/
│   ├── regulations_standards/            # INMETRO, CONTRAN, SENATRAN, ABNT, NIT-DIOS, etc.
│   └── document_knowledge_base/          # Document models, expected fields, validation rules
├── 02_visual_knowledge/
│   ├── image_knowledge_base/             # Individual components, variants, installations
│   └── inspection_photo_knowledge_base/  # Required photo views, framing, evidentiary criteria
├── 03_inspection_cases/                  # ONLY anonymized, validated reference cases in MIV
├── 04_learning_video_reference/          # Educational/reference videos ONLY
├── 05_derived_features_events/           # Planned event/feature schemas, not raw client video
├── 06_analytics_kpis/                    # KPI definitions and aggregate/de-identified outputs
├── 07_models_evaluation/                 # Evaluation datasets, model/version results
└── 08_governance_catalogs/               # Inventário Mestre
```

The preceding conversation reported these Drive operations as completed:

- `normas-regulamentacoes` renamed to `regulations_standards`, under `01_knowledge_sources`.
- `inventario-imagens` renamed to `image_knowledge_base`, under `02_visual_knowledge`.
- `Inventário Mestre - Manual da Inspeção Veicular` moved to `08_governance_catalogs`.
- `document_knowledge_base` created under `01_knowledge_sources`.
- `inspection_photo_knowledge_base` created under `02_visual_knowledge`.
- `04_video_process_data` renamed to `04_learning_video_reference`.

The user intended to move existing photo-standard examples from `image_knowledge_base` to `inspection_photo_knowledge_base`, and then add individual-component images to `image_knowledge_base`. **Do not assume those user-side moves were completed without checking.**

### Google Drive references

- Regulations and standards: https://drive.google.com/drive/folders/1JaNF7eDkq3Ug_nWcPG6Vt5Am6iw4LF-v
- Component image knowledge: https://drive.google.com/drive/folders/1c3GN9W8nBszjvzlpKZYn1qlV4ip2Ba55
- Photo standards: https://drive.google.com/drive/folders/1lfnGH16ceT-GxP4OyKIu36mMpnu3kUd-
- Document knowledge: https://drive.google.com/drive/folders/1-6UDLQ-QD0wkfGdpxDNdAn1Gwm90-SSI
- Learning/reference videos: https://drive.google.com/drive/folders/1wDLWKRV0UdX3-uVvvquekFoyAoaSkNML
- Inventário Mestre: https://docs.google.com/spreadsheets/d/1SXpaJVqiAPlR58iqEUKF53zUHUp3FIEmoGprjy-kYzo/edit

## 4. Mike Ross: separate operational storage

**Mike Ross** handles case-specific, potentially sensitive customer/inspection evidence. Its Drive should eventually follow this pattern:

```text
inspection_cases/
└── INSPECTION_ID/
    ├── 01_work_order/         # OS
    ├── 02_customer_documents/ # Customer-provided documents
    ├── 03_inspection_forms/   # FORM-TEC
    ├── 04_inspection_photos/  # MPI and other inspection images
    ├── 05_inspection_video/   # Actual inspection recordings
    ├── 06_findings/           # RNC, discrepancies, questions
    └── 07_decision/           # Results and evidence
```

Actual customer documents, photos and video belong to Mike, not to the MIV's general knowledge collection. MIV may contain anonymized/approved educational examples. Mike consumes the MIV RAG through a future API/tool rather than duplicating its normative database.

## 5. Knowledge relationships and metadata plan

Design stable identifiers and joins from the beginning:

`document_id`, `document_version_id`, `requirement_id`, `component_id`, `image_id`, `vehicle_id`, `inspection_id`, `video_id`, `event_id`.

Also plan: source type, issuer, original file ID/URL, revision, effective dates, current/obsolete status, scope/applicability, item/subitem, RT validation status, confidentiality/license, source hash, ingestion timestamp, and evidence citation.

**Important:** document-level metadata alone is not enough; requirements and excerpts should have their own traceable IDs. Authority is contextual to legal/normative competence, not merely a universal numerical ranking.

## 6. Proposed local repository layout

```text
vehicle-inspection-knowledge-assistant/
├── data/
│   └── samples/
│       └── public_regulations/    # Small local pilot dataset
├── rag/
│   ├── __init__.py
│   ├── ingestion.py
│   ├── metadata.py
│   ├── indexing.py
│   ├── retrieval.py
│   └── query.py
├── storage/                     # Local index persistence, not committed
├── tests/
│   └── rag/
├── .venv/                       # Local virtual environment, not committed
├── .env                         # Secrets, not committed
├── .gitignore
├── requirements.txt
└── README.md
```

The Drive's `image_knowledge_base` and `inspection_photo_knowledge_base` are conceptual inputs to future multimodal ingestion, not directories that need to be mirrored or committed to GitHub now.

## 7. Windows + VS Code: first setup

Prerequisites: Python 3.11 or 3.12, Git, VS Code, Microsoft Python extension. Use PowerShell in VS Code.

Clone only if repository is not already on the computer:

```powershell
git clone https://github.com/pedrolocosta/vehicle-inspection-knowledge-assistant.git
cd vehicle-inspection-knowledge-assistant
```

Create and activate a local virtual environment:

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install llama-index python-dotenv
python -c "import llama_index.core; print('LlamaIndex OK')"
```

If PowerShell activation is blocked, invoke `.\.venv\Scripts\python.exe` directly instead of changing the system's execution policy.

**Costs:** LlamaIndex is open source; hosted LLM/embedding APIs may incur separate charges. A ChatGPT subscription does not include OpenAI API credits. A local embedding option can be chosen before indexing if avoiding API charges.

### .gitignore safeguards

Check that these patterns, or equivalent protections, are present:

```gitignore
.env
.env.*
!.env.example
.venv/
storage/
data/samples/
licensed_standards/
**/licensed_standards/
__pycache__/
*.py[cod]
```

Do not blindly overwrite the repository's existing `.gitignore`; preserve its current exclusions, especially for ABNT standards and private materials.

## 8. Pilot indexing code (`rag/indexing.py`)

This is an educational prototype. It does **not** yet enforce norm validity, item-level citations, RT approvals, or incremental synchronization.

```python
from pathlib import Path
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
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

embedding = OpenAIEmbedding(model="text-embedding-3-small")
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embedding,
    show_progress=True,
)
index.storage_context.persist(persist_dir=str(STORAGE_DIR))
print(f"Documentos carregados: {len(documents)}")
print("Índice RAG salvo com sucesso.")
```

Place **one public, text-selectable PDF** in `data/samples/public_regulations/`. If using the OpenAI embedding service, place the secret only in `.env`:

```dotenv
OPENAI_API_KEY=your_key_here
```

Run:

```powershell
python -m rag.indexing
```

## 9. Pilot retrieval code (`rag/retrieval.py`)

```python
from dotenv import load_dotenv
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.openai import OpenAIEmbedding

load_dotenv()

embedding = OpenAIEmbedding(model="text-embedding-3-small")
storage_context = StorageContext.from_defaults(
    persist_dir="storage/miv_pilot"
)
index = load_index_from_storage(
    storage_context,
    embed_model=embedding,
)
retriever = index.as_retriever(similarity_top_k=3)

question = input("Pergunta técnica: ")
results = retriever.retrieve(question)

for number, result in enumerate(results, start=1):
    print(f"\n--- RESULTADO {number} ---")
    print("Score:", result.score)
    print("Origem:", result.node.metadata)
    print("Trecho:", result.node.get_content()[:1500])
```

Run:

```powershell
python -m rag.retrieval
```

**First success criterion:** retrieve the correct excerpt and source from the sample public PDF. Do not treat retrieved similarity as proof of normative correctness.

## 10. Implementation roadmap

- [ ] 1. Confirm Python, VS Code, Git, virtual environment, LlamaIndex import.
- [ ] 2. Create pilot folders and review `.gitignore`.
- [ ] 3. Ingest one public PDF and inspect retrieved chunks.
- [ ] 4. Define **MIV Metadata Schema v0.1** using actual Inventário Mestre fields.
- [ ] 5. Implement controlled ingestion, stable IDs, hashes, revision handling, and obsolete-document policies.
- [ ] 6. Implement metadata filtering, hybrid retrieval/reranking, and traceable citations.
- [ ] 7. Build a curated RT-reviewed test set with expected source sections and abstention tests.
- [ ] 8. Add controlled Google Drive synchronization.
- [ ] 9. Expose retrieval as a service/API consumed by Pedro and later Mike.
- [ ] 10. Add multimodal image/component/photo-standard relationships.
- [ ] 11. Later, connect Mike inspection videos to event extraction and process analytics with privacy and authorization controls.

## 11. Prompt for continuing in VS Code

> You are helping develop the Manual da Inspeção Veicular (MIV) knowledge platform in the repository `vehicle-inspection-knowledge-assistant`. Read `MIV_LlamaIndex_Project_Handoff.md` first and preserve its decisions. We are implementing a governed LlamaIndex RAG for Brazilian vehicle-inspection technical sources. The MIV is the reusable knowledge layer; Mike Ross is a separate operational agent for actual inspection cases; future analytics will derive process events from inspection videos. Never commit licensed ABNT standards, customer data, or secrets to the public repository. Start by checking the existing repository structure and Python environment; do not overwrite existing files without reviewing them. Guide me one small step at a time, explain what each command does, and validate each step before moving on. Respond in Portuguese unless I ask otherwise.

---

**Next action:** Open the repository in VS Code, place this file at its root, run the environment verification command, and continue from the first unchecked task.
