# notebooks

Exploratory data analysis, visualisation, and experiment notebooks. These are for research exploration — production code belongs in `src/`.

## Structure

```
notebooks/
├── Italian_dataset/   # EDA and baseline experiments on the Italian dataset (Member 1)
└── MDVRKCL/           # EDA and baseline experiments on the MDVR-KCL dataset (Member 2)
```

## Conventions

- Each notebook must have a descriptive title cell at the top.
- Strip outputs before committing: `nbstripout --install` (once per repo clone).
- Notebook naming: `{NNN}_{descriptive_title}.ipynb` (e.g. `001_italian_eda.ipynb`).
- Do not import from other notebooks — factor shared code into `src/` modules.
- Mark experimental notebooks with the `exp/` branch prefix (see CONTRIBUTING.md).
