diff --git a/strings/split.py b/strings/split.py
index ed194ec6..31d1c1d3 100644
--- a/strings/split.py
+++ b/strings/split.py
@@ -21,13 +21,17 @@ def split(string: str, separator: str = " ") -> list:
 
     split_words = []
 
+    sep_len = len(separator)
     last_index = 0
-    for index, char in enumerate(string):
-        if char == separator:
-            split_words.append(string[last_index:index])
-            last_index = index + 1
-        if index + 1 == len(string):
-            split_words.append(string[last_index : index + 1])
+    i = 0
+    while i <= len(string) - sep_len:
+        if string[i : i + sep_len] == separator:
+            split_words.append(string[last_index:i])
+            last_index = i + sep_len
+            i = last_index
+            continue
+        i += 1
+    split_words.append(string[last_index:])
     return split_words
 
 
