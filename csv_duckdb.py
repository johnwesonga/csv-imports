import duckdb
import click

CSV_FILE =  'bigmac.csv'


@click.command()
@click.option('--csv_filename', prompt='Name of CSV file',)
def import_csv(csv_filename):
    """Simple script that imports CSV to DuckDB, creates table and prints out the schema""" 
    conn = duckdb.connect()
    rel = duckdb.from_csv_auto(csv_filename)
    # print(rel)
    rcount = conn.execute("""SELECT COUNT(*) FROM %s""" %(csv_filename)).fetchall()
    print(rcount)
    #  tbl = conn.execute(f"CREATE TABLE {csv_filename[:-4]} AS {rel};")
    tbl = conn.execute(f"CREATE TABLE {csv_filename[:-4]} AS SELECT * FROM read_csv_auto({csv_filename});")
    conn.commit() 
    print(f"Table {csv_filename[:-4]} created successfully.")
    schema = conn.execute(f"DESCRIBE {csv_filename[:-4]};").fetchall()
    print(schema)


if __name__ == '__main__':
    import_csv()




