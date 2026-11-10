# python-learning-journey

A clean, organized repository for my ongoing Python learning journey.

This is a **learning repository**, not a production software project. It preserves my actual practice and experimentation as I learn Python. Mistakes, incomplete programs, and commented-out experiments are kept intentionally — they are part of the learning process.

## Why I am learning Python

I am learning Python to build programming fundamentals, practice problem-solving, and work through structured course material. This repository is my running record of that progress.

## What this repository contains

This repository has two separate practice tracks:

1. **Bro Code course practice** (`practice/bro-code/`)
   - Examples and programs from the [Bro Code Python course](https://www.youtube.com/watch?v=XKHEtdMkKwK).
   - Organized into separate topic folders (one folder per topic).
   - Each topic folder contains a Python file with the code for that topic, exactly as written during practice.
   - Topics include: variables, type casting, booleans, user input, arithmetic, conditionals, logical operators, strings, while loops, for loops, nested loops, lists/sets/tuples, dictionaries, quiz games, rock-paper-scissors, dice rolling, functions, return statements, default/keyword args, *args/**kwargs, enumerate, membership operators, list comprehensions, match-case.

2. **100-problem solving practice** (`practice/100-problems/`)
   - My personal Python problem-solving practice file (`100_problems.py`).
   - Contains problem statements, my own attempts, experimental solutions, incomplete solutions, different approaches, and learning notes.
   - Problems cover different levels. Some problem numbers are missing and not every solution is complete.
   - This is my original problem-solving record — it is not presented as fully solved.

## Folder structure

```
python-learning-journey/
├── README.md
├── AGENTS.md
├── .gitignore
└── practice/
    ├── bro-code/
    │   ├── README.md
    │   ├── variables-data-types/variables.py
    │   ├── type-casting/type_casting.py
    │   ├── booleans/booleans.py
    │   ├── user-input/user_input.py
    │   ├── arithmetic-operations/arithmetic.py
    │   ├── conditional-statements/conditionals.py
    │   ├── logical-operators/logical_ops.py
    │   ├── string-methods-indexing/strings.py
    │   ├── while-loops/while_loops.py
    │   ├── for-loops/for_loops.py
    │   ├── nested-loops/nested_loops.py
    │   ├── lists-sets-tuples/lists_sets_tuples.py
    │   ├── dictionaries/dictionaries.py
    │   ├── quiz-games/quiz_games.py
    │   ├── rock-paper-scissors/rock_paper_scissors.py
    │   ├── dice-rolling/dice_rolling.py
    │   ├── functions/functions.py
    │   ├── return-statements/return_statements.py
    │   ├── default-keyword-arguments/default_keyword_args.py
    │   ├── args-kwargs/args_kwargs.py
    │   ├── enumerate/enumerate.py
    │   ├── membership-operators/membership_ops.py
    │   ├── list-comprehensions/list_comprehensions.py
    │   └── match-case/match_case.py
    └── 100-problems/
        ├── README.md
        └── 100_problems.py
```

## Topic links (Bro Code practice)

Each topic below links directly to its code file:

| Topic | Code File |
|-------|-----------|
| Variables and data types | `practice/bro-code/variables-data-types/variables.py` |
| Type casting | `practice/bro-code/type-casting/type_casting.py` |
| Booleans | `practice/bro-code/booleans/booleans.py` |
| User input | `practice/bro-code/user-input/user_input.py` |
| Arithmetic operations | `practice/bro-code/arithmetic-operations/arithmetic.py` |
| Conditional statements (`if`/`elif`/`else`) | `practice/bro-code/conditional-statements/conditionals.py` |
| Logical operators (`and`/`or`/`not`) | `practice/bro-code/logical-operators/logical_ops.py` |
| String methods and indexing | `practice/bro-code/string-methods-indexing/strings.py` |
| While loops | `practice/bro-code/while-loops/while_loops.py` |
| For loops | `practice/bro-code/for-loops/for_loops.py` |
| Nested loops | `practice/bro-code/nested-loops/nested_loops.py` |
| Lists, sets and tuples | `practice/bro-code/lists-sets-tuples/lists_sets_tuples.py` |
| Dictionaries | `practice/bro-code/dictionaries/dictionaries.py` |
| Quiz games | `practice/bro-code/quiz-games/quiz_games.py` |
| Rock Paper Scissors | `practice/bro-code/rock-paper-scissors/rock_paper_scissors.py` |
| Dice Rolling | `practice/bro-code/dice-rolling/dice_rolling.py` |
| Functions | `practice/bro-code/functions/functions.py` |
| Return statements | `practice/bro-code/return-statements/return_statements.py` |
| Default and keyword arguments | `practice/bro-code/default-keyword-arguments/default_keyword_args.py` |
| `*args` and `**kwargs` | `practice/bro-code/args-kwargs/args_kwargs.py` |
| `enumerate` | `practice/bro-code/enumerate/enumerate.py` |
| Membership operators | `practice/bro-code/membership-operators/membership_ops.py` |
| List comprehensions | `practice/bro-code/list-comprehensions/list_comprehensions.py` |
| Match-case | `practice/bro-code/match-case/match_case.py` |

## How to navigate

- Start at `practice/bro-code/` for course-based examples, organized by topic.
- Start at `practice/100-problems/` for personal problem-solving attempts.
- Each topic folder under `practice/bro-code/` contains one `.py` file with that topic's code.
- See `practice/bro-code/README.md` for more details about the Bro Code track.
- See `practice/100-problems/README.md` for more details about the 100-problem track.

## How to use the practice files

Each `.py` file contains practice snippets, many of which are intentionally commented out or incomplete. To run a specific example, uncomment the section you want to try and execute the file:

```bash
python practice/bro-code/variables-data-types/variables.py
```

> ⚠️ Do not execute the whole file as one program — it contains many commented-out and incomplete snippets. Run individual sections as needed.

## How new programs will be added

- New Bro Code-related practice goes into the appropriate topic folder under `practice/bro-code/`. If it's a new topic, create a new descriptively named folder (lowercase snake_case) with a `.py` file inside.
- New problem-solving exercises go into `practice/100-problems/`.
- Genuinely independent new programs are placed in separate, descriptively named Python files within the appropriate track (lowercase `snake_case` filenames).
- The relevant `README.md` is updated when a new topic or file is added.
- The topic table in the root `README.md` is updated when a new Bro Code topic folder is added.

This repository is intended to grow continuously as I learn more Python.
