# Linguistics Corpus

A growing collection of linguistic data from languages of Tanzania, collected for morphological and other linguistic analysis.

## Datasets

| File | Language | Description |
|---|---|---|
| Matengo_sentences.tsv | Matengo (Kimatengo) | Words and sentences elicited from a native speaker |

More datasets will be added over time.

## Matengo_sentences.tsv

- *Language:* Matengo (Bantu), spoken in the Mbinga area, Tanzania
- *Speaker:* father of the collector
- *Elicitation:* Swahili prompts translated into Matengo by the speaker
- *Format:* tab-separated (TSV), UTF-8

| Column | Description |
|---|---|
| id | Entry number |
| matengo_sentence | Matengo form given by the speaker |
| gloss | Morpheme-by-morpheme gloss (Leipzig Glossing Rules) |
| translation_sw | Swahili prompt |
| translation_en | English translation |
| speaker | Who provided the data |
| notes | Comments, e.g. observed allomorphy |

## Conventions

- One file per language or dataset
- Tab-separated, UTF-8 encoding
- Glosses follow the Leipzig Glossing Rules

## Status

Work in progress. Some gloss fields are still empty, and more data will be added.
