"""
Вспомогательные функции для загрузки и предобработки данных.

Этот файл нужен, чтобы:
- соответствовать структуре проекта (src/preprocessing.py);
- отделить предобработку от ноутбука.

"# TODO: добавить более сложные методы обработки выбросов и масштабирование признаков"

import pandas as pd

def load_raw_data(path: str = "data/raw/data.csv") -> pd.DataFrame:
    """
    Загружает сырые данные из CSV.
    По умолчанию берёт файл data/raw/data.csv.
    """
    return pd.read_csv(path)


def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Простая предобработка:
    - копия датафрейма;
    - удаление дубликатов;
    - заполнение пропусков в числовых столбцах медианой;
    - заполнение пропусков в категориальных столбцах значением 'Unknown'.
    """
    df_clean = df.copy()

    # Удаляем дубликаты
    df_clean = df_clean.drop_duplicates()

    # Числовые признаки
    num_cols = df_clean.select_dtypes(include="number").columns
    df_clean[num_cols] = df_clean[num_cols].fillna(df_clean[num_cols].median())

    # Категориальные признаки
    cat_cols = df_clean.select_dtypes(include="object").columns
    df_clean[cat_cols] = df_clean[cat_cols].fillna("Unknown")

    return df_clean

