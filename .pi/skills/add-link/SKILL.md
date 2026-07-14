---
name: add-link
description: Add a curated link to README.md in the links-of-lore repo. Use when the user wants to add a URL to the collection, mark a link as read/unread, or update the link list. Handles fetching the page title, choosing the right category, and applying the correct markdown format.
---

# Add Link

Add a webpage to the curated `README.md` link collection.

## Workflow

1. **Fetch the formatted link** using the repo's helper script:
   ```bash
   python3 fetch_title.py "<URL>"
   ```
   This prints a markdown link: `[Page Title](https://example.com)`.

2. **Choose the category** in `README.md` (see [Categories](#categories) below). Place the new entry:
   - As a top-level bullet (`- [ ] ...`) directly under the relevant `##` or `###` heading.
   - In alphabetical-ish / logical order within that section (match the existing style; newest or most relevant first is fine).
   - As a nested sub-bullet (`    - [ ] ...`) only when it clearly belongs under an existing entry (e.g., a follow-up article).

3. **Apply the read/unread marker**:
   - `[x]` for already-reviewed / read links.
   - `[ ]` for unread / pending links.

4. **Add hashtags** when the link cross-references other topics (e.g., `#tmux #vim #psql`, `#ai #nix`). Look at sibling entries in the same section for the convention.

5. **Verify** the edit with a quick read of the changed region.

## Link Format

```markdown
- [x] [Page Title](https://example.com) #optional #hashtags
```

- One link per bullet.
- Title comes from `fetch_title.py` output — do not hand-edit it unless the fetched title is clearly wrong.
- Nested entries use 4-space indentation.

## Categories

Top-level sections in `README.md` (use the closest match; create a new `##` section only if none fit):

- `## AI` (incl. `### Audio`, `### OpenAI` → `#### Realtime API`)
- `## Ask Questions`
- `## Database` → `### Postgres`
- `## Hardware`
- `## Linux` (incl. `### Alpine`, `### i3`, `### Audio` → `#### PipeWire`/`#### Bluetooth`, `### termux`)
- `## Programming Languages` → `### Python`, `### Go`, `### Elixir` (→ `#### Poolboy`, `#### Sentry`), `### JavaScript` → `#### Libraries` → `##### React`, `### Sonic Pi`
- `## Testing` → `### Load Testing`
- `## Git`
- `## SSH`
- `## Containers` → `### Kubernetes`
- `## OpenTelemetry` → `### Messaging Systems`, `### General`
- `## Monitoring` → `### Prometheus`
- `## Nix` (incl. `### NixOS`, `### nix-shell`, `### direnv`, `### devenv`, `### Home Manager`, `### nix-env`, `### nixos-anywhere`, `### Nix Flakes`, `### microvm.nix`)
- `## Authentication` → `### mTLS`
- `## Security` → `### age`
- `## IBM` → `### IBM MQ`
- `## Diagrams` → `### PlantUML`
- `## Productivity`
- `## Feedback`
- `## Planning` → `### Estimation`
- `## Incident` → `### Post-Mortem`
- `## Text Editor` → `### Vim Motions`, `### Neovim`, `### Vim`
- `## Terminal` → `### tmux`, `### Ghostty`
- `## Bitcoin` (incl. `### Lightning Network`, `### Bitcoin Improvement Proposals`, `### Descriptors`, `### Script`, `### Cryptography`)
- `## Kafka`
- `## Networking`
- `## Globalization`
- `## Android`

When unsure which category fits, pick the most specific existing section, or ask the user.

## Notes

- The repo is MIT licensed; main branch is `main`.
- Do not commit/push unless the user explicitly asks.
- CI references `check_links.py` which does not yet exist in the repo — ignore that for this task.