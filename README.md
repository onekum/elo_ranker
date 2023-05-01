A sorting method that uses the Elo Sort system, originally designed to rank chess players. Potentially more accurate than Merge Sort, though will take much longer as it needs to compare every single combination of items.

## Running

Run this command in the terminal; admin privileges are not required:

```
python elo_ranking.py item1 item2 item3 ...
```

The script takes the items for comparison as arguments upon execution. 

A theoretical infinite amount of items are allowed to be taken as arguments, but massive amounts of items will take an **extremely** long time for the user to rank. Use my merge sort ranker if you plan on sorting a large amount of items.