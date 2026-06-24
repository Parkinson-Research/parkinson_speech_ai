# data/raw/future_dataset

Placeholder directory for future datasets.

## Adding a New Dataset

1. Create a subdirectory in `data/raw/` with the dataset name:
   ```bash
   mkdir data/raw/my_new_dataset
   ```

2. Place your raw audio files inside following the standard structure:
   ```
   data/raw/my_new_dataset/
   ├── PD/{subject_id}/*.wav
   └── HC/{subject_id}/*.wav
   ```

3. Add a `README.md` in the new directory documenting the dataset.

4. Register the dataset in `configs/dataset.yaml`.

5. Track with DVC:
   ```bash
   dvc add data/raw/my_new_dataset
   git add data/raw/my_new_dataset.dvc .gitignore
   git commit -m "data(new-dataset): add raw recordings"
   dvc push
   ```

6. Implement a dataset class in `src/datasets/` inheriting from `BaseAudioDataset`.

7. Document in `docs/datasets.md`.
