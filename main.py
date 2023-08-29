from domain.repository_crawler_service import RepositoryCrawlerService
from domain.repository_model import Repository
from domain.repository_csv_service import RepositoryCsvService


if __name__ == '__main__':
    repo_csv = RepositoryCsvService()
    repo_csv.remove_file()
    repo_csv.start_writer()
    repo_csv.write_header()

    crawler = RepositoryCrawlerService()
    repos = crawler.crawl()

    for repo_json in repos:
        repo_model = Repository(repo_json)
        repo_csv.write_row(repo_model)
    repo_csv.reset_internal()

    print('Finished')
