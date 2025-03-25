import requests

def parse_pdf(file_path):
    url = "http://localhost:8888/pdf_parse?parse_method=auto&is_json_md_dump=true"
    files = {
        'pdf_file': (file_path, open(file_path, 'rb'), 'application/pdf')
    }
    headers = {
        'accept': 'application/json'
    }

    response = requests.post(url, headers=headers, files=files)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    result_dict = parse_pdf("/home/tlmsq/testevotool/EvoTool-OL/Toolmake/docker-example/2010.07611v2.pdf")
    print(result_dict)

