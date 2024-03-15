# Google Reviews Analyzer: Find your place

Analyzes Google reviews using NLP and Generative AI 🫣

To get Google review data
go to [this repo](https://github.com/eliagonzalezmolina/google-maps-reviews-scraper).

## Configurations ⚙️
- Create a file `.env` and fill environmental variables from `.env.template`
- Make these initial installations:

```bash
make install
make pre-commit-init
make dvc-init
```

## Usage 🚀
### Open-ai place summary
Generate a summary with pros&cons of a place given its reviews.

1- Fill `params.yaml` (section `openai_place_summary`)

2- Run `google_reviews_analyzer/openai_place_summary/main.py`

## Development 🤓
- Before starting, do `dvc push` to get most recent data
- Make sure that you `dvc add` and `dvc push` your data files
- Before commiting code, it's recommendable to run `make pre-commit` to ensure code
style (however, it is done automatically when commiting code)
