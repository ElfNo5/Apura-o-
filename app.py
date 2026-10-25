import streamlit as st
import streamlit.components.v1 as components

# Configuração da página para ocupar a tela toda com layout moderno
st.set_page_config(
    page_title="Apuração 2026 · Dashboard Interativo",
    page_icon="🗳️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização CSS do container Streamlit
st.markdown("""
<style>
    .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
    }
    header[data-testid="stHeader"], footer {
        display: none !important;
    }
    body {
        margin: 0;
        background-color: #0f1318;
    }
</style>
""", unsafe_allow_html=True)

# HTML/CSS/JS expandido com novas funcionalidades
HTML_EXPANDIDO = """
<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#0f1318">
<title>Apuração 2026 · Dashboard Expandido</title>
<style>
:root{--bg:#f4f5f7;--card:#fff;--tx:#1b1f24;--mut:#667085;--bd:#e4e7ec;--c1:#d92d3a;--c2:#1f6fe0;--ok:#12a150;--warn:#d98a00}
@media(prefers-color-scheme:dark){:root{--bg:#0f1318;--card:#171c23;--tx:#eef1f5;--mut:#98a2b3;--bd:#262d37;--c1:#ff5a67;--c2:#4a93ff;--ok:#32d583;--warn:#fdb022}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--tx);font:16px/1.4 "Segoe UI",system-ui,sans-serif}
.wrap{max-width:1280px;margin:0 auto;padding:20px 16px 40px}
header{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:12px;margin-bottom:16px}
h1{font-size:24px;margin:0;cursor:pointer}h1 small{display:block;font-size:14px;color:var(--mut);font-weight:400}
.header-actions{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.live{font-size:14px;color:var(--mut);display:flex;align-items:center;gap:8px}
.dot{width:10px;height:10px;border-radius:50%;background:var(--ok);animation:p 2s infinite}.dot.off{background:var(--warn);animation:none}
@keyframes p{50%{opacity:.35}}
.btn{background:var(--card);border:1px solid var(--bd);color:var(--tx);padding:8px 14px;border-radius:10px;font-size:14px;font-weight:600;cursor:pointer;transition:all .2s;display:inline-flex;align-items:center;gap:6px}
.btn:hover{background:var(--bd)}
.card{background:var(--card);border:1px solid var(--bd);border-radius:16px;padding:20px;margin-bottom:16px}
.badge{display:inline-block;padding:4px 12px;border-radius:99px;font-size:14px;font-weight:600;background:var(--bd);color:var(--tx)}
.badge.go{background:rgba(18,161,80,.15);color:var(--ok)}.badge.wait{background:rgba(217,138,0,.15);color:var(--warn)}
.top{display:flex;flex-wrap:wrap;justify-content:space-between;gap:10px;align-items:center;margin-bottom:16px}
.top b{font-size:18px}
.cands{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.cand{padding:8px 4px}.cand.r{text-align:right}
.cname{font-size:20px;font-weight:700}.cinfo{color:var(--mut);font-size:14px}
.big{font-size:56px;font-weight:800;line-height:1.1;margin:6px 0}
.cand .v{font-size:16px;color:var(--mut)}
.c1{color:var(--c1)}.c2{color:var(--c2)}
.eleito{display:inline-block;margin-top:6px;padding:2px 10px;border-radius:99px;background:var(--ok);color:#fff;font-weight:700;font-size:14px}
.bar{height:22px;border-radius:99px;overflow:hidden;display:flex;background:var(--bd);margin:14px 0 6px;position:relative}
.bar i{display:block;height:100%;transition:width .6s}.bar .a{background:var(--c1)}.bar .b{background:var(--c2)}
.bar:after{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:var(--card);opacity:.9}
.lead{text-align:center;font-size:18px;font-weight:600;margin:10px 0 4px}
.prog{margin-top:16px}.prog .t{display:flex;justify-content:space-between;font-size:14px;color:var(--mut);margin-bottom:4px}
.prog .tr{height:10px;background:var(--bd);border-radius:99px;overflow:hidden}.prog .tr i{display:block;height:100%;background:var(--ok);transition:width .6s}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-top:16px}
.stat{background:var(--bg);border-radius:12px;padding:10px 12px}.stat span{display:block;font-size:13px;color:var(--mut)}.stat b{font-size:17px}
.tools{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:10px;margin:24px 0 12px}
.tools h2{margin:0;font-size:20px}
.search-controls{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
input[type="text"], select{font:inherit;padding:8px 12px;border-radius:10px;border:1px solid var(--bd);background:var(--card);color:var(--tx)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:12px}
.uf{padding:14px 16px;border-left:6px solid var(--bd)}.uf.l1{border-left-color:var(--c1)}.uf.l2{border-left-color:var(--c2)}
.uf .h{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px}.uf .h b{font-size:17px}.uf .h span{font-size:13px;color:var(--mut)}
.uf .p{display:flex;justify-content:space-between;font-size:20px;font-weight:700;margin-bottom:4px}
.uf .bar{height:12px;margin:4px 0 8px}
.uf .f{display:flex;justify-content:space-between;font-size:13px;color:var(--mut)}
.uf .who{font-weight:600}
.empty{color:var(--mut);padding:8px 0}
footer{margin-top:28px;font-size:13px;color:var(--mut);text-align:center}
@media(max-width:620px){.big{font-size:40px}.cname{font-size:17px}}

/* SIMULADOR */
.sim-box{background:var(--card);border:1px solid var(--bd);border-radius:16px;padding:20px;margin-bottom:20px}
.sim-title{font-size:18px;font-weight:700;margin-bottom:12px;display:flex;justify-content:space-between;align-items:center}
.sim-range{width:100%;margin:10px 0}

#fx{position:fixed;top:0;left:0;right:0;bottom:0;z-index:99;display:none;align-items:center;justify-content:center;flex-direction:column;text-align:center;padding:20px;overflow:hidden}
#fx.on{display:flex}#fx canvas{position:absolute;top:0;left:0;right:0;bottom:0;width:100%;height:100%}
#fx .e{position:relative;font-size:clamp(70px,22vw,210px);line-height:1;animation:bnc 1s ease-in-out infinite}
#fx .t{position:relative;font-size:clamp(32px,9vw,90px);font-weight:900;line-height:1.05;color:#fff;text-shadow:0 4px 24px rgba(0,0,0,.55);margin-top:8px}
#fx .s{position:relative;font-size:clamp(16px,3.5vw,28px);color:#fff;opacity:.92;margin-top:10px}
#fx button{position:relative;margin-top:26px;font:inherit;font-weight:700;padding:12px 30px;border-radius:99px;border:0;cursor:pointer;background:#fff;color:#111}
#fx.win{background:radial-gradient(circle,#ff3b4a 0,#a30f1c 55%,#350309 100%);animation:fl 1s ease-in-out infinite alternate}
#fx.win .t{animation:pop .7s ease-in-out infinite alternate,col 1.5s linear infinite}
#fx.lose{background:linear-gradient(#22344f,#0a111d)}#fx.lose .e{animation:sob 1.4s ease-in-out infinite}#fx.lose .t{font-weight:700}
@keyframes bnc{50%{transform:translateY(-20px) rotate(8deg) scale(1.1)}}
@keyframes sob{0%,100%{transform:translateY(0) rotate(-4deg)}50%{transform:translateY(10px) rotate(4deg)}}
@keyframes fl{to{filter:hue-rotate(35deg) brightness(1.2)}}@keyframes pop{to{transform:scale(1.08)}}
@keyframes col{0%{color:#fff}25%{color:#ffe14d}50%{color:#ff9fd0}75%{color:#9ff0ff}100%{color:#fff}}
</style></head><body><div class="wrap">
<header>
  <h1>Apuração 2026<small>2º turno · Presidente da República</small></h1>
  <div class="header-actions">
    <button class="btn" id="btn-sound">🔊 Som: Desligado</button>
    <button class="btn" id="btn-export">📥 Exportar CSV</button>
    <div class="live"><span class="dot" id="dot"></span><span id="live">Conectando…</span></div>
  </div>
</header>

<div id="br" class="card"><div class="empty">Carregando dados do TSE…</div></div>

<!-- SIMULADOR INTERATIVO -->
<div class="sim-box">
  <div class="sim-title">
    <span>🧮 Simulador de Votos Restantes</span>
    <span id="sim-pct-val" style="font-size:15px; color:var(--mut);">0% restante</span>
  </div>
  <input type="range" id="sim-range" class="sim-range" min="0" max="100" value="50">
  <div id="sim-res" style="font-weight:600; font-size:15px; color:var(--tx);">Projeção com base na apuração atual...</div>
</div>

<div class="tools">
  <h2>Resultado por estado</h2>
  <div class="search-controls">
    <input type="text" id="search" placeholder="Buscar estado (ex: SP, Bahia)...">
    <select id="ord">
      <option value="nome">Ordem alfabética</option>
      <option value="urnas">Mais urnas apuradas</option>
      <option value="dif">Maior diferença</option>
      <option value="eq">Mais disputados</option>
    </select>
  </div>
</div>

<div id="uf" class="grid"></div>

<footer>Fonte: resultados.tse.jus.br · Atualiza sozinho a cada poucos segundos · Resultado parcial, só o TSE proclama os eleitos.</footer>
</div>

<div id="fx"><canvas id="cv"></canvas><div class="e" id="fxe"></div><div class="t" id="fxt"></div><div class="s" id="fxs"></div><button id="fxb">Fechar</button></div>

<script>
const $=id=>document.getElementById(id);
const nf=n=>Number(n).toLocaleString('pt-BR');
const pc=p=>Number(p).toLocaleString('pt-BR',{minimumFractionDigits:2,maximumFractionDigits:2})+'%';
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const title=s=>s.toLowerCase().replace(/(^|\s)\S/g,m=>m.toUpperCase());
const first=s=>{s=title(s);return s.length>12?s.split(' ')[0]:s};
const FAV=13;let fxShown=null,fxMode='',fxRaf=0,parts=[];
let audioEnabled=false;

// Efeitos Sonoros com Web Audio API
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
function playBeep(freq=440, type='sine', duration=0.15) {
  if(!audioEnabled) return;
  try {
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = type; osc.frequency.value = freq;
    osc.connect(gain); gain.connect(audioCtx.destination);
    osc.start(); gain.gain.exponentialRampToValueAtTime(0.00001, audioCtx.currentTime + duration);
    osc.stop(audioCtx.currentTime + duration);
  } catch(e){}
}

$('btn-sound').onclick = () => {
  audioEnabled = !audioEnabled;
  $('btn-sound').textContent = audioEnabled ? '🔊 Som: Ligado' : '🔇 Som: Desligado';
  if(audioEnabled) playBeep(880, 'triangle', 0.2);
};

const cv=$('cv'),cx=cv.getContext('2d'),R=Math.random;
function fxSize(){cv.width=innerWidth;cv.height=innerHeight}
function burst(x,y){const h=R()*360;for(let i=0;i<70;i++){const a=R()*6.283,v=2+R()*6;parts.push({k:'f',x:x,y:y,vx:Math.cos(a)*v,vy:Math.sin(a)*v,l:70,c:'hsl('+(h+R()*40)+',100%,60%)'})}}
function fxLoop(){const w=cv.width,h=cv.height;cx.clearRect(0,0,w,h);
 if(fxMode==='win'){for(let i=0;i<5;i++)parts.push({k:'c',x:R()*w,y:-12,vx:(R()-.5)*3,vy:2+R()*4,s:6+R()*9,r:R()*6,vr:(R()-.5)*.3,c:'hsl('+(R()*360|0)+',95%,60%)'});if(R()<.05)burst(R()*w,R()*h*.6)}
 else for(let i=0;i<4;i++)parts.push({k:'r',x:R()*(w+200),y:-20,vx:-2,vy:9+R()*7,s:10+R()*16});
 parts=parts.filter(p=>{p.x+=p.vx;p.y+=p.vy;
  if(p.k==='c'){p.r+=p.vr;cx.save();cx.translate(p.x,p.y);cx.rotate(p.r);cx.fillStyle=p.c;cx.fillRect(-p.s/2,-p.s/4,p.s,p.s/2);cx.restore();return p.y<h+20}
  if(p.k==='f'){p.vy+=.08;p.l--;cx.globalAlpha=Math.max(p.l/70,0);cx.fillStyle=p.c;cx.beginPath();cx.arc(p.x,p.y,2.6,0,6.283);cx.fill();cx.globalAlpha=1;return p.l>0}
  cx.strokeStyle='rgba(160,200,255,.65)';cx.lineWidth=2;cx.beginPath();cx.moveTo(p.x,p.y);cx.lineTo(p.x+p.vx*1.2,p.y-p.s);cx.stroke();return p.y<h+30});
 if(parts.length>1800)parts.splice(0,parts.length-1800);fxRaf=requestAnimationFrame(fxLoop)}
function fxStart(k,me,ot){const nm=title(me.nome||'Lula');$('fx').className='on '+k;fxMode=k;parts=[];fxSize();
 if(k==='win'){
   $('fxe').textContent='🥳🎉';$('fxt').textContent='🎊 '+nm.toUpperCase()+' ELEITO! 🎊';$('fxs').textContent='Presidente da República · 2026 🇧🇷🎆';
   playBeep(523, 'sine', 0.3); setTimeout(()=>playBeep(659, 'sine', 0.4), 150);
 } else {
   $('fxe').textContent='😭';$('fxt').textContent=nm+' não foi eleito…';$('fxs').textContent=(ot&&ot.nome?title(ot.nome)+' foi eleito(a). ':'')+'Hoje a chuva é de lágrimas 💧';
   playBeep(200, 'sawtooth', 0.5);
 }
 cancelAnimationFrame(fxRaf);fxLoop()}
function fxClose(){$('fx').className='';cancelAnimationFrame(fxRaf);parts=[]}
$('fxb').onclick=fxClose;addEventListener('resize',fxSize);

function check(x){const i=x.cands.findIndex(c=>c.n===FAV);if(i<0)return;const me=x.cands[i],ot=x.cands[1-i];
 const k=me.eleito?'win':(ot.eleito?'lose':null);if(k&&k!==fxShown){fxShown=k;fxStart(k,me,ot)}}

let taps=0,tt=0,dm=0;document.querySelector('h1').onclick=()=>{taps++;clearTimeout(tt);tt=setTimeout(()=>taps=0,1500);
 if(taps>=5){taps=0;fxStart(dm++%2?'lose':'win',{nome:'Lula'},{nome:'Adversário'})}};

let data=null;
function share(x){const t=x.cands[0].votos+x.cands[1].votos;return t?x.cands[0].votos/t*100:50}
function lead(x){const [a,b]=x.cands;if(a.votos===b.votos)return null;const w=a.votos>b.votos?0:1;const t=a.votos+b.votos;
 return {i:w,nome:x.cands[w].nome,pp:Math.abs(a.votos-b.votos)/t*100,dif:Math.abs(a.votos-b.votos)}}
function status(x){const v=x.cands[0].votos+x.cands[1].votos;
 if(x.final)return['Totalização final','go'];if(x.definido)return['Resultado definido','go'];
 if(!x.dv&&v===0)return['Aguardando liberação dos votos','wait'];if(v===0||x.pst===0)return['Apuração ainda não começou','wait'];
 return['Apuração em andamento','go']}

function updateSimulator(br) {
  if(!br || !br.ok) return;
  const val = parseInt($('sim-range').value);
  $('sim-pct-val').textContent = val + '% dos votos restantes para C1';
  const c1 = br.cands[0], c2 = br.cands[1];
  const tVotos = c1.votos + c2.votos;
  const pApurado = br.pst / 100;
  if(pApurado === 0) return;
  const totalEstimado = tVotos / pApurado;
  const faltantes = Math.max(0, totalEstimado - tVotos);
  
  const novosC1 = c1.votos + (faltantes * (val / 100));
  const novosC2 = c2.votos + (faltantes * ((100 - val) / 100));
  const totalFinal = novosC1 + novosC2;
  const pFinalC1 = (novosC1 / totalFinal) * 100;
  const pFinalC2 = (novosC2 / totalFinal) * 100;
  
  const ldr = pFinalC1 > pFinalC2 ? c1.nome : c2.nome;
  $('sim-res').innerHTML = `Com ${val}% do restante para ${esc(first(c1.nome))}, resultado final projetado: <span class="c1">${pc(pFinalC1)}</span> vs <span class="c2">${pc(pFinalC2)}</span> (Liderança: <b>${esc(title(ldr))}</b>)`;
}
$('sim-range').oninput = () => { if(data) updateSimulator(data.locais[0]); };

function renderBR(x){
 if(!x||!x.ok){$('br').innerHTML='<div class="empty">Aguardando dados do TSE…'+(x&&x.erro?' ('+esc(x.erro)+')':'')+'</div>';return}
 check(x); const [a,b]=x.cands,s=share(x),L=lead(x),st=status(x),v=a.votos+b.votos;
 let msg='Ainda sem votos apurados';
 if(L&&v>0){msg=esc(first(L.nome))+' está na frente com '+L.pp.toFixed(2).replace('.',',')+' pontos percentuais de vantagem ('+nf(L.dif)+' votos)';
  if(x.cands[L.i].eleito)msg=esc(title(L.nome))+' foi eleito(a)'}
 const cd=(c,k,r)=>'<div class="cand '+(r?'r':'')+'"><div class="cname c'+k+'">'+esc(title(c.nome))+'</div><div class="cinfo">'+c.n+' · '+esc(c.sigla)+'</div>'+
  '<div class="big c'+k+'">'+(v?pc(c.pct):'—')+'</div><div class="v">'+nf(c.votos)+' votos</div>'+(c.eleito?'<span class="eleito">✔ ELEITO</span>':'')+'</div>';
 $('br').innerHTML='<div class="top"><b>Brasil</b><span class="badge '+st[1]+'">'+st[0]+'</span></div>'+
  '<div class="cands">'+cd(a,1,false)+cd(b,2,true)+'</div>'+
  '<div class="bar"><i class="a" style="width:'+(v?s:50)+'%"></i><i class="b" style="width:'+(v?100-s:50)+'%"></i></div>'+
  '<div class="lead">'+msg+'</div>'+
  '<div class="prog"><div class="t"><span>Urnas apuradas</span><b>'+pc(x.pst)+' ('+nf(x.st)+' de '+nf(x.ts)+')</b></div><div class="tr"><i style="width:'+x.pst+'%"></i></div></div>'+
  '<div class="stats"><div class="stat"><span>Comparecimento</span><b>'+pc(x.pc)+'</b></div><div class="stat"><span>Abstenção</span><b>'+pc(x.pa)+'</b></div>'+
  '<div class="stat"><span>Votos brancos</span><b>'+pc(x.pvb)+' · '+nf(x.brancos)+'</b></div><div class="stat"><span>Votos nulos</span><b>'+pc(x.ptvn)+' · '+nf(x.nulos)+'</b></div></div>';
 updateSimulator(x);
}

function card(x){
 if(!x.ok)return '<div class="card uf"><div class="h"><b>'+esc(x.nome)+'</b><span>'+x.sigla.toUpperCase()+'</span></div><div class="empty">Sem dados ainda'+(x.erro?' ('+esc(x.erro)+')':'')+'</div></div>';
 const [a,b]=x.cands,v=a.votos+b.votos,s=share(x),L=lead(x);
 const who=L&&v?'<span class="who c'+(L.i+1)+'">'+esc(first(L.nome))+' +'+L.pp.toFixed(1).replace('.',',')+' p.p.</span>':'<span>Sem votos ainda</span>';
 return '<div class="card uf '+(L&&v?'l'+(L.i+1):'')+'"><div class="h"><b>'+esc(x.nome)+'</b><span>'+x.sigla.toUpperCase()+'</span></div>'+
  '<div class="p"><span class="c1">'+(v?pc(a.pct):'—')+'</span><span class="c2">'+(v?pc(b.pct):'—')+'</span></div>'+
  '<div class="bar"><i class="a" style="width:'+(v?s:50)+'%"></i><i class="b" style="width:'+(v?100-s:50)+'%"></i></div>'+
  '<div class="f">'+who+'<span>Urnas: '+pc(x.pst)+'</span></div></div>'}

function renderUF(){
 if(!data)return;const o=$('ord').value; const q=$('search').value.toLowerCase().trim();
 let l=data.locais.slice(1);
 if(q) l = l.filter(x => x.nome.toLowerCase().includes(q) || x.sigla.toLowerCase().includes(q));
 const k={nome:()=>0,urnas:x=>-x.pst,dif:x=>{const t=x.cands.length?x.cands[0].votos+x.cands[1].votos:0;return t?-Math.abs(share(x)-50):1},eq:x=>{const t=x.cands.length?x.cands[0].votos+x.cands[1].votos:0;return t?Math.abs(share(x)-50):99}}[o];
 if(o!=='nome')l.sort((p,q)=>k(p)-k(q));
 $('uf').innerHTML=l.map(card).join('')}

$('search').oninput = renderUF;

$('btn-export').onclick = () => {
  if(!data) return;
  let csv = 'UF,Nome,Cand1_Votos,Cand1_Pct,Cand2_Votos,Cand2_Pct,Urnas_Apuradas_Pct\n';
  data.locais.forEach(x => {
    if(x.ok && x.cands.length>=2) {
      csv += `${x.sigla.toUpperCase()},"${x.nome}",${x.cands[0].votos},${x.cands[0].pct},${x.cands[1].votos},${x.cands[1].pct},${x.pst}\n`;
    }
  });
  const blob = new Blob([csv], {type: 'text/csv'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'apuracao_eleicoes_2026.csv';
  a.click();
};

const UFS=[["br", "Brasil"], ["ac", "Acre"], ["al", "Alagoas"], ["ap", "Amapá"], ["am", "Amazonas"], ["ba", "Bahia"], ["ce", "Ceará"], ["df", "Distrito Federal"], ["es", "Espírito Santo"], ["go", "Goiás"], ["ma", "Maranhão"], ["mt", "Mato Grosso"], ["ms", "Mato Grosso do Sul"], ["mg", "Minas Gerais"], ["pa", "Pará"], ["pb", "Paraíba"], ["pr", "Paraná"], ["pe", "Pernambuco"], ["pi", "Piauí"], ["rj", "Rio de Janeiro"], ["rn", "Rio Grande do Norte"], ["rs", "Rio Grande do Sul"], ["ro", "Rondônia"], ["rr", "Roraima"], ["sc", "Santa Catarina"], ["sp", "São Paulo"], ["se", "Sergipe"], ["to", "Tocantins"], ["zz", "Exterior"]];
const N=v=>{const s=String(v==null?'':v).replace(/[^0-9-]/g,'');return s?parseInt(s,10):0};
const D=v=>{const x=parseFloat(String(v==null?'':v).replace('%','').replace(',','.'));return isNaN(x)?0:x};
function build(sig,nome,r){const o={sigla:sig,nome:nome,ok:false,cands:[]};if(!r)return o;const seen={},cs=[];
 (r.carg||[]).forEach(cg=>(cg.agr||[]).forEach(ag=>(ag.par||[]).forEach(p=>(p.cand||[]).forEach(c=>{const n=N(c.n);if(seen[n])return;seen[n]=1;
  cs.push({n:n,nome:c.nmu||c.nm||'',sigla:p.sg||'',votos:N(c.vap),pct:D(c.pvapn||c.pvap),eleito:c.e==='s'&&(r.md==='e'||r.tf==='s'||String(c.st||'').indexOf('Eleit')>=0)})}))));
 cs.sort((a,b)=>a.n-b.n);if(cs.length<2)return o;const s=r.s||{},e=r.e||{},v=r.v||{};
 return Object.assign(o,{ok:true,cands:cs.slice(0,2),pst:D(s.pstn||s.pst),st:N(s.st),ts:N(s.ts),gerado:r.hg||'',dv:r.dv!=='n',final:r.tf==='s',definido:r.md==='e',brancos:N(v.vb),nulos:N(v.tvn),pvb:D(v.pvb),ptvn:D(v.ptvn),pc:D(e.pc),pa:D(e.pa),comp:N(e.c),abst:N(e.a)})}
const cache={};
async function one(u){try{const r=await fetch('https://resultados.tse.jus.br/oficial/ele2026/6258/dados/'+u[0]+'/'+u[0]+'-c0001-e006258-u.json');if(!r.ok)throw new Error('HTTP '+r.status);cache[u[0]]=build(u[0],u[1],await r.json())}
 catch(e){const old=cache[u[0]]||{sigla:u[0],nome:u[1],ok:fa
