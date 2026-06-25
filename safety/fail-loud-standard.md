# Speak Up When Something Goes Wrong

**If something doesn't go to plan, you hear about it.**

That's the whole rule. Every skill, every automation, every background job your Nerva OS assistant runs follows it. No quiet failures. No "well, it didn't crash so it must have worked." If a task hit a wall, ran out of road, or simply didn't find what it was looking for, the assistant tells you in plain words.

This file explains what that looks like in practice, and how to check that a new automation lives up to it before you turn it on.

---

## The three things every automation must do

Anything that runs on your behalf — an email sweep, a weekly report, an invoice chase, a calendar tidy — has to hit these three marks. If it doesn't, it isn't ready to ship.

### 1. Speak up when something errors

If a step breaks, the automation doesn't shrug and keep going. It says, in plain English, what it was trying to do, what stopped it, and whether the rest of the job still finished. Even a one-line note is better than silence. The user should never have to dig through a log file to find out something went wrong.

A good version of this sounds like: "Tried to send the reminder to Jane Wilson. Her email address bounced. Skipped her for now — you'll want to update her file."

A bad version is: nothing.

### 2. Tell the difference between "nothing to do" and "the lookup didn't work"

This one trips people up. If a search returns zero results, that could mean two very different things. It could mean there's genuinely nothing to act on. Or it could mean the search itself failed quietly and there might be plenty to act on, the assistant just couldn't see it.

Every automation must check the source before reporting "all clear." If the source can't be reached, the automation says so. It does not pretend the empty result is good news.

### 3. Sort every item into one of three buckets

When the assistant works through a list — invoices, leads, emails, tasks — every single item ends up in one of three places by the end:

- **Handled.** The thing was done.
- **Needs your review.** The thing was started but the assistant wants a human call before finishing.
- **Couldn't be done.** The thing didn't go through, and here's the reason.

If an item disappears from the list without landing in one of those buckets, the automation has failed its job. The total at the end must add up to the total at the start. Always.

---

## Before you turn it on — a quick check

When you're about to switch on a new automation, or hand a skill the keys to do something on a schedule, run through this list. Answer each question honestly. If any answer is "I'm not sure," the automation isn't ready yet.

1. If the input is zero, does the report look the same as a failed lookup, or different?
2. If five items go through and one of them fails, will the failure be named by item, or just hidden inside an overall success count?
3. Is there a one-line summary at the end where the numbers add up to the total that started?
4. If an outside service the automation depends on is down, does the report say so, or does it look like the work just finished with nothing to do?
5. If something needs a human eye, does it get pulled into a "needs your review" pile, rather than quietly skipped?
6. If the same automation has run before, is this run's report easy to compare to last week's, so trends are obvious?
7. Can you read the report on your phone in under thirty seconds and know whether everything's fine?
8. If you got this report at midnight on a Sunday with no other context, would you know what to do next?

A "yes" to all eight means the automation is honest about its own work. Anything less and it needs a tighter wrap-up before it goes live.

---

## A worked example

You ran the weekly invoice chase on Monday morning. It says "done." What does done actually mean?

A weak version of that report looks like this:

> Invoice chase complete.

That tells you nothing. Did it find any overdue invoices? Did it send anything? Did it skip anything? You can't tell.

A fail-loud version looks like this:

> **Invoice chase — Monday 14 March**
> 12 overdue invoices found.
> - 9 chased by email (full list attached)
> - 2 skipped because no email address on file (Mara Tan, Greg Pinto — flagged in your customer file)
> - 1 errored: the email server rejected the message to invoices@brightside.com.au. Worth checking the address.
> Total: 9 + 2 + 3 = 12. Matches the overdue count.

Notice three things about the second version. Every item is accounted for. Every problem is named, with the customer involved and the reason. And the totals at the end add up to the totals at the start, so you can see at a glance that nothing slipped through.

That's the standard. Not every report needs to be that long, but every report needs to hit those three notes: what was done, what wasn't, and why.

If you ever get a "done" with no detail, push back. Ask "done meaning what?" and the assistant will give you the proper breakdown. Over time you'll stop having to ask.

---

*Part of Nerva OS.*
