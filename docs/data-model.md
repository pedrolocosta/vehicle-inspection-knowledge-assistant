# Requirement record specification

The future inventory should keep each technical assertion tied to its evidence and review history. The following is a **schema proposal**, not a populated or approved copy of the working Google Sheet.

| Field | Meaning |
| --- | --- |
| `requirement_id` | Stable identifier independent of row number |
| `topic` | Inspection topic, such as GNV |
| `source_type` | Regulation, official guidance, PT, IT, or other controlled source |
| `issuing_body` / `source_title` | Origin and exact source title |
| `source_identifier` / `source_version` | Number, revision, and amendment chain |
| `source_location` | Article, item, page, table, or internal section |
| `published_at` / `effective_from` / `effective_until` | Distinct time boundaries, when known |
| `vehicle_type` / `service_type` | Applicability conditions |
| `requirement_text` | Controlled excerpt or internal paraphrase with rights checked |
| `interpretation` | RT-reviewed operational meaning, kept separate from source text |
| `evidence_method` | How the inspector documents the finding |
| `outcome_logic` | Applicable outcome and exceptions, only after approval |
| `related_sources` | Overrides, dependencies, and cross references |
| `review_status` | `draft`, `pending_rt`, `approved`, `rejected`, or `superseded` |
| `reviewer` / `reviewed_at` | Accountable review and date |
| `content_hash` / `last_checked_at` | Detect changes and document freshness checks |

## Example of safe public metadata

```json
{
  "requirement_id": "DEMO-GNV-001",
  "topic": "GNV",
  "source_type": "candidate_regulation",
  "source_title": "Portaria Inmetro nº 147/2022",
  "source_location": null,
  "review_status": "pending_rt",
  "requirement_text": null,
  "interpretation": null,
  "outcome_logic": null,
  "note": "Illustrative metadata only; current source status and applicability need verification."
}
```

Do not infer inspection criteria from a source title. No `pending_rt` record can be used to issue an operational answer.
