import re

# Task 2: Compile a regular expression pattern
pattern = re.compile(r"\d+")

# Task 3: Find all digit matches
test_string = "The rainfall 2021 was greater than 2019 and 2020 combined."
matches = pattern.findall(test_string)
print("Matches found:", matches)
assert matches == ['2021', '2019', '2020']

# Task 4: Replace all digit matches
replaced_string = pattern.sub("XXXX", test_string)
print("Replaced String:", replaced_string)
assert replaced_string == "The rainfall XXXX was greater than XXXX and XXXX combined."

# Task 5: Capture date groups
date_pattern = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
date_string = "Date of birth: 1990-08-15 and starting date 2020-01-01."
date_matches = date_pattern.findall(date_string)
print("Date Matches:", date_matches)
assert date_matches == [('1990', '08', '15'), ('2020', '01', '01')]

# Task 5: Use named groups
named_date_pattern = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")
for match in named_date_pattern.finditer(date_string):
    print("Year:", match.group("year"), "Month:", match.group("month"), "Day:", match.group("day"))
