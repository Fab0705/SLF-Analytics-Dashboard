import pandas as pd

def extract_data():
    print("Extraction process started.")
    leads_df = pd.read_csv("data/olist_marketing_qualified_leads_dataset.csv")
    deals_df = pd.read_csv("data/olist_closed_deals_dataset.csv")
    return leads_df, deals_df