# Pistachio

**Pistachio** is a projection system for the computer game *Out of the Park Baseball (OOTP)*.

## What It Projects

- **Position players**:  
  - wOBA  
  - WAR (by position)

- **Pitchers**:  
  - "Pitching wOBA"  
  - WAR (for starters and relievers)

## Output

When run successfully, the system generates three HTML pages:

- `pitchers.html`: Pitchers and pitching prospects  
- `hitters.html`: Hitters  
- `hit_prospects.html`: Hitter prospects

## Based on OOTP 26

These projections are built from the ground up for **OOTP 26**.  
While not perfect, the testing method is designed to be rigorous.

📊 **Testing data and methodology** (Google Sheets):  
[Detailed spreadsheet](https://docs.google.com/spreadsheets/d/19f0pZUqyonjDa2AwHckd8Al9H-wmBC6nvM-Y0RzzhSs/edit?gid=202842399#gid=202842399)

---

## Configuration Instructions

Update `config.py` to match your OOTP save:

- `filepath`: Path to your CSV exports from OOTP  
- `export_filepath`: Folder for saving HTML outputs  
- `pistachio_filepath`: Folder containing `main.py` and other scripts  
- `ID = 3332`: Your scout’s `coach_id` from `coaches.csv`  
- `team_managed = 'CHC'`: Your in-game team abbreviation

⚠️ You **must** update these before running `main.py`, or it won’t work.

### Optional Config Settings

- `club_lookup`: Maps team numbers to abbreviations (default set to MLB)
- `POSITION_THRESHOLDS`: Minimum fielding ratings by position
- **Pitcher thresholds**: Defines starter vs reliever status

ℹ️ The code expects ratings on the **20–80 scale** in increments of **5**.

---

## Additional Info

- **Player IDs** saved in `flagged.txt` can be found in outputs by:
  - Typing `flag` in the search bar
  - Using the **Custom Search Builder** in the HTML to search for 'flag equals flag'

This is useful for tracking:
- Draft prospects  
- Custom shortlists created in-game

---

## Extras

- Example outputs are included in the `outputs` folder  
  (Note: these will be overwritten once you successfully run the code in main.py with your own stuff based on your OOTP save)

- Feedback and pull requests welcome

🧵 [OOTP Forum Post (by "Squirrel")](https://forums.ootpdevelopments.com/showthread.php?t=361580)