"""Fontes independentes do curso; monta aulas e invoca o motor oficial v6."""
from pathlib import Path
from html import escape as esc
import json, re, subprocess, sys

ROOT = Path(__file__).resolve().parent
SKILL = Path('/home/nmaldaner/projetos/formato-curso-inema/formato-curso-v6')
base = json.loads((ROOT/'context/conteudo-base.json').read_text())
lessons = json.loads((ROOT/'context/aulas-editoriais.json').read_text())

def clean(text):
    return text

def p(text, cls=''):
    return f'<p{(" class="+chr(34)+cls+chr(34)) if cls else ""}>{esc(clean(text))}</p>'

def sentence_paragraphs(text):
    return ''.join(p(t) for t in re.split(r'(?<=[.!?])\s+',text))

def comparison(d, n):
    # Esses quadros mostram instruções e critérios autorais, sem simular saídas de um modelo.
    if n == 1 or n % 3 == 2:
        return f'''<figure class="largo"><div class="tela">
<div class="tela-top"><i></i><i></i><i></i><span>Pedidos para comparar · exemplo didático</span></div>
<div class="tela-caso" data-rotulo="Pedido vago"><div class="tela-body"><p class="msg eu"><span class="quem">Pedido</span>{esc(d['antes'])}</p></div><p class="tela-nota ruim">Faltam limites observáveis para conferir o trabalho.</p></div>
<div class="tela-caso" data-rotulo="Pedido verificável"><div class="tela-body"><p class="msg eu"><span class="quem">Pedido</span>{esc(d['depois'])}</p></div><p class="tela-nota bom">Há critérios claros para conferir a decisão.</p></div>
</div><figcaption>Compare as duas instruções. São exemplos escritos para a aula, sem resposta simulada de ferramenta.</figcaption></figure>'''
    return f'''<figure class="largo"><div class="lado"><div class="antes"><span class="rot">Decisão frágil</span>{p(d['antes'])}</div><div class="depois"><span class="rot">Decisão verificável</span>{p(d['depois'])}</div></div><figcaption>Observe quais características tornam a segunda decisão conferível.</figcaption></figure>'''

def window(d):
    items=''.join(f'<div class="item doc"><span class="pin">{i}</span>{esc(x)}</div>' for i,x in enumerate(d['campos'],1))
    return f'<figure class="largo"><div class="janela"><div class="tela-top"><i></i><i></i><i></i><span>Ficha preenchida · exemplo da aula</span></div><div class="janela-body">{items}</div></div><figcaption>Use esta ficha como referência. Troque o exemplo pelo seu próprio projeto.</figcaption></figure>'

def extra_visual(n):
    return ""

def third_visual(d,n):
    return f'<figure class="largo"><img src="assets/img/aula-{n}.webp" width="1280" height="720" loading="lazy" style="width:100%;height:auto;border-radius:12px" alt="{esc(d["observacao"])}"><figcaption><b>Ilustração didática criada no Codex:</b> {esc(d["observacao"])}</figcaption></figure>'

for i,d in enumerate(lessons,1):
    m=base['modules'][(i-1)//3]
    start=((i-1)%3)*2
    topics=m['topics'][start:start+2]
    steps=[]
    for j,t in enumerate(topics,1):
        prose=sentence_paragraphs(t['concept'])+sentence_paragraphs(t['why'])
        if i==1 and j==1:
            prose=prose.replace('Escopo', '<span class="gterm" data-def="Limite do trabalho: o que será feito agora e o que fica para depois.">Escopo</span>',1)
        example=f'<p data-ex="{"estudante de comunicação" if j==1 else "dona de cafeteria"}">{esc(d["ex"+str(j)])}</p>'
        visual=(comparison(d,i) if j==1 else window(d)) + (extra_visual(i) if j==1 else '')
        steps.append(f'<section class="step" data-kind="fundamento"><h2><span class="n">{j}</span>{esc(t["title"])}</h2>{prose}{example}{visual}</section>')
    feedback=['Essa escolha não resolve o critério principal do caso.']*3
    feedback[d['correta']]='Essa escolha atende ao problema observado e preserva o objetivo da peça.'
    options=''.join(f'<button class="opt" data-k="{chr(97+j)}" data-fb="{esc(feedback[j])}">{esc(o)}</button>' for j,o in enumerate(d['opcoes']))
    quiz=f'<div class="quiz" data-answer="{chr(97+d["correta"])}"><p class="qk">Teste-se</p><p class="q">{esc(d["q"])}</p>{options}<p class="qfb" aria-live="polite"></p></div>'
    steps.append(f'<section class="step" data-kind="pratica"><h2><span class="n">3</span>Confira a decisão pelo uso</h2>{p(d["confira"])}<p data-ex="dona de cafeteria">Helena usa a ficha para conferir: {esc(d["campos"][-1].lower())}.</p>{third_visual(d,i)}{quiz}<div class="calma"><p><span class="k">Se travou aqui, é normal</span>{esc(d["calma"])}</p></div></section>')
    checklist=''.join(f'<li><label><input type="checkbox" data-ptask="{j}"><span>{esc(x)}</span></label></li>' for j,x in enumerate(d['passos'],1))
    summary=''.join(f'<li>{esc(x)}</li>' for x in d['resumo'])
    cola=''.join(f'<li><span>{esc(x)}</span></li>' for x in d['resumo'])
    complement=''.join(f'<section class="comp-sec"><h3>{esc(t["title"])}</h3><h4>Experimente com calma</h4>{p(t["practice"])}<h4>O que observar</h4>{p(t["caution"])}</section>' for t in topics)
    complement += '<section class="comp-sec"><h3>Documentação oficial · consultada em 25/09/2026</h3><p><a href="https://kling.ai/quickstart/image-to-video-guide" target="_blank" rel="noopener">Kling: imagem para vídeo</a> · <a href="https://support.google.com/flow/answer/16353334?hl=pt-BR" target="_blank" rel="noopener">Flow: criar vídeos</a> · <a href="https://support.google.com/flow/answer/16353333?hl=pt-BR" target="_blank" rel="noopener">Flow: acesso e créditos</a> · <a href="https://www.capcut.com/help/how-to-recognise-subtitles" target="_blank" rel="noopener">CapCut: legendas</a> · <a href="https://www.capcut.com/resource/how-to-add-subtitle-in-capcut" target="_blank" rel="noopener">CapCut: importar e exportar</a></p><p>Acesse <a href="https://labs.google/flow/about" target="_blank" rel="noopener">Google Flow</a>, <a href="https://kling.ai" target="_blank" rel="noopener">Kling</a> ou <a href="https://www.capcut.com" target="_blank" rel="noopener">CapCut</a>. Recursos e custos devem ser conferidos na conta atual.</p></section>'
    # Aprofundamento usa apenas material autoral deste projeto; não publica acervo de terceiros.
    next_title=lessons[i]['titulo'] if i<len(lessons) else 'Aplique o método em um novo vídeo com um objetivo diferente.'
    next_link=f'#aula-{i+1}' if i<len(lessons) else '#trilha'
    html=f'''<section class="view" id="v-aula-{i}" data-aula="{i}" data-tempo="15min">
<div class="aula"><header class="a-hero"><p class="kicker">Módulo {(i-1)//3+1} · Aula {i} de {len(lessons)}</p><h1>{esc(d['titulo'])}</h1>
<figure class="cena"><img src="assets/img/aula-{i}.webp" width="1280" height="720" alt="Ilustração didática de planejamento visual: {esc(d['titulo'].lower())}."></figure>
<p class="promise">Você consegue {esc(d['entrega'])}.</p>{p(d.get("aviso_tempo","")) if d.get("aviso_tempo") else ""}{p(d['dor'],'why')}<div class="em1min"><p class="k">Em 1 minuto</p><ol>{summary}</ol></div></header>
{''.join(steps)}
<section class="practice" data-mode="tarefa"><p class="pk">Pratique agora <span class="pcount">0/3</span></p><h3 class="ph">{esc(d['tarefa'])}</h3><p class="pgoal">{esc(d["tempo_pratica"])} Pronto quando {esc(d['pronto'])}.</p>
<p class="psafe">Use arquivos próprios ou autorizados. Geração pode exigir conta e créditos. Mantenha atividades não executadas como pendentes e preserve os originais.</p>
<div class="pcodewrap"><button class="pcopy" type="button">copiar ficha</button><pre class="pcode">{esc(d['molde'])}</pre></div><ol class="psteps">{checklist}</ol><p class="pdone">Ao cumprir os passos, você consegue {esc(d['entrega'])}.</p></section>
<div class="fecho"><div class="cola"><p class="k">Cola da aula</p><h3>{esc(d['titulo'])}</h3><ol>{cola}</ol></div><div class="next-action"><p class="nak">Seu próximo passo</p><p class="na-win">Você já tem critérios para {esc(d['entrega'])}.</p><p class="na-action">Guarde a entrega desta aula na pasta do projeto. Ela será usada na etapa seguinte.</p><p class="na-hook">Próximo passo: {esc(next_title)}</p></div></div>
<details class="complementar"><summary>{esc(d.get("complemento", "Material complementar"))} · módulo {(i-1)//3+1}<small>Produção e cuidados para retomar depois da prática curta.</small></summary>{complement}</details>
<nav class="lnav"><a href="#trilha">trilha</a><a class="next" href="{next_link}">{'próxima aula' if i<len(lessons) else 'rever a trilha'}</a></nav><p class="aula-pe">Aula {i} · Primeiro Vídeo IA v6.2 · INEMA.CLUB PRO</p></div>
<script type="application/json" id="cards-{i}">{json.dumps([{'front':a,'back':b} for a,b in d['cartoes']],ensure_ascii=False)}</script></section>'''
    (ROOT/f'aulas/aula-{i}.html').write_text(html)

cfg={'id':'primeiro-video-ia-v62','titulo':'Seu Primeiro Vídeo com IA em 24 Horas v6.2','titulo_html':'Seu primeiro <em>vídeo com IA</em>','curso_curto':'Vídeo IA v6.2','kicker':'Primeiro Vídeo IA v6.2 · 4 módulos · 12 aulas','lead':'Planeje quatro cenas, gere movimentos simples e monte um vídeo curto com voz e legendas. Um desafio para organizar sua primeira produção.','imagem_trilha':'assets/img/trilha.webp','alt_trilha':'Dona de cafeteria e estudante planejam um vídeo com cartões sobre uma mesa.','rodape':'Primeiro Vídeo IA v6.2 · INEMA.CLUB PRO · <a href="landing.html">sobre o curso</a>','landing':'landing.html','glossario':True,'modulos':[{'titulo':f'Módulo {i} · '+m['title'],'resumo':m['promise'],'aulas':list(range((i-1)*3+1,i*3+1))} for i,m in enumerate(base['modules'],1)]}
(ROOT/'curso.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n')
subprocess.run([sys.executable,str(SKILL/'scripts/montar-curso.py'),str(ROOT)],check=True)
