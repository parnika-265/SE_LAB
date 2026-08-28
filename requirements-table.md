# Complete Requirements Table

## Project: Student Project Portfolio & Showcase App

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| FR-001 | Functional | The system shall enable student teams to create showcase profiles containing project information, abstracts, summaries, demo video links, and verified GitHub repository URLs. | High | Student teams can create a profile; project details can be added; demo links can be submitted; GitHub URLs are validated; invalid URLs are rejected. | Allows students to present their projects in a centralized showcase. |
| FR-002 | Functional | The system shall enable panel judges to evaluate projects using a weighted digital rubric. | High | Judges can access projects; rubric criteria are displayed; scores can be entered; weighted scores are calculated correctly. | Provides a structured and fair method for evaluating projects. |
| FR-003 | Functional | The system shall allow the public to cast secure votes for projects. | High | Eligible users can vote; duplicate or invalid votes are prevented; votes are securely recorded. | Enables public participation while protecting the integrity of voting. |
| FR-004 | Functional | The system shall update the weighted leaderboard based on project evaluation and public voting results. | High | Scores are calculated correctly; leaderboard rankings are updated; updated rankings are displayed to users. | Provides transparent and up-to-date project rankings. |
| FR-005 | Functional | The system shall allow student teams to edit their showcase profiles before the submission deadline. | Medium | Students can edit profile information before the deadline; changes are saved successfully; editing is restricted after the deadline. | Allows students to correct or update their project information before submission closes. |
| NFR-001 | Non-Functional | Public voting and leaderboard calculations shall update in real time with an API response latency under 300 ms. | High | Benchmarking tests confirm that response latency remains under 300 ms under simulated peak load. | Ensures good performance and responsiveness for users. |
| NFR-002 | Non-Functional | The system shall provide anti-Sybil security and reliability protections for public voting. | High | Security mechanisms detect or prevent suspicious duplicate or fraudulent voting attempts; voting data remains reliable and protected. | Protects the fairness and reliability of the public voting process. |
