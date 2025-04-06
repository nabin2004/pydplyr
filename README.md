<h1 align="center">🐍 pydplyr</h1>

<p align="center">
  <em>Simplicity and conciseness of R,<br>
  with the blazing speed and future-proof power of Rust.</em>
</p>

<p align="center">
  <strong>Chainable</strong> • <strong>Composable</strong> • <strong>Declarative</strong> • <strong>Semantic</strong> • <strong>Agent-Ready</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/build-passing-brightgreen?style=flat-square">
  <img src="https://img.shields.io/badge/python-3.8+-blue?style=flat-square">
  <img src="https://img.shields.io/badge/backend-pandas-orange?style=flat-square">
  <img src="https://img.shields.io/badge/vision-Rust%20Core-red?style=flat-square">
</p>

---

## 🌟 TL;DR

`pydplyr` is a modern, expressive, and chainable data manipulation library built for humans and machines. Think:

- 🧠 **Like dplyr in R**
- ⚡️ **With Python's ecosystem**
- 🚀 **On a path to a Rust-powered backend**
- 🤖 **Agent-ready for autonomous systems**

Whether you're a data scientist, a developer building intelligent systems, or a machine 🤖 looking for clarity—this library speaks your language.

---

## ✨ Key Features

- ✅ **Composable Verbs** – clear, expressive syntax for fast prototyping & serious work
- 🧬 **Chainable API** – minimal boilerplate, max readability
- 🎨 **Grammar of Graphics** – familiar design for layered visualizations *(Coming Soon!)*
- 🔍 **Simplified Regex** – harness RegEx without the brain melt
- 🔗 **Agent-First Thinking** – semantically rich, logic-oriented operations
- 🦀 **Rust Ambition** – future versions will compile to Rust for *blazing performance*

---

## 🛠️ Verbs You Can Use Today

Each verb is purpose-built and plays well with others. Start small, scale infinitely.

| Verb         | Description                          |
|--------------|--------------------------------------|
| `arrange()`  | Sort your data                       |
| `select()`   | Pick columns                         |
| `filter()`   | Subset rows                          |
| `mutate()`   | Create or modify columns             |
| `summarize()`| Aggregate and reduce                 |
| `group_by()` | Enable grouped operations            |
| `distinct()` | Drop duplicate rows                  |

### 🔁 Sample Chain

```python
from pydplyr import *

result = (
    Panel(df)
    .arrange(desc("score"))
    .filter("score > 80")
    .mutate(score_plus_age="score + age")
    .select("name", "score_plus_age")
    .collect()
)
```

> Intuitive, readable, chainable. One thought per line.

---

## 📈 Grammar of Graphics (WIP)

Just like in `ggplot2`, our graphics philosophy follows this layered system:

- **Data** – the DataFrame
- **Aesthetics** – x/y mappings, color, shape
- **Geoms** – bar, point, line, etc.
- **Stats** – transformations like count or smooth
- **Facets** – split plots by category
- **Coords** – coordinate systems (polar, cartesian, etc.)
- **Themes** – polish for publication or dashboard

> 📊 Visuals should *tell*, not *yell*.

---

## 🔡 Simplified RegEx

We believe RegEx shouldn't be a dark art.

```python
Panel(df).filter_col("email", pattern=".*@example.com")
```

You get the full power of `re`, simplified into expressive helpers for real-world usage.

---

## 🔮 Vision

> The future of data is **semantic, composable, and intelligent**.

`pydplyr` is being designed with **agentic AI frameworks** in mind — where the code can be read and written by both humans *and* agents.

Whether it’s embedded in LLM-based agents or running as the logic core of autonomous data pipelines, `pydplyr` is made to be **interpretable**, **traceable**, and **chainable**.

---

## 🧪 Roadmap

- [x] Core verbs (arrange, select, filter, mutate, summarize, distinct)
- [ ] Grouped operations
- [ ] Grammar of Graphics module
- [ ] Rust backend (via `pyo3` or `polars`)
- [ ] Natural-language Regex builder
- [ ] LLM prompt-to-code interface
- [ ] Optional `async` API for distributed computing
- [ ] Plugin system for custom verbs and visual geoms

---

## 📦 Installation

```bash
pip install pydplyr
```

---

## 🤝 Contributing

We welcome contributors who care about:

- elegant APIs 🧼  
- expressive code 💬  
- performance 🔥  
- semantic richness 🌐  
- and dreaming big 💡  

To get started, clone the repo and check the [CONTRIBUTING.md](./CONTRIBUTING.md) guidelines.

---

## 💬 Community

Got ideas? Found bugs? Want to build the future of data science?

- Open an issue  
- Start a discussion  
- Or just drop by with a star ⭐️

---

## 🧠 Quote to Code

> *"The art of data science is not in the numbers — it’s in the story they tell, and the tools that let them speak."*

—

### ✨ `pydplyr`: Built to Think. Built to Chain. Built for Tomorrow.
