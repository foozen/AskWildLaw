# 🧠 Ask WildLaw – Feature Log

A living log of ideas, enhancements, and improvements for Ask WildLaw. Prioritised for development planning and MVP tracking.

---

## ✅ Core Features (MVP)

| Feature | Status | Priority | Notes |
|--------|--------|----------|-------|
| Simple user Q&A with postcode input | ✅ Complete | High | Enables basic interaction |
| Submit button + UX cleanup | ✅ Complete | High | Makes app usable and intuitive |
| Example prompts + topic buttons | ✅ Complete | High | Guides input for clarity |
| Basic AI answer via GPT | ✅ Complete | High | Initial chatbot functionality |

---

## 🔄 In Progress

| Feature | Status | Priority | Notes |
|--------|--------|----------|-------|
| Use real UK guidance/law in answers | 🔄 In Progress | High | Transitioning from GPT guesses to law-backed answers |
| Role-based summaries (Landowner vs. Government) | 🔄 In Progress | High | Clarifies duties and ownership of actions |

---

## 📋 Planned

| Feature | Status | Priority | Notes |
|--------|--------|----------|-------|
| Include links to source law/guidance in answers | 📝 Planned | High | Builds trust and enables deeper reading |
| Include contact details for NE/DEFRA/licensing help | 📝 Planned | High | Empowers users to follow up correctly |
| Copy to clipboard / Save response | 📝 Planned | Medium | Useful for planning applications or evidence |
| Confidence level or "Check with NE" note in answers | 📝 Planned | Medium | Reinforces non-legal-advice position |
| Auto-refresh of law/guidance via scraper or API | 📝 Planned | High | Ensures app stays up to date with law |
| Exportable response as PDF | 📝 Planned | Medium | Good for record keeping or sharing |

---

## 📦 Backlog / Future Features

| Feature | Status | Priority | Notes |
|--------|--------|----------|-------|
| Portal mode for NE staff or advisors | 💤 Backlog | Medium | Lets NE give guided access to queries |
| Role-based access / portals (e.g. Landowners, Planners) | 💤 Backlog | Medium | Could offer tailored views for key audiences |
| User account system | 💤 Backlog | Low | Needed only for advanced tracking/logs |
| Usage analytics dashboard | 💤 Backlog | Low | Helps monitor what’s being asked most |
| LangChain migration to new packages (`langchain_openai`, `langchain_community`) | Planned | Medium | Current code uses deprecated imports (e.g. `OpenAIEmbeddings`). Will need to refactor to new `langchain-openai` versions ahead of LangChain 1.0. See deprecation warnings for guidance. |
| Improve fact-checking and legal precision (e.g. 30-year rule) | In Progress | High | Assistant slightly misinterpreted hedgerow law. Needs either better source wording or improved system prompt to quote facts more directly. |
| Legal Check Mode (Toggle formal vs practical answers) | Complete | High | Successfully shifts tone and quoting style. Helps support both cautious users and those looking for plain-English steps. Demonstrates clear value in MVP. |

---
