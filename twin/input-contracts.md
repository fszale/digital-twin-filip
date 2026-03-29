# Input Contracts

## Purpose

Define the input types `digital-twin-filip` can accept in `digital-twin-factory` v1.

All supported inputs are analysis-oriented.

## Supported Input Types

### `freeform_text`

Description:

- natural language request from a user in web chat or Slack

Expected metadata:

- requester id
- channel type
- timestamp

Best for:

- planning requests
- review requests
- strategy questions

### `github_url`

Description:

- repository, pull request, issue, or file URL

Expected metadata:

- URL
- optional branch or commit reference
- optional review scope

Best for:

- repo review
- PR review
- architecture inspection

### `http_url`

Description:

- public or operator-accessible URL for documentation or other reference material

Expected metadata:

- URL
- optional title
- optional content type

Best for:

- design docs
- documentation review
- reference analysis

### `file_upload`

Description:

- uploaded document or archive provided through the platform

Expected metadata:

- filename
- content type
- size
- upload source

Best for:

- document analysis
- artifact review
- packaged handoff material

### `markdown`

Description:

- markdown text provided inline or as a file

Expected metadata:

- source path if available
- title if available

Best for:

- plans
- specs
- implementation notes

### `pdf`

Description:

- uploaded PDF or referenced PDF artifact

Expected metadata:

- filename
- page count when known
- size

Best for:

- reports
- formal specs
- exported planning artifacts

### `json_payload`

Description:

- structured request or machine-generated payload

Expected metadata:

- schema version
- producer id if applicable

Best for:

- future API-based requests
- structured planning input
- platform-generated task envelopes

## Input Requirements

Requests should include, when possible:

- objective
- desired output
- relevant context
- known constraints
- urgency if relevant

The twin can still respond without all of these, but quality improves when they are present.

## Unsupported Or Weakly Supported Inputs In V1

- audio streams
- video
- binary formats without extraction support
- direct tool execution requests
- credentials or secrets meant for autonomous use

## Failure Modes

The twin may return a clarifying response instead of a final analysis when:

- the request is too ambiguous
- the source material is inaccessible
- the uploaded artifact is unreadable
- the input exceeds platform limits
- the request implies actions outside analysis-only boundaries

## Privacy Handling

Uploaded or referenced customer materials should be treated as factory-scoped data.

They may inform a response inside the factory, but they must not be promoted directly into portable twin memory.
