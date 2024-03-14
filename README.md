# Google Reviews Analyzer: Find your place

Analyzes Google reviews using NLP and Generative AI 🫣

To get Google review data
go to [this repo](https://github.com/eliagonzalezmolina/google-maps-reviews-scraper).

## Configurations ⚙️
- Create a file `.env` and fill environmental variables from `.env.template`
- Make these initial installations:

```bash
make install
make pre-commits-init
make dvc-init
```

## Development 🤓
- Before starting, do `dvc push` to get most recent data
- Make sure that you `dvc add` and `dvc push` your data files
- Before commiting code, it's recommendable to run `make pre-commit` to ensure code
style (however, it is done automatically when commiting code)
