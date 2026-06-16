# ExifTool Batch UUID Shots

A Python batch utility for assigning UUID-based identifiers to image files and storing the original filename in EXIF/XMP metadata.

> Status: personal batch-processing utility.
>
> The script modifies metadata and renames files. Test on copies first.

## What it does

For every file in `./images`, the script:

1. generates a random UUID
2. writes it to the EXIF `ImageUniqueID` tag
3. writes the original filename to the XMP `RawFileName` tag
4. renames the image to `<uuid>.jpg`

## Requirements

- Python 3
- ExifTool installed at `/opt/homebrew/bin/exiftool` or script edited for your system

Install ExifTool on macOS:

```bash
brew install exiftool
```

## Repository structure

```text
.
├── exiftool-batch-uuid-shots.py
└── README.md
```

## Expected working layout

```text
.
├── exiftool-batch-uuid-shots.py
└── images/                         # Source images to modify and rename
```

## Usage

```bash
python3 exiftool-batch-uuid-shots.py
```

## Safety notes

- The script runs ExifTool with `-overwrite_original`.
- Files are renamed in place.
- The script assumes all output filenames should end in `.jpg`.
- Keep a backup of the original image folder before running.

## License

No explicit license is included. Treat the code as all rights reserved unless a license is added by the repository owner.
