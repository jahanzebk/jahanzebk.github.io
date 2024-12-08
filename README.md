
# Files

- index.html is the main html
- index.js has the main javascript using pig.js
- pig.js is the library that helps render the gallery so fine
- legend.json is maintained by the script make_legend.py

# Uploading

Upload photos to the uploads/ folder and run the following

```
source pyenv/bin/activate
python smart-resize.py
python make_legend.py
```

Run `python3 -m http.server` and confirm the http://localhost:8000/ shows the gallery properly.

Then empty the uploads/ folder and do a git commit and push!


# TODO
- upload to github website
- add more pics
- add jquery or some event listener on #pig-figure to try enlarge the image (inspect page to see) upon clicking, even if it's to 500 res (or keep a 1024 res pic?)
- extend with ability to tag images and add a search?