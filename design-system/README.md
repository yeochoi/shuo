# Shuo

Say it until it is yours. A calm shadowing app for Mandarin. Each sentence plays twice, then waits while you say it out loud. When you can say it easily, you tap Got it and it moves to Learned. Shuo shares its foundations with the Stay Counter design system and has its own red accent.

## Principles

1. **One sentence at a time.** The screen holds the sentence you are saying now. The list, settings and forms wait in sheets.
2. **Eyes on the words, thumb on Play.** The sentence card is always the same height, so Play, previous, next and Got it never move. You can tap them without looking.
3. **Red acts, everything else is quiet.** Red is for Play, Got it, pinyin and what you are on. Ink, muted and the warm white carry the rest.
4. **Nothing is lost.** Got it moves a sentence, it does not delete it. Undo stays for a few seconds. Only delete removes sentences, and it always asks first.
5. **One way to do each thing.** Top left always closes a sheet, the bottom holds the one forward action.

## Color

| Role | Tokens | Use |
| --- | --- | --- |
| Action | `primary`, `accent-text`, `soft` | Play, Add, Got it, pinyin, the status pill, the selected segment |
| Current | `current` | The sentence you are on in the list |
| Ground | `bg`, `surface`, `line` | Screens, cards, dividers |
| Text | `ink`, `muted` | Characters, English, labels and notes |
| Quiet | `chip`, `chevron` | The disabled previous button and quiet icons |
| Attention | `warn-text` | Delete all sentences, the one action that can't be undone |
| Overlay | `backdrop` | Behind sheets |

Rules
- `primary` is a fill. Red text always uses `accent-text`.
- Characters are always `ink`, never red. Red is for what you hear and do, the characters are what you read.
- Text passes 4.5 to 1 everywhere it sits. The token notes list each pair.

## Typography

Outfit for everything in Latin letters and Noto Serif SC for Chinese characters, so the sentence feels like writing and the interface stays quiet. One exception, 说 in the name and the icon uses Noto Sans SC Medium, so it reads as a mark rather than a sentence.

Five text styles like iOS, plus Chinese. The same scale runs across Shuo, Stay Counter and Manna.

| Style | Size | Weight | For |
| --- | --- | --- | --- |
| `sentence` | 40, 56 on laptop | Semibold serif | The sentence on the card |
| `section` | 20 | Semibold | Section headers, like Playback and Sentences. 32 above, 12 below |
| `title` | 17 | Semibold | Buttons, sheet titles, the name |
| `body` | 17 | Regular | Pinyin, English, labels, settings. Like iOS body text |
| `small` | 13 | Regular | The count, notes, field labels, pinyin in lists |
| `list-han` | 17 | Semibold serif | Characters in a list row |

Text inputs use 17, so iOS does not zoom. No other exceptions.

Rules
- Serif for Chinese characters you read. Sans only for 说 in the name and icon.
- Only 400 and 600 in Latin text.
- Every sentence starts at the same height, 120 from the top of its card, so your eye finds it in one place. Long sentences step down from 40 to 32 to 28 instead of growing the card.
- On phones the buttons sit at the bottom of the screen and never move. The card fills the space between the top bar and the buttons. The status pill sits at the bottom of the card, only as wide as its words.
- Large Latin text uses minus 0.02em letter spacing.

## Layout

- Phones use a 22 side margin on every screen and sheet.
- Pinch zoom always works. Buttons ignore double tap zoom so taps stay quick.
- The colour behind the page is `bg`, the same as the top of the screen, so the home screen app shows no fade under the time.
- One column everywhere. On laptops the column grows to 600 and sits in the vertical middle of the screen, with the characters at 56.
- On devices with a keyboard and mouse, a quiet hint under Got it shows the shortcuts.
- The main screen, top to bottom, is the title row, the sentence card, the play row, Got it and one note.
- Cards are white with a 1px `line` border and `radius-card`. No shadows.

## Navigation

- No tabs. The main screen is the app.
- Three round buttons at the top right. + opens New sentence, then Sentences and Settings.
- Every round button is the same flat grey circle. `chip`, 44 wide, a 20 icon with a 2 line in `ink`, no shadow, no line. That covers the top buttons, previous and next, and the sheet close. A disabled button keeps its circle and only fades its icon to `chevron`.
- Destructive actions always go last. A single one is plain coral text, centered. Two or more related ones are grouped in one card. They always ask first.
- Layers follow iOS. Things that float over content are glass with a shadow. Things on the page are flat. Nothing in Shuo floats, so everything is flat.
- Sheets have one rule. Top left leaves. × closes a first screen, ‹ goes back one step, like Design system back to Settings. The bottom holds one forward action, like Add sentence or Add. Settings has no bottom button, changes save as you tap.
- Settings has a Design system row that opens a short version of this book inside the app.
- On laptops sheets open in the middle over a dimmed page.
- Sheets move like iOS. On phones a sheet rises from the bottom and the page steps back behind it, smaller and dimmed. A sheet opened from another sheet slides in from the right, and ‹ slides it back. Pull the grabber or the title down to close. Segmented switches slide to the chosen option.

## Practice

- Play reads each sentence twice, then pauses for the time chosen in Settings, then moves on. It stops at the end of the list.
- The pill on the card says where you are. Listen, Listen again, then Your turn in solid red.
- Previous and next keep playing if Play was on.
- Got it moves the sentence to Learned and shows a toast with Undo for 4 seconds.
- Shuo opens on the sentence you were on last time.
- On a keyboard, Space plays or pauses, the left and right arrows move, Enter is Got it, and Escape closes a sheet. Keys do nothing while you type or while a sheet is open.

## Sentences

- The Sentences sheet has two tabs, Practice and Learned, each with its count.
- In Practice, tapping a sentence jumps to it. The one you are on uses `current`.
- In Learned, Practice again moves a sentence back to Practice and opens it.
- Add a sentence with + on the main screen or Add sentence in the Sentences sheet.
- New sentences go to the top of Practice, so you say them next.
- Only Chinese is required. Pinyin and English are optional.
- Edit on the sentence card, or the pencil on a row in Sentences, opens Edit sentence. It is the same form as New sentence with Save, and Delete sentence below the card.
- Saved pinyin and English stay as they are when you change the Chinese. Clear a field to fill it in again.
- Edit from the card closes with ×. Edit from the list goes back to it with ‹.
- Settings has Start over, which moves every learned sentence back to Practice, and Delete all sentences in `warn-text`, which empties the list. Each row says how many it affects, and both ask first.
- An empty list shows one quiet line in the middle of the card, No sentences yet, in 17 regular `muted`. No count, no second line. The Add a sentence button below is the one action.
- Pinyin fills in on the phone as you type the Chinese. English comes from the free MyMemory translation service a moment later.
- Both stay editable. Once you type in a field yourself, Shuo stops filling it.
- If the English can't be fetched, a calm note says so and you can add without it.

## Icon

- 说, speak, the word the name comes from, in Noto Sans SC Medium.
- White on `primary`, a full square. Phones round the corners themselves.
- The character is traced as a shape and centred by its own edges, not by the font baseline, so it sits in the true middle.
- `icon.svg` is the source. The PNG sizes are made from it.

## Writing

- Plain words, sentence case, short. No colons, semicolons or dashes in UI text.
- Talk about the person's action, like Got it, Your turn, Practice again.
- Calm words for problems, with what to try next. When no Chinese voice is found, Settings explains which browsers work best instead of showing an error.

## Files

`tokens.json` holds every colour, type style, spacing, radius and size. `tokens.css` is made from it and the app loads it, so the app and this book never drift. Each folder in `components` has a guide and a live preview. Run `node scripts/build-design-system.mjs` after changing anything here to rebuild `tokens.css` and the page at `/shuo/design-system/`.
