import requests
import streamlit as st
import pandas as pd
from datetime import datetime

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Apuração 2026 · 2º turno",
    page_icon="🗳️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização CSS personalizada para manter o visual moderno do seu HTML original
st.markdown("""
<style>
    .main { background-color: #0f1318; color: #eef1f5; }
    .card {
        background-color: #171c23;
        border: 1px solid #262d37;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 16px;
    }
    .big-number { font-size: 42px; font-weight: 800; line-height: 1.1; }
    .c1 { color: #ff5a67; }
    .c2 { color: #4a93ff; }
    .badge-go { background-color: rgba(50, 213, 131, 0.15); color: #32d583; padding: 4px 12px; border-radius: 99px; font-weight: 600; }
    .badge-wait { background-color: rgba(253, 176, 34, 0.15); color: #fdb022; padding: 4px 12px; border-radius: 99px; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# Lista de UFs do TSE
UFS = [
    ("br", "Brasil"), ("ac", "Acre"), ("al", "Alagoas"), ("ap", "Amapá"), 
    ("am", "Amazonas"), ("ba", "Bahia"), ("ce", "Ceará"), ("df", "Distrito Federal"), 
    ("es", "Espírito Santo"), ("go", "Goiás"), ("ma", "Maranhão"), ("mt", "Mato Grosso"), 
    ("ms", "Mato Grosso do Sul"), ("mg", "Minas Gerais"), ("pa", "Pará"), ("pb", "Paraíba"), 
    ("pr", "Paraná"), ("pe", "Pernambuco"), ("pi", "Piauí"), ("rj", "Rio de Janeiro"), 
    ("rn", "Rio Grande do Norte"), ("rs", "Rio Grande do Sul"), ("ro", "Rondônia"), 
    ("rr", "Roraima"), ("sc", "Santa Catarina"), ("sp", "São Paulo"), ("se", "Sergipe"), 
    ("to", "Tocantins"), ("zz", "Exterior")
]

def safe_int(val):
    if val is None:
        return 0
    cleaned = ''.join(c for c in str(val) if c.isdigit() or c == '-')
    return int(cleaned) if cleaned else 0

def safe_float(val):
    if val is None:
        return 0.0
    try:
        return float(str(val).replace('%', '').replace(',', '.'))
    except ValueError:
        return 0.0

@st.cache_data(ttl=5) # Cache de 5 segundos para simular tempo real sem sobrecarregar a API
def fetch_tse_data(sigla, nome):
    url = f"https://resultados.tse.jus.br/oficial/ele2026/6258/dados/{sigla}/{sigla}-c0001-e006258-u.json"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return {"sigla": sigla, "nome": nome, "ok": False, "erro": f"HTTP {response.status_code}"}
        
        r = response.json()
        seen = {}
        cs = []
        
        for cg in r.get("carg", []):
            for ag in cg.get("agr", []):
                for p in ag.get("par", []):
                    for c in p.get("cand", []):
                        n = safe_int(c.get("n"))
                        if n in seen:
                            continue
                        seen[n] = 1
                        cs.append({
                            "n": n,
                            "nome": c.get("nmu") or c.get("nm") or "",
                            "sigla": p.get("sg") or "",
                            "votos": safe_int(c.get("vap")),
                            "pct": safe_float(c.get("pvapn") or c.get("pvap")),
                            "eleito": c.get("e") == "s" and (r.get("md") == "e" or r.get("tf") == "s" or "Eleit" in str(c.get("st", "")))
                        })
        
        cs.sort(key=lambda x: x["n"])
        if len(cs) < 2:
            return {"sigla": sigla, "nome": nome, "ok": False, "erro": "Dados insuficientes"}
            
        s = r.get("s", {})
        e = r.get("e", {})
        v = r.get("v", {})
        
        return {
            "sigla": sigla,
            "nome": nome,
            "ok": True,
            "cands": cs[:2],
            "pst": safe_float(s.get("pstn") or s.get("pst")),
            "st": safe_int(s.get("st")),
            "ts": safe_int(s.get("ts")),
            "gerado": r.get("hg", ""),
            "dv": r.get("dv") != "n",
            "final": r.get("tf") == "s",
            "definido": r.get("md") == "e",
            "brancos": safe_int(v.get("vb")),
            "nulos": safe_int(v.get("tvn")),
            "pvb": safe_float(v.get("pvb")),
            "ptvn": safe_float(v.get("ptvn")),
            "pc": safe_float(e.get("pc")),
            "pa": safe_float(e.get("pa")),
        }
    except Exception as e:
        return {"sigla": sigla, "nome": nome, "ok": False, "erro": str(e)}

# Cabeçalho Principal
st.title("Apuração das eleições 2026")
st.caption("2º turno · Presidente da República")

# Carrega dados do Brasil (BR)
with st.spinner("Carregando dados do TSE..."):
    br_data = fetch_tse_data("br", "Brasil")

# Exibição do Card Principal (Brasil)
if br_data["ok"]:
    cands = br_data["cands"]
    total_votos = cands[0]["votos"] + cands[1]["votos"]
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### {cands[0]['nome'].title()} <span style='font-size:14px; color:gray;'>({cands[0]['sigla']})</span>", unsafe_allow_html=True)
        st.markdown(f"<div class='big-number c1'>{cands[0]['pct']:.2f}%</div>", unsafe_allow_html=True)
        st.text(f"{cands[0]['votos']:,} votos".replace(",", "."))
        if cands[0]["eleito"]:
            st.success("✔ ELEITO")
            
    with col2:
        st.markdown(f"### {cands[1]['nome'].title()} <span style='font-size:14px; color:gray;'>({cands[1]['sigla']})</span>", unsafe_allow_html=True)
        st.markdown(f"<div class='big-number c2'>{cands[1]['pct']:.2f}%</div>", unsafe_allow_html=True)
        st.text(f"{cands[1]['votos']:,} votos".replace(",", "."))
        if cands[1]["eleito"]:
            st.success("✔ ELEITO")
            
    # Barra de progresso das urnas
    st.progress(br_data["pst"] / 100.0, text=f"Urnas apuradas: {br_data['pst']:.2f}% ({br_data['st']:,} de {br_data['ts']:,})".replace(",", "."))
else:
    st.warning(f"Aguardando dados oficiais do TSE... ({br_data.get('erro', '')})")

st.divider()

# Seção de Resultados por Estado
st.subheader("Resultado por estado")
ordenar_por = st.selectbox(
    "Ordenar por:",
    ["Ordem alfabética", "Mais urnas apuradas", "Maior diferença"]
)

# Carrega dados de todos os estados em paralelo/sequência otimizada
locais_data = [fetch_tse_data(sigla, nome) for sigla, nome in UFS[1:]]

# Ordenação
if ordenar_por == "Mais urnas apuradas":
    locais_data.sort(key=lambda x: x.get("pst", 0), reverse=True)
elif ordenar_por == "Maior diferença":
    def calc_dif(x):
        if not x.get("ok") or not x.get("cands"): return 0
        c = x["cands"]
        t = c[0]["votos"] + c[1]["votos"]
        return abs(c[0]["votos"] - c[1]["votos"]) / t if t > 0 else 0
    locais_data.sort(key=calc_dif, reverse=True)

# Grid de UFs
cols = st.columns(3)
for idx, uf in enumerate(locais_data):
    with cols[idx % 3]:
        with st.container(border=True):
            st.markdown(f"**{uf['nome']}** `{uf['sigla'].upper()}`")
            if uf["ok"]:
                c = uf["cands"]
                st.markdown(f"<span class='c1'><b>{c[0]['pct']:.1f}%</b></span> vs <span class='c2'><b>{c[1]['pct']:.1f}%</b></span>", unsafe_allow_html=True)
                st.progress(uf["pst"] / 100.0)
                st.caption(f"Urnas apuradas: {uf['pst']:.1f}%")
            else:
                st.caption("Sem dados ainda")

st.markdown("---")
st.caption("Fonte: resultados.tse.jus.br · Desenvolvido para Streamlit")
