def ingest_csv(df):
  #some logic here
  return df

def ingest_json(df2):
  #some logic here
  return df2
def ingest_data(file_path, file_type):
    if file_type == 'csv':
        return ingest_csv(file_path)
    elif file_type == 'json':
        return ingest_json(file_path)
    else:
        raise ValueError("Unsupported file type: {}".format(file_type))

  
