import json
from pathlib import Path
import boto3
from botocore.exceptions import ClientError
from mypy_boto3_textract.type_defs import DetectDocumentTextResponseTypeDef


def detect_file_text(image_path: str, output_json: str = "response.json") -> None:
    client = boto3.client("textract")

    try:
        with open(image_path, "rb") as f:
            document_bytes = f.read()

        response = client.detect_document_text(Document={"Bytes": document_bytes})
        with open(output_json, "w") as response_file:
            json.dump(response, response_file, indent=4)
        print(f"Resposta salva em {output_json}")
    except FileNotFoundError:
        print(f"Erro: Arquivo de imagem não encontrado em {image_path}")
    except ClientError as e:
        print(f"Erro ao processar documento com Textract: {e}")


def extract_lines_from_json(json_path: str) -> list[str]:
    try:
        with open(json_path, "r") as f:
            data: DetectDocumentTextResponseTypeDef = json.load(f)
            blocks = data.get("Blocks", [])
        return [block["Text"] for block in blocks if block.get("BlockType") == "LINE"]
    except FileNotFoundError:
        print(f"Erro: Arquivo JSON não encontrado em {json_path}")
    except KeyError:
        print(f"Erro: Formato inválido do arquivo JSON em {json_path}")
    return []


def get_lines(image_path: str, json_path: str = "response.json") -> list[str]:
    if not Path(json_path).exists():
        detect_file_text(image_path, json_path)
    return extract_lines_from_json(json_path)


if __name__ == "__main__":
    # Caminho para a imagem e arquivo JSON
    image_path = str(Path(__file__).parent / "images" / "lista-material-escolar.jpeg")
    json_path = "response.json"

    # Obtém e imprime as linhas de texto
    for line in get_lines(image_path, json_path):
        print(line)