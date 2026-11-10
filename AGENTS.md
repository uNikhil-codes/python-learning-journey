# AGENTS.md — Instructions for future AI agents

This is a Python learning repository, not a production software project. The goal is to preserve the user's actual learning journey, not to make the code look professional.

## Core rules

- **Never modify existing learning code unless the user explicitly requests it.**
- **Never remove previous attempts.**
- **Keep Bro Code practice separate from 100-problem practice.**
- Add new Bro Code-related practice to `practice/bro-code/`.
- Add new problem-solving exercises to `practice/100-problems/`.
- Place genuinely independent new programs in separate, descriptively named Python files within the appropriate track.
- Use **lowercase snake_case** for new standalone Python filenames.
- Do not duplicate existing programs unnecessarily.
- **Never invent completed exercises or progress statistics.**
- Document new folders and learning tracks in the relevant `README.md`.
- Do not add external dependencies unless required.
- **Check for accidental credentials or personal information before uploading.**
- **Never push personal information to a public repository without the user's approval.**
- Never overwrite existing work without checking it first.

## Preservation rules (when editing existing files)

- Preserve entire file contents, all comments, all program attempts, triple-quoted sections, and incomplete programs.
- Preserve original program order, variable names, approaches, and mistakes.
- Do not rewrite programs, correct syntax, change logic, remove unused code, remove commented programs, uncomment code automatically, replace solutions with better ones, split files, or reformat to professional standards.

## Privacy

- Scan for exposed credentials, emails, phone numbers, real names, addresses, or other personal information before any push.
- If personal info is found, replace with fake placeholders and flag with a `[PRIVACY: ...]` comment, or ask the user.
- Never change repository visibility without the user's explicit approval.

## Repository layout

```
python-learning-journey/
├── README.md
├── AGENTS.md
├── .gitignore
└── practice/
    ├── bro-code/
    │   ├── README.md
    │   └── Practice (bro code).py
    └── 100-problems/
        ├── README.md
        └── 100_problems.py
```
