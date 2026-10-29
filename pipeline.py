from src.data_loader import load_data
from src.analysis import
from src.charts import

def run_eda(name):
    data = load_data(name)
    print(data)

