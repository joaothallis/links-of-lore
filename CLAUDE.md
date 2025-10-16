# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Links of Lore is a curated collection of technical articles and resources organized by topic in README.md. The repository includes a Python utility (`fetch_title.py`) that fetches webpage titles and formats them as markdown links.

## Repository Structure

- `README.md` - Main content file containing curated links organized by categories (AI, Database, Programming Languages, etc.)
- `fetch_title.py` - Python script to fetch webpage titles and generate markdown links
- `tests/test_fetch_title.py` - Unit tests for the fetch_title utility
- `shell.nix` - Nix shell environment configuration for Python dependencies
- `.github/workflows/ci.yml` - CI workflow (references check_links.py which doesn't exist in repo)

## Development Environment

### Setup with Nix

This project uses Nix for reproducible development environments:

```bash
nix-shell
```

This automatically loads Python 3 with `requests` and `beautifulsoup4` packages.

### Setup with pip

Alternatively, install dependencies using pip:

```bash
pip install -r requirements.txt
```

## Common Commands

### Fetch a webpage title and generate markdown link

```bash
python3 fetch_title.py "https://example.com"
```

Output format: `[Page Title](https://example.com)`

### Run tests

```bash
python -m unittest tests/test_fetch_title.py
```

Or run all tests from the tests directory:

```bash
python -m unittest discover tests/
```

## Content Management

### Link Format in README.md

Links follow this structure:
- `[x]` - Read/completed links
- `[ ]` - Unread/pending links
- Links may include hashtags for cross-referencing (e.g., `#tmux #vim #psql`)
- Nested hierarchies use indentation for sub-topics

### Adding New Links

1. Use `fetch_title.py` to get the formatted markdown link
2. Add to the appropriate category in README.md
3. Mark as `[ ]` for unread or `[x]` for already reviewed
4. Add relevant hashtags if cross-referencing other topics

## Testing Strategy

The test suite uses:
- `unittest` framework with mocking (`unittest.mock`)
- `@patch('requests.get')` to mock HTTP requests
- Test coverage includes: successful requests, missing titles, HTTP errors, and connection errors

## Notes

- The CI workflow references `check_links.py` which doesn't currently exist in the repository
- The project is MIT licensed
- Main branch is `main`
