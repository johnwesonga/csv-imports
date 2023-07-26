from csvs_to_sqlite import cli
import click


@click.command()
@click.option('--opt1', default=1)
@click.option('--opt2', default=2)
def test(opt1, opt2):
    print(opt1)
    print(opt2)

@click.command()
@click.pass_context
def dist(ctx):
    args = {"opt1":3, "opt2": 4}
    ctx.invoke(test, **args)

@click.command()
@click.pass_context
def convert_csv(ctx):
    args = {"paths":"bigmac.csv", "dbname": "bigmac.db"}
    ctx.invoke(cli.cli, **args)
    

def main(csv_path):
    convert_csv()
    
if __name__ == "__main__":
    main(csv_path = "bigmac.csv")
    


