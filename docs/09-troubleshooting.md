# Troubleshooting

Things break sometimes. Here are the ten most common problems and the exact fix for each.

If your issue isn't here, scroll to the bottom for how to contact us.

---

## 1. "Claude keeps asking me to set up"

**What's happening:** You probably opened the wrong folder. The assistant only recognises you when you open the **my-assistant** folder specifically.

**Fix:**

1. Close Claude Desktop completely.
2. Reopen Claude Desktop.
3. When it asks which folder, choose the folder called exactly **my-assistant**.
4. Type "hello" again.

It should now greet you by name. If it doesn't, see issue 6 below.

---

## 2. "Skills aren't showing up"

**What's happening:** The skills loaded before, but they're not loading now. Usually this means the app needs a fresh start.

**Fix:**

1. Close Claude Desktop completely. On Mac, right-click the icon in the dock and choose Quit. On Windows, close from the system tray as well as the window.
2. Wait five seconds.
3. Reopen Claude Desktop.
4. Open the **my-assistant** folder.
5. Type: "what skills do you have?"

You should see a list. If not, the install may need to be re-run. Email support.

---

## 3. "Login loop — I can't sign in"

**What's happening:** The app is stuck in a sign-in loop. It happens occasionally and is easy to clear.

**Fix:**

1. Tell your assistant: "please sign me out and back in".
2. It will run the sign-out and sign-in steps for you.
3. A browser window will pop up. Sign in with the email you used to buy Nerva OS.
4. Close the browser. The app will reconnect.

If that doesn't work, restart your computer and try again.

---

## 4. "A popup appeared about developer tools" (Mac only)

**What's happening:** Mac is offering to install a helper toolkit. The assistant needs it.

**Fix:**

1. Click the button that says exactly **Install**.
2. **Do not** click Get Xcode. That installs something much bigger and slower.
3. Wait three to five minutes for it to finish.
4. Once done, go back to the assistant and try your request again.

This popup only appears once. After that, you're set forever.

---

## 5. "Git is not recognized" (Windows only)

**What's happening:** Windows can't find one of the helper tools. There's a one-step fix.

**Fix:**

1. Open the Start menu and type: **Edit the system environment variables**.
2. Click the result that appears.
3. In the window that opens, click the button that says **Environment Variables**.
4. Under the section called **System variables**, find the row called **Path** and double-click it.
5. Click **New** and paste in: `C:\Program Files\Git\cmd`
6. Click **OK** on every window.
7. Close Claude Desktop completely and reopen it.

If you're not comfortable with this, just tell your assistant "git isn't recognized" and it will walk you through it live.

---

## 6. "Assistant says I don't know your business"

**What's happening:** The memory file is empty or missing. The assistant has nothing to read.

**Fix:**

1. Tell your assistant: "please check whether my memory file exists, and tell me what's in it".
2. It will look in the folder **my-assistant/memory/USER.md**.
3. If it's empty, say: "let's redo the onboarding interview".
4. Answer the seven questions again. (See tutorial 02.)
5. The memory will refill and the assistant will be back to normal.

---

## 7. "Browser automation isn't working"

**What's happening:** The browser helper either didn't install or isn't connected.

**Fix:**

1. Tell your assistant: "can you check whether the browser helper is connected?"
2. If it says no, ask: "please connect the browser helper for me".
3. It will run a one-line installer and tell you when it's done.
4. Close Claude Desktop completely and reopen it.
5. Try your browser task again.

If it still fails, your Node.js install may be missing. Tell your assistant: "please check whether Node is installed". It will tell you what to do.

---

## 8. "I got an error message I don't understand"

**What's happening:** Something printed a wall of red text. Don't read it. Just hand it over.

**Fix:**

1. Copy the entire error message.
2. Paste it into the chat.
3. Add this sentence: "please translate this into plain English and tell me what to do".

The assistant will read the error, explain what it means in normal words, and either fix it for you or tell you the next step.

You never need to understand error messages yourself. That's the assistant's job.

---

## 9. "Gmail or Calendar didn't connect"

**What's happening:** The Google sign-in flow got interrupted or denied.

**Fix:**

1. Tell your assistant: "let's try connecting Gmail again, from scratch".
2. A Google sign-in screen will open in your browser.
3. Click your email address.
4. On the next screen, click **Continue** or **Allow** (don't click Cancel).
5. Wait for the page to say "you can close this window".
6. Go back to Claude Desktop. The assistant will confirm the connection.

Do the same for Calendar if needed. Each one is a separate connection.

**If the screen says your account isn't approved:** your Google account has extra security. Tell your assistant and it will guide you through unlocking it.

---

## 10. "Something else broke and I can't figure out what"

This is the catch-all. Try this in order.

1. **First, ask the assistant.** Say: "something isn't working but I don't know what — can you help me figure out the problem?". It's good at this.
2. **Second, restart Claude Desktop.** Close completely. Reopen. Type your request again. Roughly a third of all problems are fixed by this alone.
3. **Third, restart your computer.** Sounds silly. Works often.
4. **Fourth, email us.** Write to **support@nerva-os.com**. Include:
   - What you were trying to do
   - What you typed
   - What the assistant said back
   - A screenshot if you can take one

We answer within one business day, usually faster.

---

## A Calm Word

Nothing here is permanent. Nothing here can break your computer. Nothing here can lose your business data. The worst case is you restart the app and try again.

If you're ever unsure, just stop and ask your assistant. That's what it's for.

---

**Next:** Once you're unstuck, head back to [02 — Your First Conversation](./02-your-first-conversation.md) or [04 — The Skill System](./04-the-skill-system.md) and keep going.
