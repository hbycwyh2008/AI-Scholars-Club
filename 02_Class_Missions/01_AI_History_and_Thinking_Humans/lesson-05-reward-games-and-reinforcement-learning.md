# Session 37 — Chapter 9 “Game On”: Games and Reinforcement Learning

**Class duration:** 70 minutes  
**Required reading before class:** Chapter 9, “Game On”  
**Supporting unit context:** Chapters 8 and 10 may be used for extension, but Chapter 9 is the required preparation for this lesson.  
**Essential question:** Why are games useful environments for AI learning, and what does success in a game actually prove?

## Lesson Design Principle

This class **uses** the reading; it does not repeat the reading.

Students who prepare begin immediately with retrieval, explanation, and application. Students who arrive without the required preparation enter the **Catch-Up Lane** and use class time to complete the missing reading evidence before joining the main activity.

The consequence is therefore built into the learning design:

```text
prepared before class
→ retrieve
→ explain
→ apply
→ extend

not prepared
→ catch up independently
→ miss the first discussion/retrieval evidence
→ join the class only after minimum preparation is complete
```

Do not give an emergency chapter summary to students who did not prepare. That would remove the reason to prepare next time.

## Before Class — Prep Ticket

Students read Chapter 9 and bring a completed Prep Ticket.

### Chapter 9 Prep Ticket

1. Write **three important ideas, people, systems, or terms** from the chapter.
2. Explain **one** of them in your own words.
3. Identify **one example** from the chapter that you think matters.
4. Write **one question** about something you do not fully understand.

The Prep Ticket is intentionally short. Its purpose is to make reading visible and to give every prepared student something to retrieve and explain in class.

## Preparation Gate

At the beginning of class, students show the Prep Ticket.

### Prepared

Student immediately enters the main lesson.

### Not Prepared

Student enters the **Catch-Up Lane**:

1. open Chapter 9;
2. read independently;
3. complete the minimum Prep Ticket;
4. show the completed ticket;
5. rejoin the main lesson at the current activity.

No extra punishment task is assigned. The natural cost is the class time and discussion the student loses while doing work that should already have been completed.

The teacher does **not** pause the main class to reteach the chapter.

## Required Mastery

By the end of the lesson, students should be able to:

1. explain why games are useful environments for AI research;
2. identify the roles of agent, environment, action, and reward in a game-learning setting;
3. distinguish a reward signal from a supervised-learning label;
4. explain why repeated interaction can be used for learning;
5. explain why success in a bounded game does not automatically imply general intelligence;
6. compare a game environment with a less predictable real-world environment;
7. explain one Chapter 9 idea clearly to a person with no AI background.

The target is **recognition → simple explanation → small application**, not memorisation of every technical detail.

## 70-Minute Learning Cycle

| Time | Block | Prepared students | Catch-Up Lane |
|---:|---|---|---|
| 0–5 | **Prep Gate** | Show Prep Ticket and begin individual retrieval. | Open Chapter 9 and start the missing Prep Ticket. |
| 5–12 | **Entry Retrieval** | Complete six short recall/recognition questions without the book. | Continue reading/prep independently. |
| 12–22 | **Teach-Back** | Explain one Prep Ticket idea to a partner; partner asks one follow-up question. | Rejoin only when the minimum Prep Ticket is complete. |
| 22–30 | **Teacher Bridge** | Teacher clarifies misconceptions and connects ideas; no chapter recap. | Join the bridge if prep is complete. |
| 30–47 | **Guided Application** | Compare why a game is easier to specify than a real-world task. | Participate once caught up. |
| 47–58 | **Transfer Challenge** | Analyse what may fail when a game-learning approach moves into the real world. | Participate once caught up. |
| 58–66 | **Teach a Beginner** | Explain one Chapter 9 idea to a Grade 6 student / beginner. | Participate once caught up. |
| 66–70 | **Exit Retrieval** | Close all materials and answer three final questions. | Complete the same exit retrieval. |

## Entry Retrieval — Easy Confidence-Building Questions

Students answer without opening the book.

1. What is the **agent** in a game-learning system?
2. What does the agent choose: a **label**, an **action**, or a **dataset**?
3. What information tells the agent whether an outcome was good or bad?
4. Give one reason games are useful environments for AI research.
5. Is winning one game enough to prove general intelligence? **Yes or no — then give one reason.**
6. Write one example, person, system, or idea you remember from Chapter 9.

These questions should feel achievable to a student who completed the reading. The goal is early success plus retrieval, not trick questions.

## Teach-Back

Students use their Prep Ticket, then close it.

Each student gets about two minutes:

> Explain one Chapter 9 idea as if your partner had not read the chapter.

The listener must ask one question:

> “Why does that matter?”

or

> “Can you give me an example?”

The speaker then improves the explanation.

## Teacher Bridge — Maximum 8 Minutes

Do not summarise Chapter 9 from beginning to end.

Use teacher time only for ideas students are unlikely to build correctly alone:

```text
game
→ clear rules
→ possible actions
→ repeated interaction
→ measurable outcome/reward
→ learning can be evaluated
```

Then establish the boundary:

```text
strong performance in a bounded game
≠
general intelligence in an open real world
```

If students already understand a point, move on.

## Guided Application — Why Games?

Give groups two environments:

### Environment A — Board / Video Game

- rules are specified;
- legal actions are constrained;
- success can usually be measured;
- the environment can be repeated many times.

### Environment B — School Helper Robot

The robot must “be helpful around school.”

Groups answer:

1. Which environment has the clearer goal?
2. Which environment has the clearer action space?
3. Which environment is easier to score automatically?
4. Which environment contains more ambiguity?
5. Why would an AI researcher often begin with Environment A?

Required output: a short comparison table plus a two-sentence conclusion.

## Transfer Challenge — From Game to Real World

Prompt:

> A system becomes extremely good at a game through repeated interaction and reward. What additional problems appear if we ask the same learning approach to operate in the real world?

Students identify at least three differences, such as:

- incomplete or noisy information;
- changing environments;
- goals that are difficult to specify;
- actions with real consequences;
- situations that cannot be repeated safely thousands of times;
- multiple people with different preferences;
- success that cannot be reduced to one simple score.

Students must connect each difference to the central question:

> What does game success prove, and what does it **not** prove?

## Teach a Beginner

Students choose one prompt:

- Explain why AI researchers use games.
- Explain “reward” without using technical vocabulary.
- Explain why winning a game is not the same as understanding the world.
- Explain the difference between learning from a label and learning from a reward.

Constraint: **60 seconds, no notes, no jargon unless the jargon is immediately explained.**

## Exit Retrieval

Close the book and all notes.

Answer:

1. Give **two reasons** games are useful for AI learning.
2. In one sentence, explain the role of **reward**.
3. Complete this statement:

```text
Being very good at a game demonstrates ____________________,
but it does not by itself demonstrate ____________________.
```

## Evidence of Learning

A complete lesson produces four visible pieces of evidence:

1. Chapter 9 Prep Ticket;
2. Entry Retrieval;
3. Guided Application comparison;
4. Exit Retrieval.

A student who arrives unprepared may complete the Prep Ticket during the Catch-Up Lane, but the teacher should not recreate the missed peer discussion for that student during the lesson.

## Teacher Check After Class

Use these questions to evaluate the lesson design itself:

- Did prepared students get an immediate advantage from preparing?
- Could an unprepared student still rely on the teacher to summarise the chapter? If yes, remove that pathway next lesson.
- Were the retrieval questions easy enough to build confidence?
- Did class time add value beyond what students could get from reading alone?
- Could students explain the main idea without copying book language?

## Gate

The student passes the lesson gate when they can independently explain:

1. why games are useful learning environments for AI; and
2. why game performance alone is insufficient evidence of broad, real-world intelligence.
