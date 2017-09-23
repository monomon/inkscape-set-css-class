# Set CSS class Inkscape extension

This extension sets a CSS class on elements selected in Inkscape.
It optionally clears their inline styles, in order for the CSS styling to have effect.

This works well in conjunction with "Merge Styles into CSS".

## Installation

Use the included `setup.py` script:

    python setup.py install

or manually copy the files to your Inkscape extensions directory.

On Linux this is usually `~/.config/inkscape/extensions` and on Windows it is `%APPDATA%\inkscape\extensions`.

## Usage

Select objects in the document, and in the menu select `Extensions->Set CSS class on elements`.

## License

GPL-2.0
