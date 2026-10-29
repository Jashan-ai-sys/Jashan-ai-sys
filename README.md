<p align="center">
  <img src="assets/hero.svg" alt="Jashanprit Singh, AI Engineer. A live phone call card: the customer says the payment failed, the agent replies in Hindi within about a second and sends a payment link." width="100%"/>
</p>

<p align="center">
  <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=18&duration=2600&pause=900&color=3987E5&center=true&vCenter=true&width=600&lines=AI+Engineer;Voice+agents+on+real+phone+calls;Multi-agent+systems+with+MCP;LLM+inference+%26+routing;Hackathon+builder%2C+production+shipper" alt="Typing summary"/></a>
</p>

<p align="center">
  <a href="https://jashan-ai-sys.github.io/"><img src="https://img.shields.io/badge/Portfolio-jashan--ai--sys.github.io-0d1117?style=flat-square&logo=githubpages&logoColor=white"/></a>
  <a href="https://www.linkedin.com/in/jashanprit-singh-"><img src="https://img.shields.io/badge/LinkedIn-jashanprit--singh-0A66C2?style=flat-square&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:singhjashanprit86@gmail.com"><img src="https://img.shields.io/badge/Email-singhjashanprit86%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white"/></a>
</p>

---

<p align="center">
  <img src="assets/terminal.svg" alt="whoami: Jashanprit Singh, AI Engineer, B.Tech CSE 2027. Focus: voice agents on real phone calls, multi-agent systems with MCP, LLM inference. Shipped: dunning-agent, inference-gateway, shopwave-agents, sales-call-intel, pharmaconnect, agentic-honeypot." width="100%"/>
</p>

<p align="center">🌐 <b>Portfolio:</b> <a href="https://jashan-ai-sys.github.io/">jashan-ai-sys.github.io</a>: case studies and how to hire me for AI voice agents, chatbots and automation</p>

---

## 🚀 Featured projects

<table>
<tr>
<td width="50%" valign="top">

### 📞 [Dunning Agent](https://github.com/Jashan-ai-sys/dunning-agent)
**Voice AI for revenue recovery** · Razorpay AI Buildathon

Detects failed subscription payments and **calls customers in Hindi** over Twilio. During the call it can send a payment link or re-authorise a mandate. It runs live on Cloud Run, with **~1.13 s** from the moment the customer stops speaking to the agent's reply.

`Pipecat` `Twilio` `Gemini` `MCP` `Cloud Run`

</td>
<td width="50%" valign="top">

### ⚡ [Inference Gateway](https://github.com/Jashan-ai-sys/inference-gateway)
**LLM routing + scheduling** · in progress

An OpenAI-compatible gateway in front of vLLM and hosted APIs. Its router picks the backend from cost, quality and predicted latency, and its scheduler orders requests by deadline, tenant fairness and KV-cache headroom. A benchmark on an L4 GPU is in progress.

`vLLM` `FastAPI` `Prometheus` `Terraform` `AWS`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🛒 [ShopWave Multi-Agent Support](https://github.com/Jashan-ai-sys/ShopWave-MultiAgent-Customer-Support-System)
**Agentic customer support** · Ksolves Agentic AI Hackathon

A self-correcting pipeline that runs risk analysis, then a planner, a validator, an MCP executor and a responder, with a reflection loop when a tool fails and a dead-letter queue.

`Gemini` `MCP` `Python`

</td>
<td width="50%" valign="top">

### 🧠 [AI Sales Call Intelligence](https://github.com/Jashan-ai-sys/AI-Sales-Call-Intelligence-System)
**Speech → insights**

Turns a call recording into a transcript, extracts intent, sentiment and objections, flags "magic moments", writes LLM coaching and runs a RAG search over past calls.

`Whisper` `spaCy` `Llama 3.3` `ChromaDB`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 💊 [PharmaConnect](https://github.com/Jashan-ai-sys/pharmaconnect-prototype)
**Pharmacy platform** · Centific Hackathon

A POS with role-based access, FEFO stock depletion and atomic billing. When a drug is out of stock, an AI engine suggests a substitute for the pharmacist to approve.

`FastAPI` `SQLAlchemy` `JWT`

</td>
<td width="50%" valign="top">

### 🍯 [Agentic Honey-Pot](https://github.com/Jashan-ai-sys/Agentic-Honey-Pot-for-Scam-Detection-Intelligence-Extraction)
**Scam intelligence** · GUVI Hackathon

A persona agent that keeps scammers talking and extracts their UPI IDs, URLs and phone numbers for reporting.

`FastAPI` `LLM agents`

</td>
</tr>
</table>

<details>
<summary><b>More repos</b></summary>
<br/>

| Project | What it is |
|---|---|
| [Portfolio](https://github.com/Jashan-ai-sys/Jashan-ai-sys.github.io) | My freelance site for AI voice agents, chatbots and automation (React, Tailwind, three.js) |
| [LeetCode → GitHub](https://github.com/Jashan-ai-sys/LeetCode-to-GitHub-Automation) | Syncs my accepted LeetCode submissions to GitHub, sorted by difficulty |
| [Telecom Revenue Analysis](https://github.com/Jashan-ai-sys/Telecom-Customer-Billing-and-Revenue-Analysis) | Revenue drivers, service bundling, hypothesis tests and outliers (Pandas, SciPy, statsmodels) |

</details>

---

## 🔍 Deep dives

<details>
<summary><b>📞 Dunning Agent: where the 1.13 s goes</b></summary>
<br/>
<p align="center">
  <img src="assets/voice-latency.svg" alt="Per-stage p50 latency: STT first byte 0.396 s, turn detection 0.173 s, LLM first token 0.553 s, TTS first audio 0.209 s; about 1.13 s from customer silence to agent reply" width="100%"/>
</p>

- **The model can't invent an outcome.** The conversation is a graph. The LLM picks an edge label, and the code refuses any label that isn't legal at the current node.
- **The agent can't name a case.** Its MCP tools take no arguments, and the code injects the case where the model can't reach it.
- **Nobody is called twice about the same debt.** This is enforced with `FOR UPDATE SKIP LOCKED` and a concurrency test.

</details>

<details>
<summary><b>⚡ Inference Gateway: how a request is placed</b></summary>
<br/>

```mermaid
flowchart LR
    C([Client<br/>OpenAI API]) --> A[Analyzer<br/>tokens · class · deadline]
    A --> R{Model Router<br/>filter → predict TTFT → rank}
    R -->|chosen backend| S[Workload Scheduler<br/>class queues · VTC fairness<br/>aging · KV admission]
    S -. "queue_wait(b, class)" .-> R
    S --> D[Dispatcher<br/>streaming · backpressure<br/>circuit breaker]
    D --> G1[(vLLM<br/>Qwen3-1.7B)]
    D --> G2[(vLLM<br/>Qwen3-8B-AWQ)]
    D --> H[(Hosted<br/>Groq · Gemini)]
    G1 & G2 -. "/metrics every 1 s" .-> T[Telemetry<br/>TTFT / TPOT EWMAs]
    T -.-> R
```

The router reads the scheduler's predicted queue wait. When an interactive request would miss its deadline on the local GPU, it overflows to a hosted API. The gateway core is merged with 133 tests. The benchmark compares six places scheduling could live, from FIFO passthrough to vLLM-native priority to separate replica pools, and its results will be published with confidence intervals.

</details>

---

## 🛠️ Tech stack

**AI & LLMs**<br/>
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"/>
<img src="https://img.shields.io/badge/Hugging%20Face-FFCC00?style=for-the-badge&logo=huggingface&logoColor=black"/>
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white"/>
<img src="https://img.shields.io/badge/LlamaIndex-0d1117?style=for-the-badge"/>
<img src="https://img.shields.io/badge/MCP-0d1117?style=for-the-badge"/>
<img src="https://img.shields.io/badge/RAG-FF5733?style=for-the-badge"/>
<img src="https://img.shields.io/badge/vLLM-0d1117?style=for-the-badge"/>
<img src="https://img.shields.io/badge/FAISS-0467DF?style=for-the-badge"/>

**Voice AI**<br/>
<img src="https://img.shields.io/badge/Pipecat-0d1117?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Twilio-F22F46?style=for-the-badge&logo=twilio&logoColor=white"/>
<img src="https://img.shields.io/badge/Whisper-412991?style=for-the-badge"/>
<img src="https://img.shields.io/badge/STT%20%C2%B7%20TTS%20%C2%B7%20VAD-0d1117?style=for-the-badge"/>

**Backend**<br/>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>
<img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white"/>
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white"/>

**Cloud & ops**<br/>
<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Bedrock-232F3E?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white"/>
<img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white"/>
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white"/>

**ML & data**<br/>
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"/>
<img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>

---

## 📈 GitHub activity

<p align="center">
  <img src="https://streak-stats.demolab.com?user=Jashan-ai-sys&theme=github-dark-blue&hide_border=true&border_radius=12" alt="GitHub streak" height="170"/>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Jashan-ai-sys/Jashan-ai-sys/output/snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Jashan-ai-sys/Jashan-ai-sys/output/snake.svg"/>
  <img alt="A snake eating my contribution graph" src="https://raw.githubusercontent.com/Jashan-ai-sys/Jashan-ai-sys/output/snake-dark.svg" width="100%"/>
</picture>

---

<p align="center">
  <b>Let's build something.</b><br/><br/>
  <a href="https://jashan-ai-sys.github.io/"><img src="https://img.shields.io/badge/Visit%20my%20portfolio-jashan--ai--sys.github.io-3987e5?style=for-the-badge&logo=githubpages&logoColor=white"/></a>
  <a href="https://www.linkedin.com/in/jashanprit-singh-"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:singhjashanprit86@gmail.com"><img src="https://img.shields.io/badge/Email-Say%20hi-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>
