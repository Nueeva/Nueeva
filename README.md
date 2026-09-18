<div align="center">

<img src="./ascii.svg" width="620" alt="NUEVA — Rifqi Ariansyah"/>

<img src="./stats.svg" width="620" alt="Contributions in the last year"/>

[portfolio](https://nueva.my.id) &nbsp;·&nbsp;
[blog](https://blog.nueva.my.id) &nbsp;·&nbsp;
[resume](https://nueva.my.id/resume) &nbsp;·&nbsp;
[xssscope](https://github.com/Nueeva/xssscope) &nbsp;·&nbsp;
[ctf-toolkit](https://github.com/Nueeva/CTF-Toolkit) &nbsp;·&nbsp;
[clouvia](https://linktr.ee/die_de_nueva) &nbsp;·&nbsp;
[linkedin](https://linkedin.com/in/Nueva) &nbsp;·&nbsp;
[email](mailto:rifqiariansyah123@gmail.com)

</div>

<br/>

<img src="./hd-about.svg" width="620" alt="about"/>

> **Rifqi Ariansyah** &nbsp;·&nbsp; `Nueeva` &nbsp;·&nbsp; Cybersecurity Researcher & Systems Developer<br>
> *Identifying vulnerabilities before they become threats.* Focus: Application Security, Reflected Sinks, and Hardened Architectures.

Self-taught security researcher and software engineer with a deep passion for Web Application Pentesting, Cryptography, and Offensive Tooling.

- 🛡️ **Specialization:** Web Application Pentesting, Reflected XSS Analysis, and Defensive Code Review.
- 🔬 **Active Research:** Developing zero-dependency offensive tooling (**[xssscope](https://github.com/Nueeva/xssscope)**) and modular CTF frameworks (**[CTF-Toolkit](https://github.com/Nueeva/CTF-Toolkit)**).
- 💼 **Ecosystem:** Founder & Lead at **[Clouvia](https://linktr.ee/die_de_nueva)** (Cloud hosting & secure web infrastructure).
- 🤝 **Engagement Status:** Open for **Web Security Audits, Pentesting Collaborations, and Vulnerability Research**.
- 📬 **Direct Inquiries:** [rifqiariansyah123@gmail.com](mailto:rifqiariansyah123@gmail.com) &nbsp;·&nbsp; **Portfolio:** [nueva.my.id](https://nueva.my.id) &nbsp;·&nbsp; **Articles:** [blog.nueva.my.id](https://blog.nueva.my.id)

<br/>

<img src="./hd-projects.svg" width="620" alt="projects"/>

<div align="center">

<a href="https://github.com/Nueeva/xssscope">
  <img src="https://raw.githubusercontent.com/Nueeva/xssscope/main/assets/banner.svg" alt="xssscope banner" width="100%">
</a>

<p align="center">
  <a href="https://github.com/Nueeva/xssscope/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-3fb950.svg?style=flat-square" alt="License MIT"></a>
  <a href="https://nodejs.org"><img src="https://img.shields.io/badge/Node-%3E%3D%2018-58a6ff.svg?style=flat-square&logo=node.js&logoColor=white" alt="Node version"></a>
  <img src="https://img.shields.io/badge/Dependencies-Zero-3fb950.svg?style=flat-square" alt="Zero Dependencies">
  <img src="https://img.shields.io/badge/Type-Reflected%20XSS%20Scanner-f85149.svg?style=flat-square" alt="Reflected XSS Scanner">
  <a href="https://github.com/Nueeva/xssscope/stargazers"><img src="https://img.shields.io/github/stars/Nueeva/xssscope?style=flat-square&color=e3b341" alt="GitHub Stars"></a>
</p>

</div>

### 🔍 [xssscope](https://github.com/Nueeva/xssscope) — Reflected XSS Scanner with Context Detection
> *Zero dependencies. Probe, classify, verify.*

Most scanners fire arbitrary payload banks at every query param, causing false positives and wasted time. **xssscope** operates backwards:
1. **Probe first:** Injects an inert canary to verify if reflection actually occurs.
2. **Classify context:** Identifies the precise sink (element text, quoted/unquoted attribute, script string, or HTML comment).
3. **Targeted payload:** Dispatches only the payload crafted for that exact breakout syntax.
4. **Byte-exact verification:** Confirms execution only when returned unescaped and syntactically valid.

<div align="center">
  <a href="https://github.com/Nueeva/xssscope">
    <img src="https://raw.githubusercontent.com/Nueeva/xssscope/main/assets/demo.svg" alt="xssscope demo" width="95%">
  </a>
</div>

```bash
# Quick run (zero npm install required)
git clone https://github.com/Nueeva/xssscope.git
node xssscope/bin/cli.js --target http://localhost:8080
```

👉 **[Explore the xssscope Repository & Documentation →](https://github.com/Nueeva/xssscope)**

---

### 🛡️ [CTF-Toolkit](https://github.com/Nueeva/CTF-Toolkit) — Modular Terminal Framework for Security Labs

<p align="left">
  <a href="https://github.com/Nueeva/CTF-Toolkit"><img src="https://img.shields.io/badge/Python-3.10%2B-0d1117.svg?style=flat-square&logo=python&logoColor=3776AB" alt="Python 3.10+"></a>
  <a href="https://github.com/Nueeva/CTF-Toolkit/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-0d1117.svg?style=flat-square&logoColor=3fb950" alt="License MIT"></a>
  <img src="https://img.shields.io/badge/Architecture-Modular%20CLI-0d1117.svg?style=flat-square" alt="Modular CLI">
  <img src="https://img.shields.io/badge/Domain-Crypto%20%7C%20BinEx%20%7C%20Web%20%7C%20DFIR-0d1117.svg?style=flat-square" alt="Domain">
</p>

Terminal-first CTF helper framework engineered for legal labs, rapid challenge analysis, and defensive triage. Features interactive domain modules:
* **Crypto:** Classical cipher solvers, frequency analysis, and automated decoding routines.
* **BinEx:** Architecture header inspection, string entropy analysis, and binary helpers.
* **Web:** Offline payload crafting, URL/header parameter tamper utilities, and encoding matrix.
* **DFIR:** Magic byte header verification, metadata extraction, and offline forensic analysis.

```bash
# Quick run
git clone https://github.com/Nueeva/CTF-Toolkit.git
python CTF-Toolkit/main.py
```

👉 **[Explore the CTF-Toolkit Repository →](https://github.com/Nueeva/CTF-Toolkit)**

<br/>

**Other Platforms:**
* **[Clouvia](https://linktr.ee/die_de_nueva)** &nbsp;·&nbsp; Cloud hosting, secure infrastructure, and web platforms.
* **[nueva.my.id](https://nueva.my.id)** &nbsp;·&nbsp; Personal portfolio showcasing security projects, technical writeups, and full-stack systems.

<br/>

<img src="./hd-stack.svg" width="620" alt="stack"/>

<p align="left">
  <strong>Offensive Security &amp; Analysis</strong><br/>
  <img src="https://img.shields.io/badge/Focus-Web%20Pentesting-0d1117?style=flat-square&logo=securityscorecard&logoColor=f85149" alt="Web Pentesting" />
  <img src="https://img.shields.io/badge/Research-Reflected%20XSS-0d1117?style=flat-square&logoColor=3fb950" alt="Reflected XSS" />
  <img src="https://img.shields.io/badge/Standard-OWASP%20Top%2010-0d1117?style=flat-square&logoColor=58a6ff" alt="OWASP Top 10" />
  <img src="https://img.shields.io/badge/OS-Linux%20Hardening-0d1117?style=flat-square&logo=linux&logoColor=white" alt="Linux" />
  <img src="https://img.shields.io/badge/VCS-Git-0d1117?style=flat-square&logo=git&logoColor=F05032" alt="Git" />
</p>

<p align="left">
  <strong>Core Languages &amp; Runtimes</strong><br/>
  <img src="https://img.shields.io/badge/Node.js-Core%20HTTP-0d1117?style=flat-square&logo=node.js&logoColor=339933" alt="Node.js" />
  <img src="https://img.shields.io/badge/JavaScript-ES2024-0d1117?style=flat-square&logo=javascript&logoColor=F7DF1E" alt="JavaScript" />
  <img src="https://img.shields.io/badge/Python-Security%20Automation-0d1117?style=flat-square&logo=python&logoColor=3776AB" alt="Python" />
  <img src="https://img.shields.io/badge/Java-Systems%20%26%20Minecraft-0d1117?style=flat-square&logo=openjdk&logoColor=ED8B00" alt="Java" />
  <img src="https://img.shields.io/badge/PHP-Modern%208.2-0d1117?style=flat-square&logo=php&logoColor=777BB4" alt="PHP" />
  <img src="https://img.shields.io/badge/Shell-Bash%20%2F%20PowerShell-0d1117?style=flat-square&logo=gnubash&logoColor=white" alt="Shell" />
</p>

<p align="left">
  <strong>Infrastructure, Storage &amp; Cloud</strong><br/>
  <img src="https://img.shields.io/badge/Docker-Containers-0d1117?style=flat-square&logo=docker&logoColor=2496ED" alt="Docker" />
  <img src="https://img.shields.io/badge/MariaDB-High%20Perf-0d1117?style=flat-square&logo=mariadb&logoColor=white" alt="MariaDB" />
  <img src="https://img.shields.io/badge/MySQL-Relational-0d1117?style=flat-square&logo=mysql&logoColor=4479A1" alt="MySQL" />
  <img src="https://img.shields.io/badge/MongoDB-Document-0d1117?style=flat-square&logo=mongodb&logoColor=47A248" alt="MongoDB" />
  <img src="https://img.shields.io/badge/SQLite-Embedded-0d1117?style=flat-square&logo=sqlite&logoColor=003B57" alt="SQLite" />
  <img src="https://img.shields.io/badge/Firebase-BaaS-0d1117?style=flat-square&logo=firebase&logoColor=FFCA28" alt="Firebase" />
</p>

<br/>

<img src="./hd-stats.svg" width="620" alt="stats"/>

<div align="center">

<img src="./streak.svg" width="620" alt="Current and longest streak"/>

<img src="./langs.svg" width="620" alt="Top languages by bytes and by repo"/>

<img src="./year.svg" width="620" alt="The last year, one character per day"/>

<br/>

<img src="https://komarev.com/ghpvc/?username=nueeva&label=Profile%20Views&color=0e75b6&style=flat-square" alt="Profile Views" />

</div>

<br/>

<img src="./hd-connect.svg" width="620" alt="connect"/>

<p align="center">
  <a href="https://twitter.com/nueeva"><img src="https://img.shields.io/badge/Twitter-nueeva-0d1117?style=flat-square&logo=x&logoColor=white" alt="Twitter" /></a>
  <a href="https://linkedin.com/in/Nueva"><img src="https://img.shields.io/badge/LinkedIn-Nueva-0d1117?style=flat-square&logo=linkedin&logoColor=0A66C2" alt="LinkedIn" /></a>
  <a href="https://discord.com/users/Clouvia"><img src="https://img.shields.io/badge/Discord-Clouvia-0d1117?style=flat-square&logo=discord&logoColor=5865F2" alt="Discord" /></a>
  <a href="https://instagram.com/nueeva"><img src="https://img.shields.io/badge/Instagram-nueeva-0d1117?style=flat-square&logo=instagram&logoColor=E4405F" alt="Instagram" /></a>
  <a href="https://wa.me/+6281212994597"><img src="https://img.shields.io/badge/WhatsApp-+6281212994597-0d1117?style=flat-square&logo=whatsapp&logoColor=25D366" alt="WhatsApp" /></a>
  <a href="https://t.me/nueva_inc"><img src="https://img.shields.io/badge/Telegram-nueva_inc-0d1117?style=flat-square&logo=telegram&logoColor=26A5E4" alt="Telegram" /></a>
  <a href="mailto:rifqiariansyah123@gmail.com"><img src="https://img.shields.io/badge/Email-rifqiariansyah123@gmail.com-0d1117?style=flat-square&logo=gmail&logoColor=EA4335" alt="Email" /></a>
</p>

<br/>

<img src="./hd-about-this-page.svg" width="620" alt="about this page"/>

Every graphic here is self-generated, not embedded from third-party hosting services.<br>
`ascii.svg` renders typewriter-animated monochrome ASCII branding with SMIL;<br>
the stat graphics and section headings are drawn by a [scheduled GitHub Action](.github/workflows/stats.yml)<br>
straight from the GitHub GraphQL API, once a day, committing only what changed.

They animate via SMIL inside the SVG because GitHub strips scripts and inline CSS from READMEs.<br>
Because nothing loads from external analytics hosts, nothing can rate-limit, break, or go dark.<br>
The typeface is [JetBrains Mono](scripts/fonts), subsetted to character usage and inlined as base64.
