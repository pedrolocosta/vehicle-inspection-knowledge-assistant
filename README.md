# Vehicle Inspection Knowledge Assistant

**An AI engineering portfolio project for traceable answers in a regulated vehicle inspection workflow.**

**Repository description:** An AI/ML portfolio project for Brazilian vehicle inspection, connecting regulatory monitoring, vehicle technical data, the Pedro assistant, and educational content through traceable sources and human review.

**Language policy:** Engineering documentation for recruiters and collaborators is written in American English. Pedro's client-facing responses, Brazilian normative content, and technical interpretations remain in Brazilian Portuguese.

Brazilian vehicle inspection requirements are distributed across regulations, technical procedures, and operational documents. A useful assistant must identify the applicable source and its version, retain a traceable path from requirement to answer, and recognize when technical review is still pending. This project explores that workflow through a GNV (compressed natural gas) pilot and an assistant concept named **Pedro**.

## Project workstreams

| Workstream | Goal | Public repository status |
| --- | --- | --- |
| Regulatory monitoring | Track source versions, amendments, and effective dates | Governance approach documented; no automated feed here |
| Vehicle technical data | Organize vehicle specifications with provenance and freshness checks | Planned; no vehicle database published here |
| Pedro assistant | Answer inspection questions with reviewed evidence and escalation | Deterministic abstention demo; no production assistant |
| Educational content | Explain inspection topics to Brazilian audiences | Planned; no video production pipeline in this starter |

The **GNV pilot** is the first bounded use case. These workstreams describe the intended project, while the table below identifies what this repository actually implements.

> **Current status:** Portfolio starter and governance prototype. The last status snapshot available to this public demo, dated September 22, 2026, reported 12 structured `MVP_GNV` requirements pending Responsible Technical Engineer (RT) validation. The controlled inventory may have changed since then. This repository does not publish or endorse their technical content. It is not an operational inspection tool.

## What is in this repository

| Component | Purpose | Status |
| --- | --- | --- |
| [Architecture](docs/architecture.md) | Source-to-answer flow and review gates | Proposed design |
| [Data model](docs/data-model.md) | Traceability fields for future verified requirements | Specification |
| [Source governance](docs/source-governance.md) | Version control, permissions, and RT approval | Draft process |
| [Evaluation plan](docs/evaluation.md) | Cases, metrics, and release criteria | Starter suite |
| [Demo CLI](src/assistant.py) | Shows how unvalidated material is blocked | Working, deterministic demonstration |

The demo contains **synthetic metadata and process guidance only**. It contains no published regulatory acceptance criteria, copied standards, company PTs/ITs, customer records, or production model integration.

## Try the governance demo

Python 3.10+ is sufficient; no dependencies or API keys are needed.

```bash
python -m src.assistant "Qual é o estado de validação do MVP?"
python -m src.assistant "Qual critério de inspeção de GNV devo aplicar?"
python -m unittest discover -s tests -v
```

The first question returns a Portuguese project-status message with provenance. The second returns a Portuguese refusal because the demo has no RT-approved technical requirement. The test suite checks this behavior; it does **not** measure the accuracy of regulatory answers.

## Proposed engineering path

1. Verify source identity, current version, effective dates, and permitted use.
2. Normalize requirements into individually traceable records with applicability and evidence pointers.
3. Obtain documented RT review for each record before it can support an operational answer.
4. Add retrieval with source and version filtering, followed by answer generation with precise references.
5. Evaluate applicability, citations, conflict handling, abstention, and source freshness against reviewed cases.
6. Pilot internally with an explicit escalation route and review change logs before broader use.

See [roadmap](docs/roadmap.md) for deliverables and evidence to add at each milestone. **RAG, an LLM, and a production assistant have not been implemented in this starter.**

## Why this matters to US engineering teams

The Brazilian domain is the test bed; the engineering patterns are transferable: document provenance, temporal validity, human approval gates, retrieval evaluation, and safe abstention in a regulated workflow. Portuguese titles and terms such as *GNV*, *Portaria*, *PT*, *IT*, and *Responsável Técnico (RT)* are retained. Portfolio explanations and code documentation use American English. The product's user-visible text, normative excerpts, and interpretations use Brazilian Portuguese.

## Publication boundaries

The master inventory and all original source files remain outside this public starter. Do not add private communications, company procedures, internal PTs/ITs, unlicensed scans of standards, customer or vehicle data, employee information, or presenter photos. Publicly available documents may be linked, but reproduction rights must be checked before copying them. See [publication checklist](docs/publication-checklist.md).

## Author and scope

Created as a portfolio demonstration by **Pedro Costa**, a mechanical engineer and technical lead in Brazilian vehicle inspection, transitioning into AI/ML engineering. This description reflects the project brief; source verification and technical review are tracked separately.

- GitHub: [pedrolocosta](https://github.com/pedrolocosta)
- LinkedIn: [pedrolocosta](https://www.linkedin.com/in/pedrolocosta/)

No open-source license has been selected. The public repository showcases this prototype; it does not grant reuse rights beyond those provided by applicable law.
