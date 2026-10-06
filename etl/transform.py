import pandas as pd
import numpy as np

def transform_data(leads_df, deals_df):
    print("Transformation process started.")
    
    df_final = pd.merge(leads_df, deals_df, on='mql_id', how='left')
    
    useful_columns = [
        'mql_id', 'first_contact_date', 'origin', 'sr_id', 
        'won_date', 'business_segment', 'declared_monthly_revenue'
    ]
    df_final = df_final[useful_columns].copy()

    df_final.columns = [
        'Lead_ID', 'Fecha_Recepcion', 'Proveedor_Lead', 'ID_Vendedor', 
        'Fecha_Venta', 'Segmento_Negocio', 'Ingreso_Generado'
    ]

    # Crear el Estado del Lead (Si tiene Fecha de Venta, es 'Vendido', sino 'Perdido')
    df_final['Estado_Final'] = np.where(df_final['Fecha_Venta'].notna(), 'Vendido', 'Perdido')

    # Limpiar Nulos: Reemplazar valores vacíos en Vendedor para los que no cruzaron
    df_final['ID_Vendedor'] = df_final['ID_Vendedor'].fillna('Sin Asignar')
    df_final['Proveedor_Lead'] = df_final['Proveedor_Lead'].fillna('Desconocido')
    df_final['Ingreso_Generado'] = df_final['Ingreso_Generado'].fillna(0)

    # Simular 'Minutos_Respuesta' (Speed-to-Dial)
    # Usamos una distribución exponencial para que la mayoría se contacte rápido y unos pocos tarden mucho
    np.random.seed(42) # Para que los datos sean consistentes en cada ejecución
    df_final['Minutos_Respuesta'] = np.random.exponential(scale=45, size=len(df_final)).astype(int)

    # Simular el 'Costo_Lead' basado en el Proveedor (origin)
    costos = {
        'organic_search': 0, 
        'paid_search': 15, 
        'social': 10, 
        'direct_traffic': 5,
        'email': 8
    }
    df_final['Costo_Lead'] = df_final['Proveedor_Lead'].map(costos).fillna(12) # 12 por defecto para los demás

    df_final['Fecha_Recepcion'] = df_final['Fecha_Recepcion'].astype(str)
    df_final['Fecha_Venta'] = df_final['Fecha_Venta'].astype(str)

    print("Datos transformados. Total de filas:", len(df_final))
    return df_final