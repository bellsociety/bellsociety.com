# Bell Senior Society Website

### Startup Guide

To start developing locally we need to run the following commands. First, initialize and download the `LoveIt` submodule that we use at the theme for this Hugo site:
```
git submodule init
git submodule update
```
Once you have the theme installed, you can run the site in development mode with Hugo:
```
hugo serve -D
```
Hugo will hot-reload changes you make to the site, so no need to restart the process as you make changes (just reload the page).

If you do not already have Hugo installed, you can find installation instructions [here](https://gohugo.io/getting-started/installing/). On macOS, you can just run `brew install hugo`.


## Adding people

If you'd like to add new people to the website, follow the steps below:

Edit the `config.toml` file to add an entry as follows, replacing `$YEAR`
with your class year.

```toml
  [[menu.main]]
    identifier = "$YEAR"
    name = "$YEAR"
    url = "$YEAR"
    title = ""
    weight = 1
```

Navigate to the `webscrape/` directory

    cd webscrape

Run the import data script after changing the `CLASS_YEAR` variable in the file
and setting the `PATH_TO_CSV` to point to the path to your downloaded Excel
sheet (in `.csv` format).

    python3 import_data.py

This script does most of the work for you -- it creates the relevant markdown
files with everyone's bios.

Images, however, don't usually work as smoothly. See the comments in
`import_data.py` for more information. You'll likely need to manually add some
folks' images into the repository.


### Contributors

Ben Demers, Campbell Phalen, Danny Bessinov, Praneeth Alla, and Rohan Gupta.
