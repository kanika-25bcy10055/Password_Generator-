# Password Generator

A small Python script to generate secure random passwords.

Usage (interactive):

```powershell
python Password_Generator.py
```

Usage (non-interactive):

```powershell
python Password_Generator.py -l 12          # generate one password of minimum length 12
python Password_Generator.py -l 10 --no-special -n 3  # generate 3 passwords of length >=10 without special chars

Copy to clipboard:

The script can copy the last generated password to the clipboard using the `--copy` flag. It requires the `pyperclip` package. Install with:

```powershell
pip install pyperclip
```

Example:

```powershell
python Password_Generator.py -l 12 --copy
```
```

No external dependencies; uses Python standard library.
