# Seu Primeiro Vídeo com IA em 24 Horas v6.2

Curso aberto e gratuito com quatro módulos e 12 aulas.
[Abra o curso](https://inematds.github.io/curso-primeiro-video-ia/).

Caso autoral Ponto da Pausa: roteiro, quatro cenas, movimento, revisão, montagem, voz, legendas e entrega.
O desafio de 24 horas organiza o escopo; acesso, créditos e filas podem exigir mais tempo. Reserve 4–6 horas com a produção.
As aulas usam ilustrações Codex image_gen. Não apresentam imagens paradas como resultados Kling/Flow nem incluem vídeos de demonstração desses modelos.
As atividades de geração exigem ferramenta compatível e só são concluídas com arquivo real conferido.

## Arquivos

`context/conteudo-base.json` e `context/aulas-editoriais.json` são as fontes autorais.
`python3 montar.py` gera as aulas usando o motor oficial INEMA v6. O caminho da skill está em SKILL no script.
`assets/aula.css` e `assets/curso.js` são cópias sem alterações do motor.
Fontes oficiais, inventário de imagens, auditoria e leitores simulados ficam em `context/`.
Não houve teste com alunos reais nem geração de vídeos Kling/Flow durante a autoria.

## INEMA.CLUB

- [Ficha](https://www.inema.club/cursos/290-seu-primeiro-video-com-ia-em-24-horas-v6-2/)
- [Como aprender IA](https://www.inema.club/aprender-inteligencia-artificial/)
- [Catálogo](https://www.inema.club/cursos/)

## English / Español

[English](https://inematds.github.io/curso-primeiro-video-ia/en/) · [Español](https://inematds.github.io/curso-primeiro-video-ia/es/)

Textos traduzidos com GPT-6 Luna por subagentes nativos da assinatura Codex, sem API externa. Ilustrações originais compartilhadas; progresso e anotações separados por idioma.

Após montar o português, reaplique os catálogos salvos:

```sh
python3 scripts/i18n_local.py build .
python3 scripts/verify_i18n.py .
node scripts/check_i18n_browser.cjs . /tmp/curso-i18n-checks
```

Requer Python/BeautifulSoup e os pacotes locais Babel/Playwright indicados nos scripts. A montagem não chama modelos nem redes. Mudanças na fonte PT exigem revisar os catálogos `i18n/`. O motor oficial `assets/curso.js` é preservado; a proteção de importação é gerada em `assets/curso-i18n.js` e nas edições traduzidas.

Evidências em `context/validacao-i18n.md`. Revisões por agentes são simuladas, não testes com alunos reais.
