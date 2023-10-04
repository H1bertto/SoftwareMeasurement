import pandas as pd
import csv

if __name__ == '__main__':
    ck_file = pd.read_csv("./ck.csv", encoding='utf-8').to_dict(orient='records')
    repository_file = pd.read_csv("./repository.csv", encoding='utf-8').to_dict(orient='records')

    result_file = open("result.csv", "a", newline='', encoding='utf-8')
    writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    Cks = []
    for row in ck_file:
        qi = (row["cbo"] + row["dit"] + row["lcom"]) / 3
        if qi > 0:
            Cks.append({
                "name": row["name"],
                "cbo": row["cbo"],
                "dit": row["dit"],
                "lcom": row["lcom"],
                "loc": row["loc"],
                "qi": qi
            })

    for row in repository_file:
        repository = {
            "name": row["name_with_owner"],
            "created_at": row["created_at"],
            "stargazer_count": row["stargazer_count"],
            "releases": row["releases"],
        }

        # M1 Pro be blessed
        for ck in Cks:
            if ck["name"] == repository["name"]:
                writer.writerow([
                    ck["name"],
                    ck["cbo"],
                    ck["dit"],
                    ck["lcom"],
                    ck["loc"],
                    repository["created_at"],
                    repository["stargazer_count"],
                    repository["releases"],
                    ck["qi"],
                ])
                result_file.flush()
