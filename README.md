# 🚀 TalentLens AI

> **XPRIZE "Build with Gemini" Hackathon Project**
> *Resumes tell employers what candidates claim. TalentLens shows what their projects actually demonstrate — then helps them close the gap before the interview.*

TalentLens AI is an evidence-based career-readiness platform for early-career software engineers[span_0](start_span)[span_0](end_span). It acts as an intelligent bridge between a candidate's GitHub repository and their target job description. By analyzing real code signals, it maps demonstrated skills directly to job requirements with strict, traceable evidence.

---

## ✨ Core Features

* **Evidence-First Analysis Engine:** Every verified skill claim links directly to a real repository file path, configuration, or test file. If a skill isn't in the code, it's labeled "unverified" rather than assuming the candidate lacks it.
* **Transparent Readiness Score:** Calculated in deterministic code using weighted criteria ($Required = 3\text{ pts}$, $Preferred = 1\text{ pt}$), ensuring an explainable and trustworthy metric.
* **HireReady Career Preparation (~30% of MVP):** Generates project-specific technical interview questions, architecture talking points, and prioritized repository growth tasks.
* **Responsible AI Guardrails:** Built strictly for decision support and preparation; it explicitly excludes automated hiring/screening decisions, code execution, or personality inference.

---

## 🏗️ Technical Architecture & Stack

The application ensures reliability by surrounding Gemini’s advanced reasoning with a deterministic data-collection pipeline.

* **Frontend:** Next.js with TypeScript & Tailwind CSS.
* **Backend:** Next.js Server Routes (Node.js).
* **AI Engine:** Google GenAI SDK powered by Gemini (utilizing Structured JSON Outputs and Long Context capabilities).
* **Data Retrieval:** GitHub REST API for secure metadata, trees, and file content collection.
* **Database:** Cloud Firestore for analysis records and share tokens.

---
