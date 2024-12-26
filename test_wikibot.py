from mylib.bot import scrape
from click.testing import CliRunner
from wikibot import cli


def test_scrape():
    assert "Carlos Sainz" in scrape("Carlos Sainz Jr.")


def test_wikibot():
    runner = CliRunner()
    result = runner.invoke(cli, ["--name", "Microsoft"])
    assert result.exit_code == 0
    assert "Microsoft" in result.output
