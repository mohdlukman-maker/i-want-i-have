# Verification and Known Limits

## Verified repairs

- Fixed the update lifecycle crash caused by reading `prev.screen` from a missing argument.
- Fixed the Notes field rendering `[object Object]`; it now starts as a blank editable field.
- Added a visible disclosure: **USER-TEST PROTOTYPE · SIMULATED · NO DATA SAVED**.
- Added a true phone-responsive mode and a forced `?mobile=1` preview mode.
- Removed the designer/engineering explanation panel from the participant-facing view.
- Disabled controls that are outside this moderated test instead of presenting them as working.
- Replaced the fake account action with an honest “no account required” note.
- Added document metadata, button types, form control names, landmarks, and status announcements.
- Stored integrity-verified React 18.3.1 and ReactDOM 18.3.1 runtime files locally.

## Real execution completed

- Buyer journey: identify item -> simulated analysis -> edit details -> request options -> simulated matches -> provider -> chat.
- Provider journey: simulated shelf scan -> review four items -> edit price -> publish -> respond -> chat.
- Chat entry submitted and displayed.
- Desktop presentation visually checked.
- Forced mobile mode visually checked.
- Direct `file://` opening and interaction verified.
- Browser console checked after major buyer and provider transitions: zero application errors.
- Automated regression suite and JavaScript syntax checks passed.

## Still simulated / not implemented

No authentication, database, persistence, real camera upload, OCR/AI, location search, inventory service, real provider responses, realtime messaging, notifications, moderation, payments, transaction handling, or admin tools exist.

BGC, Taguig, Philippine-peso prices, providers, ratings, stock, and messages are sample scenario data. Refreshing resets all changes.

## Developer regression command

From the project directory on this machine:

```text
C:\Users\mohdl\AppData\Roaming\uv\python\cpython-3.11-windows-x86_64-none\python.exe -m unittest discover -s tests -v
```
