# Event Email Campaign Skill

A reusable AI skill for writing personalised, three-email cold outreach sequences to people attending an event: conferences, trade shows and user conferences.

It turns an attendee list into short, fact-led emails that read like a note from a peer, written to four rules: clarity, simplicity, brevity and humanity. Each email is personalised by the contact's news, industry and role, and checked against a spam-word list before it goes out.

## What it does

1. **Interviews you first.** It asks questions in numbered rounds, each with a recommended answer, about your goal, audience, proof, constraints and timing. It looks up the facts itself (event agenda, company news, your past campaigns) and only asks you for decisions.
2. **Gives the reader something of value.** Every email carries a fact about their world, a proof point or a no-strings offer. Never a plain "just following up".
3. **Personalises in layers:** a news or industry trigger, a use case for their industry, proof matched to their segment, a technical or business angle by role, and the event sessions that matter to them.
4. **Previews on 1 or 2 prospects** so you can approve the copy and subject lines before it writes for everyone.
5. **Builds a mail-merge sheet** (GMass, Instantly, Lemlist and similar) with subject, opening, body and CTA columns for each email.
6. **Checks for spam words, dashes and merge errors** across every row.

## The sequence

| Email | When | Purpose |
|---|---|---|
| 1 | 4 to 5 days before the event | A news or industry trigger, the problem, who you are, one proof point, a soft meeting ask |
| 2 | 2 days later | One proof point matched to their segment |
| 3 | The event's opening day | A low-pressure booking ask plus a concrete offer |

See [`examples/example-sequence.md`](examples/example-sequence.md) for a full fictional example.

## How to use it

### Claude (claude.ai, Claude desktop, Claude Code)
Copy the `event-email-campaign` folder into your skills directory, or upload it as a skill. Then ask something like: "Use event-email-campaign to write outreach for the attached attendee list."

### Other agent tools
Point the tool at `event-email-campaign/SKILL.md`. It's a plain markdown file with YAML frontmatter, so any agent that reads SKILL.md files can load it.

### Any chat LLM (ChatGPT, Gemini and others)
Paste the contents of `SKILL.md` as custom instructions or at the start of a chat, then attach your contact list. Steps that need file or code access, like building the sheet and running the spam check, work best in a tool that can run code.

## Spam check script

```bash
pip install openpyxl
python event-email-campaign/scripts/spam_check.py emails.xlsx phrases.txt
```

`phrases.txt` holds one spam word or phrase per line. A good public source is Mailmeteor's list: https://mailmeteor.com/blog/spam-words. The script lists every hit by column with an example, so you can reword it.

## Repo layout

```
event-email-campaign/
  SKILL.md              the skill instructions
  scripts/spam_check.py spam word and dash scanner
examples/
  example-sequence.md   a fictional worked example
```

## License

MIT. See [LICENSE](LICENSE).
