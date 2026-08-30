import sys
from pathlib import Path

# So test files can `import utils` / `from spawn_batch import ...` without
# path boilerplate in each one.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
