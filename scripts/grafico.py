#!/usr/bin/env python3
"""Gera grafico.svg: mapa de calor das contribuicoes, na paleta roxa do perfil.

Le a pagina publica de contribuicoes do GitHub -- a mesma que qualquer visitante
ve, sem token e sem revelar nada a mais. Servico de terceiro para isso (o
github-readme-activity-graph e companhia) responde 402 e 503 desde hoje, entao
aqui e feito em casa e roda no Actions.

Falha em voz alta de proposito: se o HTML do GitHub mudar e o parser nao achar
celula, o script sai com erro em vez de commitar um SVG vazio.
"""
import re
import sys
import urllib.request
from datetime import date

USUARIO = "ChaconDavi"
SAIDA = "grafico.svg"

# paleta: mesma familia do banner.svg
FUNDO = "#1B0A40"
NIVEL = ["#2E1065", "#5B21B6", "#7C3AED", "#A78BFA", "#DDD6FE"]
TEXTO = "#B69CFB"
TEXTO_FORTE = "#DDD6FE"

CELULA, VAO = 11, 3
PASSO = CELULA + VAO
MARGEM_ESQ, MARGEM_TOPO = 34, 46
MESES = ["jan", "fev", "mar", "abr", "mai", "jun",
         "jul", "ago", "set", "out", "nov", "dez"]
DIAS = {1: "seg", 3: "qua", 5: "sex"}


def buscar(ano: int) -> str:
    url = (f"https://github.com/users/{USUARIO}/contributions"
           f"?from={ano}-01-01&to={ano}-12-31")
    req = urllib.request.Request(url, headers={"User-Agent": "perfil-grafico"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def extrair(html: str):
    """Devolve [(date, nivel)] em ordem cronologica, e o total do ano."""
    pares = re.findall(r'data-date="(\d{4}-\d{2}-\d{2})"[^>]*?data-level="(\d)"', html)
    if not pares:  # a ordem dos atributos ja mudou uma vez; tenta invertida
        pares = [(d, n) for n, d in
                 re.findall(r'data-level="(\d)"[^>]*?data-date="(\d{4}-\d{2}-\d{2})"', html)]
    if not pares:
        sys.exit("ERRO: nenhuma celula encontrada — o HTML do GitHub mudou")
    total = sum(int(x) for x in re.findall(r">(\d+) contribution", html))
    dias = sorted(((date.fromisoformat(d), int(n)) for d, n in pares), key=lambda p: p[0])
    return dias, total


def montar(dias, total, ano) -> str:
    # coluna = semana, linha = dia da semana (0 = domingo, como no GitHub)
    col0 = dias[0][0]
    desloc = (col0.weekday() + 1) % 7          # segunda=0 -> domingo=0
    celulas, rotulos, visto = [], [], set()
    for i, (d, n) in enumerate(dias):
        pos = i + desloc
        col, lin = pos // 7, pos % 7
        x = MARGEM_ESQ + col * PASSO
        y = MARGEM_TOPO + lin * PASSO
        celulas.append(
            f'<rect x="{x}" y="{y}" width="{CELULA}" height="{CELULA}" rx="2.5" '
            f'fill="{NIVEL[n]}"><title>{d.isoformat()}</title></rect>')
        if d.month not in visto and d.day <= 7:
            visto.add(d.month)
            rotulos.append(
                f'<text x="{x}" y="{MARGEM_TOPO - 10}" font-size="11" '
                f'fill="{TEXTO}" font-family="{FONTE}">{MESES[d.month - 1]}</text>')

    semanas = (len(dias) + desloc + 6) // 7
    larg = MARGEM_ESQ + semanas * PASSO + 12
    alt = MARGEM_TOPO + 7 * PASSO + 30

    diasem = "\n  ".join(
        f'<text x="6" y="{MARGEM_TOPO + l * PASSO + 9}" font-size="10" '
        f'fill="{TEXTO}" font-family="{FONTE}">{r}</text>'
        for l, r in DIAS.items())

    # "mais" precisa de ~30px a direita da ultima celula, senao sai cortado
    legenda_x = larg - 12 - 30 - 5 * PASSO
    legenda = "\n  ".join(
        f'<rect x="{legenda_x + i * PASSO}" y="{alt - 20}" width="{CELULA}" '
        f'height="{CELULA}" rx="2.5" fill="{c}"/>' for i, c in enumerate(NIVEL))
    fim_legenda = legenda_x + 5 * PASSO

    ativos = sum(1 for _, n in dias if n > 0)
    fmt = f"{total:,}".replace(",", ".")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {larg} {alt}" width="{larg}" height="{alt}" role="img" aria-label="{total} contribuicoes em {ano}, em {ativos} dias">
  <rect width="{larg}" height="{alt}" rx="10" fill="{FUNDO}"/>
  <text x="{MARGEM_ESQ}" y="24" font-size="14" font-weight="600" fill="{TEXTO_FORTE}" font-family="{FONTE}">{fmt} contribuições em {ano}</text>
  <text x="{larg - 12}" y="24" font-size="14" fill="{TEXTO}" font-family="{FONTE}" text-anchor="end">{ativos} dias ativos</text>
  {diasem}
  {"".join(rotulos)}
  {"".join(celulas)}
  {legenda}
  <text x="{legenda_x - 8}" y="{alt - 11}" font-size="10" fill="{TEXTO}" font-family="{FONTE}" text-anchor="end">menos</text>
  <text x="{fim_legenda + 6}" y="{alt - 11}" font-size="10" fill="{TEXTO}" font-family="{FONTE}">mais</text>
</svg>
'''


FONTE = "'Helvetica Neue', Helvetica, Arial, sans-serif"

if __name__ == "__main__":
    ano = int(sys.argv[1]) if len(sys.argv) > 1 else date.today().year
    dias, total = extrair(buscar(ano))
    svg = montar(dias, total, ano)
    with open(SAIDA, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"{SAIDA}: {total} contribuicoes, "
          f"{sum(1 for _, n in dias if n > 0)} dias ativos, {len(dias)} celulas")
