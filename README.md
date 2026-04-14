# 🧠 Home AI

## Version: v1 (Architecture Freeze)

Home AI is a declarative, human-governed cognitive execution system with strict separation between:

- Cognition (decision-making)
- Execution (action runtime)
- Security (capability enforcement)
- Architecture (declarative system definition)
- Verification (runtime integrity checks)
- Drift Detection (non-mutating observation)

---

## 🚨 Architectural Guarantee (v1 Freeze)

This system is **frozen at architecture version 1**.

No subsystem is allowed to:

- Modify system architecture at runtime
- Self-approve structural changes
- Add implicit wiring or hidden dependencies
- Override governance or security boundaries

All structural changes MUST be made through:
`architecture/system.yaml`

---

## 🧱 Core Architecture

### 🧠 Cognition
Located in:
core/cognition/

Responsible for:
- Planning
- Replanning
- Tool selection (capability-aware)

---

### ⚙️ Execution
Located in:
core/execution/


Responsible for:
- DAG execution
- Tool invocation
- Result handling

---

### 🔐 Security
Located in:
runtime/security/

Responsible for:
- Capability enforcement
- Tool proxying
- Permission validation

---

### 🧾 Architecture (Source of Truth)
Located in:
architecture/

Contains:
- system.yaml (single source of truth)
- loader (runtime graph construction)
- introspection (structure verification)

---

### 🔍 Verification Layer
Located in:
architecture/introspection/

Responsible for:
- Comparing runtime vs spec graph
- Detecting structural drift
- Reporting mismatches (NO fixes)

---

### 🧬 Integrity Layer
Located in:
runtime/drift/
arch_guard/

Responsible for:
- Detecting behavioral drift
- CI enforcement signals

---

## 🧠 System Construction Flow
system.yaml
↓
loader
↓
runtime graph
↓
execution system
↓
introspection verification

---

## 🚫 Forbidden Behaviors (Hard Rules)

- No runtime architecture mutation
- No implicit system wiring
- No cross-layer authority override
- No self-healing structural changes
- No bypassing loader or YAML spec

---

## 🧾 Architecture Versioning

This is:

> Home AI v1 — Frozen Architecture Baseline

Any structural changes require a new version (v2+).  
v1 MUST remain immutable for reference and validation.

---

## 🧠 Design Philosophy

Home AI v1 prioritizes:

- Deterministic behavior
- Explicit system structure
- Human-controlled evolution
- Runtime verifiability
- Strict separation of concerns

---

## 🔒 Summary

Home AI is not an evolving runtime system.

It is a **declared and verified cognitive architecture**.

