from etl.extraction import extract_data
from etl.transform import transform_data
from etl.loading import load_data

def run_etl_pipeline():
    # Extraction
    leads_df, deals_df = extract_data()
    
    # Transformation
    df_final = transform_data(leads_df, deals_df)
    
    # Loading
    load_data(df_final)

if __name__ == "__main__":
    run_etl_pipeline()