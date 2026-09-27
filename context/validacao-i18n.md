# Validação EN/ES — 2026-09-27

Conteúdo 1.1.1; formato OSWork v6.2 preservado.
- EN: 12/12 aulas aprovadas; média 10/10. Ver auditoria-en.json.
- ES: 12/12 aulas aprovadas; média 9.916666666666666/10. Ver auditoria-es.json.
- Auditor adaptado ao idioma EN: download/upload/login/backup/setup/input/output/script são vocabulário nativo, não empréstimos ingleses no português. Sentinelas técnicas (API, CLI, JSON, Git, terminal etc.) e demais critérios permanecem ativos. A adaptação é local ao verificador; a skill global não foi alterada.
- Motor: 26/26 comportamentos em PT, EN e ES; logs i18n-motor-*.log.
- Estrutura, links, IDs, respostas de quiz, arquivos locais e sintaxe JS verificados.
- Navegador: todas as aulas em celular, imagens, troca de idioma preservando a aula, exportação/importação e rejeição de outra edição; nenhum erro JS.
- Planejadores interativos, quando presentes: campos de estado, persistência e exportação/importação por edição testados.
- Revisão textual simulada nos relatórios revisao-i18n-*.md. Não houve teste com alunos externos.
- Todos os testes de navegador bloquearam HTTP externo; fontes de fallback locais. Nenhuma API de tradução usada.
- Capturas locais: /home/nmaldaner/projetos/output/cursos-v62-traducao/curso-primeiro-video-ia. A inspeção visual é registrada separadamente após abrir as capturas.

Inspeção visual: ES aula12 no celular e EN aula6 no desktop escuro abertas e conferidas; texto, imagens e práticas legíveis, sem cortes. A adaptação do auditor foi verificada em fixtures: PT continua reprovando script, EN continua reprovando API sem definição.
