import pandas as pd

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.tables = {}

    def create_table(self, table_name, headers):
        self.tables[table_name] = pd.DataFrame(columns=headers)

    def insert_data(self, table_name, data_dict):
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist in the database. Create the table first.")
        new_row = pd.DataFrame(data_dict, index=[0])
        self.tables[table_name] = pd.concat([self.tables[table_name], new_row], ignore_index=True)
        print(f"Data inserted into '{table_name}' table.")

    def get_last_row(self, table_name):
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist in the database.")
        last_row = self.tables[table_name].iloc[-1]
        return last_row

    def show_tables(self):
        print("Tables in the database:")
        for table_name, df in self.tables.items():
            print(f"Table: {table_name}")
            print(df)