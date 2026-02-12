\# 🎸 Fret Explorer \*\*by Henrique Arnold\*\*
This document is also available in [Português (Brasil)](README_ptbr.md).

A string instrument fretboard visualizer developed entirely in
\*\*Python\*\*.

\-\--

\## 📖 Description \*\*Fret Explorer\*\* is a tool for musicians that
allows for the visualization of scales, triads, and intervals on various
instruments (Guitar, Bass, Ukulele, etc.). It supports 4 to 12 strings
with an interface that adapts in real-time to the user\'s needs.

\-\--

\## 🚀 Key Features

\* \*\*Multi-Instrument Support:\*\* Dynamic adjustment from 4 to 12
strings. The app automatically recognizes industry-standard tunings for
4 to 9 strings. \* \*\*Lefty Mode:\*\* Complete horizontal inversion of
the fretboard, frets, and markings. \* \*\*Advanced Note
Visualization:\*\* \* Dynamic labels (Standard Notation vs. Intervals).
\* \*\*Bi-color System\*\* (arcs) to identify dual harmonic functions on
the same note. \* Quick secondary color clearing with a right-click. \*
\*\*Scale Library:\*\* Quick access to patterns like Major, Natural
Minor, Pentatonics, Greek Modes, and Harmonic Minor. \*
\*\*Internationalization:\*\* Fully bilingual interface
(\*\*Portuguese\*\* and \*\*English\*\*) with instant switching. \*
\*\*Preset System:\*\* Save your favorite configurations in JSON files
for later reference. \* \*\*Data Validation:\*\* Protection against
invalid notes and handling of \'X\' characters for custom tunings above
10 strings.

\-\--

\## 🛠️ Technologies Used \* \*\*Language:\*\* Python 3.12.9 \*
\*\*GUI:\*\* Tkinter (Native Graphical Interface) \*
\*\*Persistence:\*\* JSON (Preset Storage)

\-\--

\## 📋 How to Run

\> \*\*Note:\*\* These instructions are based on \*\*Windows and
macOS\*\* environments and do not include specific directions for Linux
distributions.

0\. \*\*For non-programmers:\*\* Download the executable directly and
run it. If Windows warns about an \"unknown file,\" click on \*More
info\* and \*Run anyway\*. 1. \*\*To run the source code:\*\* Ensure you
have \*\*Python 3.12.9\*\* installed on your machine. 2. Download the
\`fret.py\` file. 3. Run the \`fret.py\` file directly or through your
preferred IDE (most should already have all necessary libraries, as they
are native). 4. The \`guitar_presets.json\` file will be created
automatically in the same folder when saving the first preset.

\-\--

\## ⌨️ Shortcuts and Usage Tips \* \*\*Left Click (on the color
box):\*\* Opens the color picker for the note/interval. \* \*\*Right
Click (on the secondary color box):\*\* Clears the secondary color,
returning the note to a solid color. \* \*\*⚙ Settings:\*\* Opens the
configuration window (only one instance at a time). \* \*\*Apply
Changes:\*\* Updates tuning and strings. Replace all \'X\' with valid
notes before applying.

\-\--

\## 📜 Dev Log Summary Development followed a logical sequence of 26
steps, starting from the mapping of the 12-note chromatic scale and
bimodal rendering on the Tkinter Canvas, to the final refactoring for
code compaction and implementation of different logics throughout the
process for the creation of the executable.

\-\--

\## 👤 Author \*\*Henrique Arnold\*\* \* Computer Engineering Student \*
Fret Explorer © 2026
