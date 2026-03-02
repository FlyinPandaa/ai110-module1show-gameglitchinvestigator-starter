# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

| Bug | Details |
|---|---|
| Hardcoded UI message | App showed "Guess a number between 1 and 100." regardless of difficulty; changed to use `low`/`high` and ensured new games pick secrets within the selected range. |
| Difficulty range mismatch | "Hard" used range 1–50 (smaller than "Normal" 1–100), which can make the game easier; propose updating `get_range_for_difficulty("Hard")` to a larger range (e.g., 1–200) or rebalancing ranges. |
| Secret number staleness | Secret is only generated when `secret` is absent, so changing difficulty can leave the secret outside the new range; propose regenerating the secret when difficulty changes or when the stored secret falls outside `low`..`high`. |
| Inverted hint messages | Hints show the wrong direction (e.g., "Too High" displays "Go HIGHER!"); propose swapping the hint text so messages match the comparison outcome. |



---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- I used Copilot on Auto for this project. For the most part the AI-proposed fixes were okay. The only thing that Copilot "failed" at was when I asked it to document bugs that was fixed. I wanted it as a table and I assumed that Copilot would make a table in the Reflection.md, but it only made a bullet point. I had to clarify my instruction to Copilot to format the bug reports the way I wanted it.

---


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

- I decided whether a bug was fixed or not by going into the game and playing with it to see if it was fixed. Additionally, I asked Copilot to write pytests for the bugs that we fixed, and it was able to do that. I ran the pytest and all 4 passed. The AI helped a lot with the designing and giving me a better understanding of the tests, by writing comments when needed to explain the tests.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

- Since there was no session state that persists, reruns reset the variables. That in turn leads to the secret being regenerated each time. Script reruns on every interaction, and session state is the memory that persists across reruns of the game/program. The change that was implemented was checking if the "secret" is not in `st.session_state` to only generate once. Only regenerating a "secret" when the difficulty changes or when out-of-range.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

- One habit is highlighting lines where I want Copilot to look at. Next time I want to spend more time reading through the what Copilot says. Sometimes, Copilot spits out a wall of text that I just briefly skim through the bullet points and then move on. Next time I want to spend more time reading through and understand everything Copilot says. Before this project, I never messed with Copilot too much, but I'm realizing just how powerful Copilot and these AI models are when it comes to coding tasks. It also made me realize the importance of writing detailed prompts, so that the AI models can give me the output I wanted. 