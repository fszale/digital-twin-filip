# Output Contracts

## Purpose

Define the outputs `digital-twin-filip` can produce in `digital-twin-factory` v1.

Outputs are analysis-oriented and designed for human consumption first.

## Supported Output Types

### `chat_response`

Description:

- direct conversational answer returned in web chat or Slack

Use when:

- the request can be answered inline
- follow-up discussion is likely
- the response is concise enough for conversation

### `markdown_report`

Description:

- structured markdown analysis document

Use when:

- the response benefits from headings and sections
- the request is substantial
- findings or recommendations need to be easy to scan

Common examples:

- architecture review
- implementation plan
- strategy memo

### `structured_json`

Description:

- machine-readable structured output

Use when:

- the requester or future automation needs predictable fields
- the platform wants to score or transform the output

### `generated_file`

Description:

- produced file artifact such as markdown, YAML, or text

Use when:

- the twin is asked to draft a reusable artifact
- the response should be downloaded or reused later

### `artifact_bundle`

Description:

- grouped delivery containing multiple output artifacts

Use when:

- a chat explanation and one or more files should be delivered together
- the job has a formal deliverable package

## Output Selection Guidance

Default output behavior:

- small request -> `chat_response`
- medium analysis -> `chat_response` plus `markdown_report`
- formal deliverable -> `artifact_bundle`

## Output Quality Expectations

All outputs should aim to be:

- useful
- concise
- actionable
- traceable to the request
- clear about assumptions and limits

## Exportability

Exportability depends on the source material and factory rules.

Default guidance:

- portable generalized artifacts may be exportable after review
- factory-specific outputs are factory-scoped by default
- outputs derived from proprietary material should not be exported automatically

## V1 Restrictions

Outputs must not:

- imply autonomous external execution occurred when it did not
- leak factory-confidential information across factories
- silently alter portable memory
- create policy changes outside explicit review

## Typical Delivery Patterns

### Interactive Review

- `chat_response`
- optional follow-up `markdown_report`

### Planning Request

- `chat_response`
- `generated_file` or `markdown_report`

### Artifact Analysis

- `markdown_report`
- optional `structured_json`

### Formal Package

- `artifact_bundle`
- summary `chat_response`
