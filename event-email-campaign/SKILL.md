---
name: event-email-campaign
description: Plan and write personalised 3-email cold outreach sequences for event attendee lists. Interviews the user in rounds first, gathers reference material, previews on 1-2 prospects, then builds and spam-checks a sheet for every contact.
---

# Event email campaign

Use this for pre-event cold email sequences (industry conferences, trade shows, user conferences) where someone senior from your company, usually the founder or CEO, is the meeting ask. The output is three short emails per contact, personalised by news, industry and role, and checked against a spam-word list.

## Phase 0: Discovery interview (before writing anything)

Interview the user until you share an understanding of the campaign. Treat it as a decision tree: each answer opens the questions that depend on it.

**Work in rounds.** In each round, ask every question you can ask now without guessing at an answer you haven't heard yet. Number each question and give your recommended answer. Then wait. A question that depends on another one still open in the same round goes to a later round.

Format each round like this:

```
❓ **Q1** - **<title>**: <question, with options if useful>

➡️ <your recommended answer>

---

❓ **Q2** - ...
```

**Finding facts is your job, not the user's.** Look these up yourself before and during the rounds, and never ask for anything you can find:
- past campaigns and what worked (earlier conversations, notes, approved examples, subject lines, open rates)
- uploaded files: contact lists, enriched or searched email sheets, spam-word lists, marketing pages, pre-show mailers
- the event: dates, venue, agenda, session tracks, speakers, networking and 1:1 meeting areas, the meeting app
- the company: product capabilities, customers cleared for public use, proof numbers, partnerships, who is attending
- each contact: verified news from the last 6 months, a speaking slot at the event, role and tenure, line of business, regional angles

When a question needs one of these facts, look it up first and ask only the questions downstream of it once you have the answer.

**The decisions are the user's.** Typical branches:
1. **Goal and ask:** a meeting at the show, a demo, a call the week after? Who meets them? How long, and where (coffee, booth, meeting area)?
2. **Audience:** which tiers, roles and segments? Who to exclude (existing customers, competitors, partners)?
3. **Proof:** which named customers and numbers are cleared for use? What is the proof for segments with no named reference?
4. **Value for the receiver:** what do they get even if they never meet you? Options include a concrete, no-strings offer (an audit or look-back on their own data), a short benchmark or insight for their segment, the event sessions most relevant to their role, a peer introduction, or an invite to a side event. Pick one per segment.
5. **Personal hooks:** news triggers, their own session at the event, a mutual connection, a recent post, tenure. What is off-limits?
6. **Channel and timing:** sending tool, sender name and signature, send dates against the event dates, coordination with LinkedIn or other channels.
7. **Constraints:** the spam-word list, banned phrases, tone, length, things the company never says.
8. **Output:** sheet layout, columns, and whether to preview first.

The interview is done when no branch is left open and nothing is silently assumed. Confirm a short summary of the plan with the user before writing.

## Phase 1: Style rules

- **Fact-led copy:** specific facts over adjectives, write how people talk, prove every claim, and make the subject line carry the news.
- **Four rules of good writing:**
  1. **Clarity:** one idea per sentence, in plain words the reader already uses.
  2. **Simplicity:** cut jargon and anything that doesn't serve the point.
  3. **Brevity:** short sentences, short paragraphs, nothing the reader can skip.
  4. **Humanity:** write to one person, warmly, the way you'd talk to them.
- No em dashes or en dashes. Write "20 percent", never a % sign.
- Open on the reader, not the sender. Present your exec as a person ("is well known in {field} for {segment}"), not as a title.
- The CTA is a soft, short ask (coffee, 15 minutes), and the exec makes time whenever suits the reader. Never say the exec is "free".
- Every email gives the reader something: a fact about their world, a proof point or an offer. Never send a plain "just following up".
- Never invent a customer, statistic or news item. If there is no verified hook, use an industry trigger instead.

## Phase 2: Sequence structure

**Email 1** (send 4 to 5 days before the event)
- Subject: first name plus a short hook, e.g. "{First}, {Event}: the one step still done by hand".
- Opening: "{First}, I noticed you'll be at {Event} this year."
- Paragraph 1: "I read that {news}...", or an industry trigger, then the problem in concrete terms.
- Paragraph 2: the exec's credibility, "our team built {product}", what it does, that nothing gets replaced, and one proof number.
- CTA: "{Exec} is at {venue} the whole week and will make time whenever suits you. Coffee, 15 minutes? May I look at your availability on the event app and set it up?"

**Email 2** (send 2 days later): one proof point
- Subject personalised by segment, e.g. "{First}, what {Customer} changed", "{First}, AI on {Co}'s {Platform}", "{First}, a proof point for {Co}".
- Opening: "{First}, one proof point before {City}." The body is one proof: a named customer for the matching segment, or product proof otherwise. The CTA asks for their view, then the same short ask.

**Email 3** (send on the event's opening day): low pressure
- Subject: "{Co} at {Event short name}".
- Body: "{First}, I noticed a few gaps in your event calendar this week. Should I book you for coffee with {Exec}? They'd love to swap notes on {topic}." Then the value offer for their segment.
- Close: "Just say yes and I'll set it up."

## Phase 3: Personalisation layers

Layer these for every contact:
1. **Trigger:** a verified news hook from the last 6 months, or an industry trigger for their line of business if there's no news.
2. **Use case:** the problem as it shows up in their industry, plus a peer-group line naming their segment.
3. **Proof:** matched to their industry or segment.
4. **Role angle:** technical roles get the platform version (no rebuild, fits their current stack). Business roles get the outcome version (leakage, cycle time, headcount). Partners and vendors get a partnership version.
5. **Value and event relevance:** the value offer, plus their session or related sessions where you have them.

## Phase 4: Preview, then build

1. Write all three emails for 1 or 2 contrasting prospects (one technical, one business) and share them in the chat. Iterate one email at a time.
2. Offer 3 to 5 subject options with a recommended pick. Subjects that get opened are short (under about 45 characters), use the first name or company, mention their news, read like a note from a colleague, and add light curiosity.
3. After approval, generate every row with a script: map hook types to bridge text, keep each row's facts, and apply the segment and role rules. Exclude existing customers and list them on an Excluded tab.

## Phase 5: Checks

- **Spam words:** if the user gave a spam-word list, convert it to a phrase list and scan every field of all three emails, matching whole words case-insensitively, plurals included. `scripts/spam_check.py` does this. A good public list is at https://mailmeteor.com/blog/spam-words. At minimum avoid: free, money, cash, cost, price, deal, buy, offer, win, guarantee, chance, opportunity, problem, solution, never, stop, now, only, new, all, here, open, fast, check, call, click, profit, income, million, billion, %, !, $$$. Reword rather than delete ("$4.3bn" for "$4.3 billion", "earnings" for "profit", "gaps in your calendar" for "open slots"). Ask before changing company names that match the list.
- **Quality:** check for dashes, empty cells, unfilled merge fields, duplicate emails and garbled accented names. Spot-read random rows plus the approved examples.

## Phase 6: Output

Deliver a spreadsheet ready for a mail-merge tool (GMass, Instantly, Lemlist and similar).
- **Columns:** Email, First Name, Last Name, Title, Company, Short Name, then E1/E2/E3 Subject, Opening, Body and CTA, then Tier, Hook, Role, Line, E2 Version.
- **Tabs:** a "How to use" tab with send dates and rules, and an Excluded tab.

Then summarise in a few lines: the counts, how the emails were tailored by industry, any wording changed from the approved copy, and any open decisions.
