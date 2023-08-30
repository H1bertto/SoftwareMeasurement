from domain.repository_crawler_service import RepositoryCrawlerService
from domain.repository_model import Repository
from domain.repository_csv_service import RepositoryCsvService

if __name__ == '__main__':
    repo_csv = RepositoryCsvService()
    repo_csv.remove_file()
    repo_csv.start_writer()
    repo_csv.write_header()

    crawler = RepositoryCrawlerService()

    result = crawler.crawl()
    for page in range(1, 10):
        for repo_json in result["repos"]:
            repo_model = Repository(repo_json)
            repo_csv.write_row(repo_model)
        result = crawler.crawl(result["cursor"])

    repo_csv.reset_internal()
    print('Finished')
