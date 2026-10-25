# SentenceCard

The one thing on the main screen. The sentence you are saying now.

- White `surface` card, 1px `line` border, `radius-card`, 20 padding. On phones it fills the space between the top bar and the buttons, so the buttons never move.
- The count in `small` `muted` at the top left, Edit at the top right in semibold `accent-text`, which opens Edit sentence.
- The characters always start 120 from the top of the card, 85 on short phones. Below them pinyin in `body` `accent-text` and English in `body` `muted`.
- Long sentences step down from 40 to 32 to 28, 56 to 44 to 36 on laptops, instead of making the card taller. On the smallest phones a very long one scrolls inside the card.
- English is optional. When it is empty the line keeps its space.
- The StatusPill sits at the bottom left of the card while playing, only as wide as its words.
