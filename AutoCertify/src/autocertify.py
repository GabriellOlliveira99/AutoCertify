import openpyxl
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os

# Definir os caminhos dos arquivos
base_dir = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(base_dir, 'data', 'exampleNames.xlsx')
font_nome_path = os.path.join(base_dir, 'fonts', 'Courgette-Regular.ttf')
font_geral_path = os.path.join(base_dir, 'fonts', 'georgia.ttf')
certificado_path = os.path.join(base_dir, 'image', 'certificado.png')

# Carregar a planilha Excel
workbook_alunos = openpyxl.load_workbook(excel_path)
sheet_alunos = workbook_alunos['Planilha1']

# Iterar sobre as linhas da planilha, começando da segunda linha
for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2)):
    name_alunos = linha[0].value # NOME ALUNOS
    date_curso = linha[1].value # DATA DO CURSO
    emissao_cert = linha[2].value # DATA DE EMISSÃO

    # Verificar se o nome do aluno é nulo e quebrar o loop
    if name_alunos is None:
        break
      
    # Carregar as fontes
    font_nome = ImageFont.truetype(font_nome_path, 90)
    font_geral = ImageFont.truetype(font_geral_path, 40)

    # Abrir a imagem do certificado
    image = Image.open(certificado_path)
    desenhar = ImageDraw.Draw(image)

    # Desenhar o texto na imagem
    desenhar.text((700, 600), name_alunos, fill='black', font=font_nome)
    desenhar.text((1050, 823), date_curso, fill='black', font=font_geral)
    desenhar.text((1680, 1323), emissao_cert, fill='black', font=font_geral)

    # Salvar a imagem com o nome do aluno
    image.save(os.path.join(base_dir, 'certificates', f'{indice}_{name_alunos}_certificado.png'))
