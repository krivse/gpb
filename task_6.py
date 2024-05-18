import requests
import pandas as pd
from pydantic import BaseModel
from datetime import datetime

data_json = {
    "Columns": ["key1", "key2", "key3"],
    "Description": "Банковское API каких-то важных документов",
    "RowCount": 2,
    "Rows": [
        ["value1", "value2", "value3"],
        ["value4", "value5", "value6"]
    ]
}


class APIResponse(BaseModel):
    """API response model."""
    Columns: list[str]
    Description: str
    RowCount: int
    Rows: list[list[str]]


class Document(BaseModel):
    """Document model."""
    document_id: int
    document_dt: datetime
    document_name: str
    load_dt: datetime = datetime.now()


def get_documents(url: str) -> pd.DataFrame:
    """Get data from API."""
    response = requests.get(url)
    data = response.json()
    # data = data_json
    response = APIResponse(**data)

    df = pd.DataFrame(
        response.Rows,
        columns=response.Columns
    )
    df = df.rename(columns={
        'key1': 'document_id',
        'key2': 'document_dt',
        'key3': 'document_name'
    })
    df = df.assign(load_dt=datetime.now())

    return df


if __name__ == '__main__':
    url_gpb = 'https://api.gazprombank.ru/very/important/docs?documents_date={"начало дня сегодня в виде таймстемп"}'
    result = get_documents(url_gpb)
    print(result)
