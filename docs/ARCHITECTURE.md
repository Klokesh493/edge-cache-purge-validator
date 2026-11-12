# Edge Cache Purge Validator architecture

Validates cache purge requests for scope, approval, and rollback notes.

```mermaid
flowchart LR
    A["Purge request CSV"]
    B["Check approval for global scope and require rollback notes"]
    C{"Validation issues present?"}
    D["Report missing approval or rollback notes"]
    E["Request passes the local checks"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
