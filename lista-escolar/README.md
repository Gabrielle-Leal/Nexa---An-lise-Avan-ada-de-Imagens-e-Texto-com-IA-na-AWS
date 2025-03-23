"def detect_file_text(image_path: str, output_json: str = "response.json") -> None:"
    Detecta texto em uma imagem usando AWS Textract e salva a resposta em um arquivo JSON.

    :param image_path: Caminho para a imagem.
    :param output_json: Nome do arquivo JSON de saída.
____________________________________________________________________________________________
"def extract_lines_from_json(json_path: str) -> list[str]:"

    Extrai linhas de texto de um arquivo JSON gerado pelo Textract.

    :param json_path: Caminho para o arquivo JSON.
    :return: Lista de linhas de texto detectadas.
_____________________________________________________________________________________________
"def get_lines(image_path: str, json_path: str = "response.json") -> list[str]:"

    Obtém as linhas de texto de uma imagem, usando Textract se necessário.

    :param image_path: Caminho para a imagem.
    :param json_path: Caminho para o arquivo JSON de resposta.
    :return: Lista de linhas de texto detectadas.
