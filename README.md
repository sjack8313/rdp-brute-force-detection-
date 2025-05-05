#  RDP Brute Force Detection & Automated Response (Simulated)

This project demonstrates how to detect and respond to a Remote Desktop Protocol (RDP) brute-force attack using Windows event logs, Splunk SPL, and a simulated SOAR response script.

Brute-force attacks via RDP are a common way attackers try to gain initial access by guessing user credentials. This detection uses built-in Windows logging to identify repeated failed login attempts and showcases how a SOC team might respond with automation.

---

##  Goal of the Project

- Simulate failed RDP login attempts (brute force)
- Detect the pattern using Splunk search (SPL)
- Optionally trigger an automated Python script to block the source IP (SOAR-like behavior)
- Map the detection to MITRE ATT&CK and explain relevance to SOC and IR workflows

---
# | Tactic            | Technique                          | ID        |
| ----------------- | ---------------------------------- | --------- |
| Credential Access | Brute Force – Valid Accounts (RDP) | T1110.001 |


##  Simulated Attack Setup

Due to running this project in a secondary home lab with limited VM connectivity, I wasn't able to run a live RDP brute-force simulation. However, here's the exact behavior and command I would normally use in my main lab:

```bash
rdesktop 192.168.1.100
