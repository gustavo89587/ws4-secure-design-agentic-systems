# Pattern: Resource-Aware Telemetry for Agentic Systems
---
## Problem Statement
Agentic systems can enter infinite loops or recursive "hallucination states." This is a critical security vulnerability: Denial of Wallet (DoW) and Resource Exhaustion. Current designs focus on identity, but fail to address the availability and cost risks of uncontrolled telemetry generation.
---
## Proposed Design: The Telemetry Circuit Breaker
We propose an "Adaptive Sampling" mechanism at the telemetry layer for all AI Agents:

Span Budgeting: Limit the number of spans an agent can generate per single user request.

Redundancy Detection: If the agent emits repetitive telemetry patterns (indicating a loop), the system must trigger a circuit breaker to drop telemetry and pause execution.

Cost Guardrails: Direct integration between telemetry volume and execution cost monitoring.

---

 ## Implementation Insight (Based on OTel Standards)
The telemetry pipeline should implement a Tail-Sampling Processor logic, where traces exceeding a MaximumSpansPerTrace threshold are automatically dropped before hitting the storage backend.
