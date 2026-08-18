# I Want, I Have — Moderated User-Test Script

## Purpose

Test one question before building a marketplace:

> Can a buyer who urgently needs an item understand the request flow, compare a useful nearby offer, and confidently start a conversation—and can a provider understand how to publish stock and respond?

This prototype tests comprehension and workflow. It does **not** test real AI accuracy, real stock, real matching, authentication, notifications, payments, or transactions.

## Recommended participants

- **5–7 buyers** who have recently searched for a locally available item.
- **5–7 providers** from one product category and one dense area.
- Run buyer and provider sessions separately where possible.
- Allow approximately **20 minutes** per participant.

## Before each session

1. Double-click `app/index.html` in Edge or Chrome.
2. Refresh the page to reset the demonstration.
3. Tell the participant: “This is a simulated concept. Please speak your thoughts aloud. We are testing the idea, not you.”
4. Do not explain the interface unless the participant is completely blocked.
5. Do not collect real addresses, phone numbers, payment details, or confidential business data.

## Buyer task

Read this prompt only:

> “You urgently need a 20,000mAh power bank today. Use this prototype to ask nearby providers, compare an offer, and send a message.”

Observe whether the participant can:

- Identify **I Want** without coaching.
- Choose an input method.
- Understand that product analysis is simulated and editable.
- Notice and correct one product detail.
- Set urgency, distance, quantity, budget, and fulfilment.
- Understand the match cards and select a provider.
- Explain why they chose that provider.
- Send a message.

Ask afterward:

1. What did you think would happen after posting?
2. Which information made you trust or distrust a provider?
3. Was anything misleading or unclear?
4. When would you use this instead of Google, Facebook, Shopee, or calling shops?
5. How quickly would a real provider need to respond for this to be useful?
6. Would you use it again? Why or why not?

## Provider task

Read this prompt only:

> “You run a nearby shop. Use the prototype to scan a shelf, check the detected items, publish your stock, and respond to a buyer.”

Observe whether the participant can:

- Identify **I Have** without coaching.
- Understand what the simulated shelf scan is meant to do.
- Review item names, prices, quantities, and availability.
- Notice the low-confidence item.
- Edit a price before publishing.
- Understand what “Published & live” means.
- Recognize the buyer request and start a response.

Ask afterward:

1. What work would this save compared with your current process?
2. How often could you realistically update stock and prices?
3. What would make you trust or reject a buyer request?
4. Which inventory details are essential before publishing?
5. Would responding create too much staff work?
6. What would make you keep using this after the first week?

## Record these measures

| Measure | Result |
|---|---|
| Completed without help | Yes / No |
| Time to first major action | |
| Number of times moderator helped | |
| Understood simulation disclosure | Yes / No |
| Correctly explained the product concept | Yes / No |
| Buyer: chose a provider and explained why | Yes / No |
| Provider: edited and published stock | Yes / No |
| Serious confusion or false expectation | |
| Willingness to try a real pilot | 1–5 |

## Decision after usability tests

Do **not** decide based only on whether participants liked the screens. Proceed to a small manual pilot only if both sides understand the workflow and enough providers are willing to respond quickly.

For the real manual pilot, track:

- Percentage of requests receiving at least one accurate offer.
- Median time to first useful response.
- Percentage of requests fulfilled.
- Accuracy of quoted stock and price.
- Buyer willingness to reuse.
- Provider effort and willingness to continue.

Keep the pilot to one dense area and one urgent product category before building a backend.
