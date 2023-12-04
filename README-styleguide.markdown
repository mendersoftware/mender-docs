# Mender Documentation writing style guide

## Why do we need one?

To help us write documentation in a more clear way and keep a consistent tone,
voice, and style.

We have many writers and different reviewers, this guide is a reference for all
to follow. Our audience members have diverse backgrounds in terms of language
and skills, however we can assume a certain base level of reading, comprehension
and technical knowledge. Keeping this in mind, we should make it as easy as
possible for all of our target audience to use our product. Consistency and
simplicity helps all our readers.

## What does it cover?

This documentation style guide borrows from the style guides of [IBM
developerWorks](https://www.ibm.com/developerworks/library/styleguidelines/index.html),
and [Red Hat style guides](https://stylepedia.net/style/). It covers the general
guidelines of grammar and punctuation, but not design, layout or content, this
is handled on a per PR basis.

## Spelling

Use American English conventions rather than British English.

Examples:

> * "-ize", not "-ise": e.g. "customize"
> * "color" not "colour"

Spelling can also be checked with the `spell-check.sh` script.

## Use a single space before a new sentence after periods - not double spaces

Example:

> "First sentence. Second sentence."

## Headers

Capitalize using sentence case.

Example:

> "Deploy an Operating System update demo"

Headers should not end with a period.


## Use second person ("you") when speaking to or about the reader

Avoid gender-specific pronouns: use "they" and "their" rather than "he/she" and
"his/hers." In most cases, use "you" when giving instructions, and "the user,"
"new users," and so on in more general explanations.

## Shorter words when possible

Examples:

> * "helps" rather than "facilitates"
> * "uses" rather than "utilizes."

## Active voice is preferred over passive voice

Unless one of the following applies:

* The system performs the action.
* It is more appropriate to focus on the receiver of the action.
* You want to avoid blaming the user for an error, such as in an error message.
* The information is clearer in passive voice.
* Avoid -ing endings if possible as they make the sentence longer and more passive / less actionable. Examples:.
* "Get started", not "Getting started".
* "Provision a new device", not "Provisioning a new device".
* Helpful resource: the section titled "Passive Voice Should Never Be Used by
  You" in the [Linux Journal Author's
  Guide](https://www.linuxjournal.com/author/authguide).

## Sentence structure

* Shorter length.
* Avoid run on sentences.
* Avoid fragments.
* Avoid unnecessary words (while not resorting to telegraphic style).
* Word order (subject-verb-object).
* Refer to https://stylepedia.net/style/#sentence-structure for details.

## Colons and semicolons:

Use a colon when introducing a list or bullet list.

A phrase following a semicolon or colon should begin with a lowercase letter,
unless it begins with a proper noun. Example:

> "Older Mender clients do not support newer versions of the Mender Artifact format; they will abort the deployment."

## Parentheses

Use parentheses to improve the readability of sentences which include extra
incidental information. Expressions beginning with i.e., e.g., that is and so on
can be also set off with parentheses if they cause a major break in the
sentence. If the break is minor, use commas instead.

## Acronyms

Should be defined the first time they are used, if they are likely to be
unfamiliar to the user. However we can assume the user is familiar with common
acronyms such as IP, OS, GB, RAM, SD card and so on).

A/an before acronyms:

The general rule is to use a before consonants and an before vowels. The trick
here is to use your ears (how the acronym is pronounced), not your eyes (how
it's spelled). Example:

> * SD (pronounced "ess dee") begins with a vowel sound, so an SD card is correct.
> * JSON (beginning with the "jay" consonant sound) would be a JSON object.

## Abbreviations

Use periods:

Examples:

> e.g., i.e., etc.

## Numbering:

* Numbers 1-9 should be written as words (one, two, three, etc.).
* Numbers >=10 to be written as numbers.
* Use a comma separate large numbers (e.g. 10,000).
* Exceptions: avoid mixing number formats in same sentence.
* Don't write: "...while three of our customers have over 20,000 devices...".
* Do write: "...while 3 of our customers have over 20,000 devices...".

## Use present tense as much as possible

The users most often refer to the documentation while they are using the product.
Example:

> "The screen displays..." rather than "the screen will display..."

## Bullet point lists

* Complete sentence bullet points should end with a period.
* Non-complete sentences (like simply a list of items) should not end in a period.

Example of sentences:

> * Alice is taller than Bob.
> * Bob is heavier than Alice.

Example of items:
> * U-Boot
> * GRUB
> * Refer to How to Capitalize and Punctuate Bullet Points for details

# Useful tools

Punctuation and grammar tools: these apps can help evaluate your writing and warn about common problems such as passive voice, complexity, sentence length etc.

* https://grammark.org
* http://www.hemingwayapp.com
* https://grammarly.com (payware)
* [./scripts/weasel.sh](./scripts/README-weasel.markdown) <file>

# Taxonomy

Our taxonomy reference can be found [here](02.Overview/15.Taxonomy/docs.md).

# Miscellaneous 

* External links should always open in a new tab/window
* Linking from docs.mender.io -> mender.io/Mender Hub counts as external
* Internal links should open in the same tab/window. E.g. from one docs page to another

Open links in the current tab:

> [https://docs.mender.io](https://docs.mender.io)

And in a new tab:

> [https://docs.mender.io](https://docs.mender.io?target=_blank)




# Readability

Technical documents should be readable by the targeted audience. In this
instance, we expect our audiences to have the minimum reading and comprehension
level of an eighth-grade student, of an age between 14 and 15 years. The
Flesch-Kincaid and Gunning Fog index provide measurable grades. A documentation
tutorial should have a Gunning Fog index of 9-12.
