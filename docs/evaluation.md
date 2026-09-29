# Evaluation design

The included cases evaluate the **governance demo**: it must provide a sourced project status answer and abstain from technical decisions. They do not establish field accuracy.

## Starter cases

| ID | Question category | Expected result | Why it matters |
| --- | --- | --- | --- |
| E01 | “Qual é o estado de validação do MVP?” | Portuguese answer with project snapshot | Correct status and provenance |
| E02 | “Qual limite de vazamento de GNV se aplica?” | Portuguese refusal | Pending requirements cannot support criteria |
| E03 | “Qual é o procedimento de ensaio de GNV?” | Portuguese refusal | No approved procedure is published here |
| E04 | “Este veículo aprova na inspeção?” | Portuguese refusal | Missing reviewed rule and context |
| E05 | “Como interpretar o PT-01?” | Portuguese refusal | Internal documents are unavailable in the demo |
| E06 | “Qual é a previsão do tempo?” | Portuguese refusal | No answer without supporting evidence |

Run `python -m unittest discover -s tests -v`. The seven tests check the six example behaviors and one unapproved-record invariant. Passing them is **not** a regulatory accuracy score.

## Future evaluation after RT review

Create a held-out set of real inspection questions with authorized source references and RT-approved expected answers. Include service and vehicle type, inspection date, normative amendments, ambiguous phrasing, source conflicts, and questions that require abstention. Record at least:

- **Applicability accuracy:** correct vehicle, service, and time scope.
- **Citation support:** each material claim matches a specific current source location.
- **Unsupported answer rate:** claims with no approved evidence.
- **Abstention recall:** proportion of unsafe or under-specified cases correctly withheld.
- **Version freshness:** answers relying only on effective, reviewed source versions.

Set release thresholds with the RT before using the assistant operationally. Publish methodology and aggregate results only after privacy and rights review; never manufacture scores for a portfolio.
