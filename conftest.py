import sys
import os
from pathlib import Path

# Добавляем корень проекта в sys.path
root = Path(__file__).parent
sys.path.insert(0, str(root))
sys.path.insert(0, str(root / 'blogicum'))

# Явно указываем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')
