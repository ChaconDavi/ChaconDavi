<img src="https://raw.githubusercontent.com/ChaconDavi/ChaconDavi/master/banner.svg?v=2" width="100%" alt="Davi Chacon — desenvolvedor full-stack">

<p align="center">
  <a href="https://www.linkedin.com/in/davi-chacon-5123b018a/"><img src="https://img.shields.io/badge/LINKEDIN-7C3AED?style=for-the-badge&labelColor=7C3AED" alt="LinkedIn"></a>
  <a href="mailto:davichacon784@gmail.com"><img src="https://img.shields.io/badge/E--MAIL-5B21B6?style=for-the-badge&labelColor=5B21B6" alt="E-mail"></a>
</p>

## Experiência

| Onde | O que sustento lá |
|:--|:--|
| **Plataforma de gestão** — multi-perfil, em produção<br><img src="https://img.shields.io/badge/PHP-7C3AED?style=flat-square&logo=php&logoColor=white" alt="PHP"> <img src="https://img.shields.io/badge/MySQL-7C3AED?style=flat-square&logo=mysql&logoColor=white" alt="MySQL"> <img src="https://img.shields.io/badge/JS-7C3AED?style=flat-square&logo=javascript&logoColor=white" alt="JS"> <img src="https://img.shields.io/badge/HTML-7C3AED?style=flat-square&logo=html5&logoColor=white" alt="HTML"> <img src="https://img.shields.io/badge/CSS-7C3AED?style=flat-square&logo=css&logoColor=white" alt="CSS"> | Server-rendered: do `SELECT` ao `<select>` no mesmo arquivo. Permissão por perfil, relatório, e **migrations escritas à mão e versionadas por data** |
| **Marketplace** — app, web e API<br><img src="https://img.shields.io/badge/TypeScript-6D28D9?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript"> <img src="https://img.shields.io/badge/Expo-6D28D9?style=flat-square&logo=expo&logoColor=white" alt="Expo"> <img src="https://img.shields.io/badge/Next.js-6D28D9?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js"> <img src="https://img.shields.io/badge/Postgres-6D28D9?style=flat-square&logo=postgresql&logoColor=white" alt="Postgres"> | PIX e cartão em checkout transparente, entrega por motoboy via Uber Direct, e **comissão congelada na venda** para relatório antigo não ser reescrito |
| **Cloud Humans** — atendimento com IA<br><img src="https://img.shields.io/badge/Ruby-5B21B6?style=flat-square&logo=ruby&logoColor=white" alt="Ruby"> <img src="https://img.shields.io/badge/Kotlin-5B21B6?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin"> <img src="https://img.shields.io/badge/Java-5B21B6?style=flat-square&logo=openjdk&logoColor=white" alt="Java"> <img src="https://img.shields.io/badge/K8s-5B21B6?style=flat-square&logo=kubernetes&logoColor=white" alt="K8s"> | **Integração nativa** entre o agente de IA e a plataforma omnichannel — fazer os dois produtos da empresa virarem um |
| **Em construção** — com o time<br><img src="https://img.shields.io/badge/Python-8B5CF6?style=flat-square&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/TypeScript-8B5CF6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript"> <img src="https://img.shields.io/badge/Postgres-8B5CF6?style=flat-square&logo=postgresql&logoColor=white" alt="Postgres"> | SaaS de cobrança recorrente, e plataforma de ingressos com check-in por QR Code |

<a href="https://github.com/cloudhumans/typebot.io/pull/132">
  <img src="https://img.shields.io/badge/PR_%23132_na_Cloud_Humans-merged_%7C_%2B2.463_linhas_em_57_arquivos-5B21B6?style=for-the-badge&labelColor=2E1065&logo=github&logoColor=white" alt="PR #132 na Cloud Humans">
</a>

<details>
<summary><b>O que tem dentro de cada uma</b></summary>

<br>

**Marketplace** — monorepo de quatro pacotes: app Expo, web Next, API Express e uma
camada compartilhada de regra de negócio, para o app e o site nunca divergirem no
que cobram.

- Pagamento com PIX (QR) e cartão, com estorno e conciliação contra o gateway
  quando o webhook não chega — porque `status_pago` no meu banco não é verdade
  sobre dinheiro se o webhook falhou calado
- A loja escolhe entre entrega própria e app, e o frete segue quem de fato entregou
- Comissão congelada em coluna própria: baixar o percentual de uma parceira não
  pode mudar o lucro dos pedidos antigos dela
- CI com testes de integração contra um Postgres de verdade, porque a regra que
  importa mora no SQL

**Cloud Humans** — features nos dois produtos: **ClaudIA**, agente de IA que
resolve atendimento sozinho, e **CloudChat**, a plataforma omnichannel de WhatsApp,
chat, e-mail e redes. No [PR #132](https://github.com/cloudhumans/typebot.io/pull/132),
público: blocos novos no construtor de fluxo (variáveis nativas, validação de CPF e
CNPJ, bloco de nota com editor próprio), busca dentro do fluxo — o que salva quando
o bot passa de algumas centenas de nós — e o pipeline de CI/CD com migração por
matriz, imagem Docker e deploy em Kubernetes.

**Também:** app mobile com Angular, Ionic e Capacitor, com build Android gerado.

</details>

## Projetos públicos

| Projeto | O que faz |
|:--|:--|
| [**Analisador de Currículos com IA**](https://github.com/ChaconDavi/ACV.py)<br><img src="https://img.shields.io/badge/Python-7C3AED?style=flat-square&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/Streamlit-7C3AED?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit"> <img src="https://img.shields.io/badge/Ollama-7C3AED?style=flat-square&logo=ollama&logoColor=white" alt="Ollama"> | Avalia currículo em PDF com LLM **rodando local**: sem chave de API e sem o arquivo sair da máquina |
| [**Calculadora de Preço**](https://github.com/ChaconDavi/MDCalculator)<br><img src="https://img.shields.io/badge/JavaScript-6D28D9?style=flat-square&logo=javascript&logoColor=white" alt="JavaScript"> <img src="https://img.shields.io/badge/HTML-6D28D9?style=flat-square&logo=html5&logoColor=white" alt="HTML"> <img src="https://img.shields.io/badge/CSS-6D28D9?style=flat-square&logo=css&logoColor=white" alt="CSS"> | Margem por faixa de custo, histórico no navegador e exportação em PDF |

## Stack

<img src="https://img.shields.io/badge/PHP-5B21B6?style=flat-square&logo=php&logoColor=white" alt="PHP"> <img src="https://img.shields.io/badge/TypeScript-5B21B6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript"> <img src="https://img.shields.io/badge/JavaScript-5B21B6?style=flat-square&logo=javascript&logoColor=white" alt="JavaScript"> <img src="https://img.shields.io/badge/SQL-5B21B6?style=flat-square&logo=mysql&logoColor=white" alt="SQL"> <img src="https://img.shields.io/badge/HTML-5B21B6?style=flat-square&logo=html5&logoColor=white" alt="HTML"> <img src="https://img.shields.io/badge/CSS-5B21B6?style=flat-square&logo=css&logoColor=white" alt="CSS"> <img src="https://img.shields.io/badge/Sass-5B21B6?style=flat-square&logo=sass&logoColor=white" alt="Sass"> <img src="https://img.shields.io/badge/Ruby-5B21B6?style=flat-square&logo=ruby&logoColor=white" alt="Ruby"> <img src="https://img.shields.io/badge/Kotlin-5B21B6?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin"> <img src="https://img.shields.io/badge/Java-5B21B6?style=flat-square&logo=openjdk&logoColor=white" alt="Java"> <img src="https://img.shields.io/badge/Python-5B21B6?style=flat-square&logo=python&logoColor=white" alt="Python">

<img src="https://img.shields.io/badge/React-6D28D9?style=flat-square&logo=react&logoColor=white" alt="React"> <img src="https://img.shields.io/badge/React_Native-6D28D9?style=flat-square&logo=expo&logoColor=white" alt="React_Native"> <img src="https://img.shields.io/badge/Next.js-6D28D9?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js"> <img src="https://img.shields.io/badge/Angular-6D28D9?style=flat-square&logo=angular&logoColor=white" alt="Angular"> <img src="https://img.shields.io/badge/Ionic-6D28D9?style=flat-square&logo=ionic&logoColor=white" alt="Ionic"> <img src="https://img.shields.io/badge/Capacitor-6D28D9?style=flat-square&logo=capacitor&logoColor=white" alt="Capacitor">

<img src="https://img.shields.io/badge/Node.js-7C3AED?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node.js"> <img src="https://img.shields.io/badge/Express-7C3AED?style=flat-square&logo=express&logoColor=white" alt="Express"> <img src="https://img.shields.io/badge/MySQL-7C3AED?style=flat-square&logo=mysql&logoColor=white" alt="MySQL"> <img src="https://img.shields.io/badge/PostgreSQL-7C3AED?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL">

<img src="https://img.shields.io/badge/Docker-8B5CF6?style=flat-square&logo=docker&logoColor=white" alt="Docker"> <img src="https://img.shields.io/badge/Kubernetes-8B5CF6?style=flat-square&logo=kubernetes&logoColor=white" alt="Kubernetes"> <img src="https://img.shields.io/badge/GitHub_Actions-8B5CF6?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub_Actions"> <img src="https://img.shields.io/badge/Linux-8B5CF6?style=flat-square&logo=linux&logoColor=white" alt="Linux"> <img src="https://img.shields.io/badge/Git-8B5CF6?style=flat-square&logo=git&logoColor=white" alt="Git">
