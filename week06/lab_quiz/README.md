# Week 6 Lab: Club Registration with Lists

## Program

`lab06_club_registration.py` manages the student registrations of a university club. The three main branches are stored in a tuple, `kulup`, so they cannot be changed later. All students are stored in an empty list called `tum_ogrenciler`. Each student is a nested list in the form `["Name", ["Branches"]]`. Names are added by hand and cleaned with `strip()`, so `" Baran "` is saved as `"Baran"`. `insert(0, ...)` adds the "Başkan" student at the start, `len()` prints the total student count, `remove()` deletes Orhan, and `pop()` takes out the last student and prints only the name. After that Burak Tan (Tasarım) is added with `append()`. Finally `sorted()` prints a temporary alphabetical copy and `sort()` sorts the main list permanently.

## sorted() vs sort()

`sorted(tum_ogrenciler)` is a function that returns a new sorted copy, so the original list keeps its order. I proved this by printing the original list right after it. `tum_ogrenciler.sort()` is a list method that sorts the list itself and returns `None`, so the original order is changed for good. Nested lists are compared by their first item, which is the student name.

## Why pop(2)

At the moment of the `pop` call the list has exactly three students: Başkan, Baran and Furkan. Furkan is at index 2, which is the last position, so `pop(2)` removes the last registered student. I chose to write the index by hand. `pop()` without an index would also work and would always take the last item, even if the list length changed. I used `sonuncu[0]` to print only the name, because `pop` returns the whole student list.

## Why No input()

Task 2.1 says to add the students by hand, so I wrote the names directly in the code instead of asking the user with `input()`. I still used `strip()` on every name with extra spaces around it, for example `"  Baran  ".strip()`, so Task 2.2 is covered and `strip()` really removes spaces.

## Expected Output

| Step | Result |
|---|---|
| After `insert` | 4 students (Başkan, Baran, Furkan, Orhan) |
| `len()` output | Toplam Kayıtlı Öğrenci Sayısı: 4 |
| `remove` and `pop` | Orhan removed, then Furkan popped |
| After `append` | Başkan, Baran, Burak Tan |
| `sorted()` copy | Baran, Başkan, Burak Tan |
| Original after `sorted()` | Başkan, Baran, Burak Tan (unchanged) |
| After `sort()` | Baran, Başkan, Burak Tan (changed permanently) |

## Test I Ran

I ran the whole file and checked the terminal output. The count printed 4, the popped student printed as `Furkan`, and the original list was still in the old order after `sorted()`. After `sort()` the main list was in alphabetical order.

## What I Changed After Testing

My first version of `remove` used `["Orhan"]`, but the list contains `["Orhan", ["Pazarlama"]]`. `remove()` looks for the exact same element, so Python raised a `ValueError`. I changed it to the full student list. I also first wrote `append[...]` and `.sorted()` as if they were different kinds of calls, then fixed them to `append([...])` and `sorted(list)`. My "Başkan" student first had no branch list, so I changed it to `["Başkan", ["Yazılım"]]` to keep the same format as the other students.