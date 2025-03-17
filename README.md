# AutoCertify

![Certificado Exemplo](src/certificates/exemplo_certificado.png)

## Configuração

1. Clone o repositório:
    ```bash
    git clone [https://github.com/GabriellOlliveira99/AutoCertify.git]
    cd AutoCertify
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Execução

1. Certifique-se de que os arquivos de fontes, imagem e planilha estão nos diretórios corretos.
2. Execute o script:
    ```bash
    python src/autocertify.py
    ```

Os certificados gerados serão salvos no diretório `src/certificates`.

## Personalização

Se você deseja utilizar este projeto com outro arquivo de imagem de certificado, será necessário alterar a posição das informações (nome do aluno, data do curso e data de emissão) no script. Para isso, edite as coordenadas no arquivo `src/autocertify.py` nas seguintes linhas:

```python
# Desenhar o texto na imagem
desenhar.text((700, 600), name_alunos, fill='black', font=font_nome)  # Coordenadas do nome do aluno
desenhar.text((1050, 823), date_curso, fill='black', font=font_geral)  # Coordenadas da data do curso
desenhar.text((1680, 1323), emissao_cert, fill='black', font=font_geral)  # Coordenadas da data de emissão
```

Altere os valores das coordenadas `(x, y)` conforme necessário para posicionar corretamente as informações no seu novo certificado.

## Contribuição

Sinta-se à vontade para abrir issues e pull requests para melhorias.

## PROJETO AINDA EM CONSTRUÇÃO
