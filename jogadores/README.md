📌 Resumo das Melhorias Implementadas

-Tratamento de Erros Aprimorado
Captura de erros específicos (AWS, imagens inválidas, arquivos não encontrados).
Mensagens claras para facilitar o diagnóstico.

-Configuração Flexível via Linha de Comando
Parâmetros dinâmicos (--source, --target, --threshold).
Nome personalizável para o arquivo de saída (--output).

-Validação de Imagens
Verificação automática de arquivos corrompidos ou incompatíveis.

-Tipagem Forte e Documentação
Type hints para melhor autocompletar e detecção de erros.
Docstrings detalhadas em todas as funções.

-Logs Estruturados
Registro em arquivo (app.log) e console.
Timestamp e níveis de severidade (INFO, ERROR).

-Visualização Aprimorada
Legendas com contagem de rostos e porcentagem de similaridade.

-Testabilidade
Código refatorado para facilitar testes unitários.
Exemplo com pytest incluído.

-Segurança
Credenciais da AWS gerenciadas via .env (não hardcoded).
