# Unit 3 — CodeHS Advanced Python and AI Programming

**Suggested length:** 5 × 75 minutes + optional extension  
**Purpose:** strengthen program structure, algorithmic reasoning, and AI-programming fluency before sustained ML work.  
**Primary resource:** selected modules from CodeHS *Advanced Python and AI Programming*.

## Selection Rule

Do **not** run the entire year-long course as a prerequisite. Select the pieces that directly improve IOAI readiness:

- OOP for organising larger programs;
- libraries and packages;
- data structures / algorithms where they improve reasoning;
- search and graph-search ideas;
- selected AI Algorithms content;
- classifier build/evaluation.

The adventure-game and music-player projects are optional programming extensions, not required IOAI milestones.

## Lesson Sequence

| Lesson | Learn | Practice | Rebuild | Share / Evidence |
|---:|---|---|---|---|
| 1. Program structure + OOP for ML code | classes, composition, interfaces; when OOP helps and when it adds noise | refactor a small procedural script | design a small reusable data/model helper class | code + design rationale |
| 2. Libraries, packages, docs, exceptions | reading APIs, imports, environment discipline, defensive code | inspect and use an unfamiliar library function | reproduce the behaviour from documentation only | dependency note + tested code |
| 3. Data structures + complexity | stack/queue/hash/tree/graph concepts, Big-O intuition | compare operations and trace algorithms | choose a data structure for an unseen problem and implement it | complexity explanation |
| 4. Search / AI algorithms | state, actions, goal, heuristic, graph search | trace BFS/DFS/greedy/A*-style examples as appropriate | solve a new state-space problem | search trace + limitations |
| 5. Build and evaluate a classifier | features, labels, split, baseline, train, predict, evaluate | guided classifier | rebuild on a new dataset and explain metric choice | classifier notebook + mini model card |

Continue the formal task-recognition drill from Unit 2 and require students to justify the baseline and metric rather than merely name them.

## Optional Extension

Strong students may complete a larger CodeHS project if it develops a demonstrated weakness in software design or algorithmic reasoning. It should not delay the ML workflow phase merely for course-completion percentage.

## Teacher Prompts

- Why is this abstraction useful here?
- What operation dominates runtime?
- What information is the algorithm allowed to use?
- What makes this search heuristic useful or dangerous?
- Is the classifier score valid, or did our workflow leak information?

## Exit Gate

Student can independently:

1. organise a non-trivial Python program;
2. read third-party documentation;
3. justify a data structure or algorithm choice;
4. trace a search process;
5. build a small classifier with a valid split and a stated metric;
6. explain at least one failure mode.
