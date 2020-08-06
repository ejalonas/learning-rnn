from pathlib import Path

repo_dir = Path(__file__).parent.parent.resolve()

# Local repo dirs
raw_data_cache = repo_dir / 'data' / 'raw'
interim_data_cache = repo_dir / 'data' / 'interim'
processed_data_cache = repo_dir / 'data' / 'processed'
figure_cache = repo_dir / 'reports' / 'figures'
model_cache = repo_dir / 'models'
report_cache = repo_dir / 'reports'