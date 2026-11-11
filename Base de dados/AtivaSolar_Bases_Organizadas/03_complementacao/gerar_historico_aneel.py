"""Agrega registros oficiais ANEEL por município e ano.
Execute --help. Os nomes das colunas devem ser conferidos no cabeçalho oficial.
Não baixa dados. Requer CSV oficial extraído e nomes de colunas explicitados.
"""
import argparse
import csv
from collections import Counter
from datetime import datetime
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('entrada', type=Path)
parser.add_argument('saida', type=Path)
parser.add_argument('--municipio', required=True, help='Coluna do código IBGE municipal')
parser.add_argument('--fonte', required=True, help='Coluna da fonte de geração')
parser.add_argument('--data', required=True, help='Coluna da data de conexão')
parser.add_argument('--identificador', required=True, help='Coluna do identificador único do empreendimento')
parser.add_argument('--valor-solar', default='UFV')
parser.add_argument('--encoding', default='utf-8-sig')
parser.add_argument('--formato-data', default='%Y-%m-%d')
args = parser.parse_args()
base = Path(__file__).resolve().parents[1] / '02_base_integrada/base_integrada.csv'
with base.open(encoding='utf-8-sig', newline='') as stream:
    municipios = {row['codigo_ibge'] for row in csv.DictReader(stream, delimiter=';')}
counts = Counter()
seen = set()
with args.entrada.open(encoding=args.encoding, newline='') as stream:
    reader = csv.DictReader(stream, delimiter=';')
    required = {args.municipio, args.fonte, args.data, args.identificador}
    if not required.issubset(reader.fieldnames or []):
        raise ValueError('Colunas informadas ausentes no CSV')
    for row in reader:
        code = row[args.municipio].strip()
        if code not in municipios or row[args.fonte].strip() != args.valor_solar:
            continue
        identifier = row[args.identificador].strip()
        if not identifier:
            raise ValueError('Empreendimento selecionado sem identificador')
        year = datetime.strptime(row[args.data].strip(), args.formato_data).year
        key = (code, year)
        if identifier in seen:
            raise ValueError('Identificador duplicado no recorte. Rever granularidade antes de agregar')
        seen.add(identifier)
        counts[key] += 1
if not counts:
    raise ValueError('Nenhum registro selecionado. Verifique colunas e valor da fonte solar')
with args.saida.open('w', encoding='utf-8-sig', newline='') as stream:
    writer = csv.writer(stream, delimiter=';')
    writer.writerow(['codigo_ibge', 'ano_conexao', 'empreendimentos_fotovoltaicos'])
    for (code, year), count in sorted(counts.items()):
        writer.writerow([code, year, count])
print(f'Geradas {len(counts)} combinações município/ano a partir de {len(seen)} empreendimentos')
