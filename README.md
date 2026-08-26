<h1 align="center">Davi Chacon</h1>

<p align="center">
  <strong>Desenvolvedor full-stack</strong><br>
  Sistemas em produção, com gente dependendo deles
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/davi-chacon-5123b018a/">
    <img src="https://img.shields.io/badge/LINKEDIN-7C3AED?style=for-the-badge&labelColor=7C3AED" alt="LinkedIn">
  </a>
  <a href="mailto:davichacon784@gmail.com">
    <img src="https://img.shields.io/badge/E--MAIL-5B21B6?style=for-the-badge&labelColor=5B21B6" alt="E-mail">
  </a>
</p>

<p align="center">
<img src="https://img.shields.io/badge/PHP-6D28D9?style=flat-square&logo=php&logoColor=white" alt="PHP">
<img src="https://img.shields.io/badge/TypeScript-6D28D9?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
<img src="https://img.shields.io/badge/Ruby-6D28D9?style=flat-square&logo=ruby&logoColor=white" alt="Ruby">
<img src="https://img.shields.io/badge/Kotlin-6D28D9?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin">
<img src="https://img.shields.io/badge/Java-6D28D9?style=flat-square&logo=openjdk&logoColor=white" alt="Java">
<img src="https://img.shields.io/badge/Python-6D28D9?style=flat-square&logo=python&logoColor=white" alt="Python">
</p>

---

Trabalho em sistemas que já têm gente dependendo deles: plataforma de gestão com
anos de histórico, marketplace com pagamento e entrega no ar, plataforma de
atendimento com IA. O que me interessa é o problema que sobra depois do "funciona
na minha máquina" — regra de negócio que ninguém documentou, dado inconsistente
em produção, mudança que precisa entrar sem janela de manutenção.

## 💼 Experiência

### Plataforma de gestão multi-perfil

<img src="https://img.shields.io/badge/PHP-7C3AED?style=flat-square&logo=php&logoColor=white" alt="PHP">
<img src="https://img.shields.io/badge/MySQL-7C3AED?style=flat-square&logo=mysql&logoColor=white" alt="MySQL">
<img src="https://img.shields.io/badge/JavaScript-7C3AED?style=flat-square&logo=javascript&logoColor=white" alt="JavaScript">
<img src="https://img.shields.io/badge/HTML-7C3AED?style=flat-square&logo=html5&logoColor=white" alt="HTML">
<img src="https://img.shields.io/badge/CSS-7C3AED?style=flat-square&logo=css&logoColor=white" alt="CSS">

Sistema em produção com perfis distintos para profissional, empresa, corretora e
unidade, mantido por um time de seis pessoas — é onde está a maior parte do meu
volume de código.

É server-rendered: o mesmo arquivo PHP carrega a consulta, a marcação, o estilo e
o comportamento, então o trabalho vai de `SELECT` a `<select>` no mesmo dia. Atuo
em cadastro, permissão por perfil, relatório, integração entre módulos e nas
**migrations de banco, escritas à mão e versionadas por data**.

### Marketplace com entrega rápida

<img src="https://img.shields.io/badge/TypeScript-7C3AED?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
<img src="https://img.shields.io/badge/React_Native-7C3AED?style=flat-square&logo=expo&logoColor=white" alt="React_Native">
<img src="https://img.shields.io/badge/Next.js-7C3AED?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js">
<img src="https://img.shields.io/badge/Node.js-7C3AED?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node.js">
<img src="https://img.shields.io/badge/Express-7C3AED?style=flat-square&logo=express&logoColor=white" alt="Express">
<img src="https://img.shields.io/badge/PostgreSQL-7C3AED?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL">
<img src="https://img.shields.io/badge/PIX-7C3AED?style=flat-square&logo=pix&logoColor=white" alt="PIX">
<img src="https://img.shields.io/badge/Uber_Direct-7C3AED?style=flat-square&logo=uber&logoColor=white" alt="Uber_Direct">

Monorepo de quatro pacotes — app Expo, web Next, API Express e uma camada
compartilhada de regra de negócio, para o app e o site nunca divergirem no que
cobram ou no que mostram. O que construí ali:

- **Pagamento** com PIX (QR) e cartão em checkout transparente, incluindo estorno
  e conciliação contra o gateway quando o webhook não chega — porque `status_pago`
  no meu banco não é verdade sobre dinheiro se o webhook falhou calado
- **Entrega por motoboy** integrada à Uber Direct, com a loja escolhendo entre
  entrega própria e app, e o frete seguindo quem de fato entregou
- **Comissão congelada na venda**, e não lida da configuração atual: baixar o
  percentual de uma parceira não pode reescrever o lucro dos pedidos antigos dela
- **CI** rodando testes de integração contra um Postgres de verdade, porque a
  regra que importa mora no SQL

### Atendimento com IA — Cloud Humans

<img src="https://img.shields.io/badge/Ruby-7C3AED?style=flat-square&logo=ruby&logoColor=white" alt="Ruby">
<img src="https://img.shields.io/badge/Kotlin-7C3AED?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin">
<img src="https://img.shields.io/badge/Java-7C3AED?style=flat-square&logo=openjdk&logoColor=white" alt="Java">
<img src="https://img.shields.io/badge/TypeScript-7C3AED?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
<img src="https://img.shields.io/badge/Kubernetes-7C3AED?style=flat-square&logo=kubernetes&logoColor=white" alt="Kubernetes">

Features nos dois produtos da empresa: **ClaudIA**, agente de IA que resolve
atendimento de forma autônoma, e **CloudChat**, a plataforma omnichannel de
WhatsApp, chat, e-mail e redes.

A entrega que considero minha melhor foi a **integração nativa entre os dois** —
fazer o agente de IA operar dentro da plataforma de atendimento como parte dela,
e não como bot externo pendurado por fora.

Parte do trabalho é pública, no construtor de fluxo:

<a href="https://github.com/cloudhumans/typebot.io/pull/132">
  <img src="https://img.shields.io/badge/PR_%23132-merged_%7C_%2B2.463_linhas_em_57_arquivos-5B21B6?style=for-the-badge&logo=github&logoColor=white" alt="PR #132">
</a>

Blocos novos no builder (variáveis nativas, validação de CPF e CNPJ, bloco de nota
com editor próprio), busca dentro do fluxo — que é o que salva quando o bot passa
de algumas centenas de nós — e o pipeline de CI/CD: migração de banco por matriz,
build de imagem Docker e deploy em Kubernetes.

### Em construção

<img src="https://img.shields.io/badge/Python-7C3AED?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/TypeScript-7C3AED?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
<img src="https://img.shields.io/badge/PostgreSQL-7C3AED?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL">

Dois produtos em desenvolvimento agora, em que participo junto com o time:

- **SaaS de cobrança recorrente** — o usuário informa quem deve, quanto e quando
  vence; a plataforma acompanha a cobrança, gera o pagamento, envia lembrete e
  identifica automaticamente a entrada do dinheiro
- **Plataforma de ingressos e check-in** — venda por lote, pagamento confirmado no
  back-end, ingresso emitido com QR Code único, validação na portaria e registro
  para auditoria

**Também:** app mobile com Angular, Ionic e Capacitor, com build Android gerado.

---

## 🚀 Projetos públicos

### [Analisador de Currículos com IA](https://github.com/ChaconDavi/ACV.py)

<img src="https://img.shields.io/badge/Python-7C3AED?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Streamlit-7C3AED?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit">
<img src="https://img.shields.io/badge/Ollama-7C3AED?style=flat-square&logo=ollama&logoColor=white" alt="Ollama">

Avaliação de currículo em PDF por LLM **rodando local** — sem chave de API e sem o
arquivo sair da máquina, o que importa quando o PDF tem nome, telefone e endereço
de alguém. Extrai o texto com PyMuPDF, monta um prompt de recrutador para o
Mistral via Ollama e devolve o feedback em PDF.

### [Calculadora de Preço — MD Móveis](https://github.com/ChaconDavi/MDCalculator)

<img src="https://img.shields.io/badge/JavaScript-7C3AED?style=flat-square&logo=javascript&logoColor=white" alt="JavaScript">
<img src="https://img.shields.io/badge/HTML-7C3AED?style=flat-square&logo=html5&logoColor=white" alt="HTML">
<img src="https://img.shields.io/badge/CSS-7C3AED?style=flat-square&logo=css&logoColor=white" alt="CSS">

Precificação por faixa de custo para uma loja de móveis: margem que cai conforme o
ticket sobe, histórico nomeado no navegador, exportação em PDF e tema escuro.

---

## 🧰 Stack

**Linguagens**

<img src="https://img.shields.io/badge/PHP-5B21B6?style=flat-square&logo=php&logoColor=white" alt="PHP">
<img src="https://img.shields.io/badge/TypeScript-5B21B6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
<img src="https://img.shields.io/badge/JavaScript-5B21B6?style=flat-square&logo=javascript&logoColor=white" alt="JavaScript">
<img src="https://img.shields.io/badge/SQL-5B21B6?style=flat-square&logo=mysql&logoColor=white" alt="SQL">
<img src="https://img.shields.io/badge/HTML-5B21B6?style=flat-square&logo=html5&logoColor=white" alt="HTML">
<img src="https://img.shields.io/badge/CSS-5B21B6?style=flat-square&logo=css&logoColor=white" alt="CSS">
<img src="https://img.shields.io/badge/Sass-5B21B6?style=flat-square&logo=sass&logoColor=white" alt="Sass">
<img src="https://img.shields.io/badge/Ruby-5B21B6?style=flat-square&logo=ruby&logoColor=white" alt="Ruby">
<img src="https://img.shields.io/badge/Kotlin-5B21B6?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin">
<img src="https://img.shields.io/badge/Java-5B21B6?style=flat-square&logo=openjdk&logoColor=white" alt="Java">
<img src="https://img.shields.io/badge/Python-5B21B6?style=flat-square&logo=python&logoColor=white" alt="Python">

**Front-end**

<img src="https://img.shields.io/badge/React-6D28D9?style=flat-square&logo=react&logoColor=white" alt="React">
<img src="https://img.shields.io/badge/React_Native-6D28D9?style=flat-square&logo=expo&logoColor=white" alt="React_Native">
<img src="https://img.shields.io/badge/Next.js-6D28D9?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js">
<img src="https://img.shields.io/badge/Angular-6D28D9?style=flat-square&logo=angular&logoColor=white" alt="Angular">
<img src="https://img.shields.io/badge/Ionic-6D28D9?style=flat-square&logo=ionic&logoColor=white" alt="Ionic">
<img src="https://img.shields.io/badge/Capacitor-6D28D9?style=flat-square&logo=capacitor&logoColor=white" alt="Capacitor">

**Back-end e dados**

<img src="https://img.shields.io/badge/Node.js-7C3AED?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node.js">
<img src="https://img.shields.io/badge/Express-7C3AED?style=flat-square&logo=express&logoColor=white" alt="Express">
<img src="https://img.shields.io/badge/MySQL-7C3AED?style=flat-square&logo=mysql&logoColor=white" alt="MySQL">
<img src="https://img.shields.io/badge/PostgreSQL-7C3AED?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL">

**Infra**

<img src="https://img.shields.io/badge/Docker-8B5CF6?style=flat-square&logo=docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/Kubernetes-8B5CF6?style=flat-square&logo=kubernetes&logoColor=white" alt="Kubernetes">
<img src="https://img.shields.io/badge/GitHub_Actions-8B5CF6?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub_Actions">
<img src="https://img.shields.io/badge/Linux-8B5CF6?style=flat-square&logo=linux&logoColor=white" alt="Linux">
<img src="https://img.shields.io/badge/Git-8B5CF6?style=flat-square&logo=git&logoColor=white" alt="Git">
