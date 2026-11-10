#!/usr/bin/env python3
import subprocess, datetime, random

def random_date(start, end):
    dt = start + datetime.timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )
    # Return in ISO 8601 format with timezone offset
    return dt.strftime('%Y-%m-%dT%H:%M:%S+00:00')

# Customize the window
START = datetime.datetime(2018, 1, 1)
END = datetime.datetime(2021, 12, 31)

# Build git-filter-repo expression that sets both author and committer dates
expr = f'set_commit_date({random_date(START, END).encode()!r})'
cmd = ['git', 'filter-repo', '--force', '--date-order', '--commit-callback', expr]
subprocess.run(cmd, check=True)
print("Dates rewritten. Push with --force-overwrite origin <branch>")