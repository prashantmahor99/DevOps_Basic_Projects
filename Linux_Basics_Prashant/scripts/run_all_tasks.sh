#!/bin/bash
set -e

echo "=== Linux Basics Assignment ==="

mkdir -p test_dir
touch test_dir/Example.txt
mv Example.txt test_dir/renamed_example.txt

echo "--- /etc/passwd ---"
cat /etc/passwd
echo "--- FIRST 5 ---"
head -n 5 /etc/passwd
echo "--- LAST 5 ---"
tail -n 5 /etc/passwd
echo "--- ROOT SEARCH ---"
grep "root" /etc/passwd

echo "--- ZIP ---"
zip -r test_dir.zip test_dir

echo "--- UNZIP ---"
mkdir -p unzipped_dir
unzip -o test_dir.zip -d unzipped_dir

echo "--- DOWNLOAD ---"
wget -q https://raw.githubusercontent.com/github/gitignore/main/Linux.gitignore -O sample.txt

echo "--- PERMISSIONS ---"
touch test_dir/secure.txt
chmod 444 test_dir/secure.txt
ls -l test_dir/secure.txt

echo "--- ENVIRONMENT VARIABLE ---"
export MY_VAR="Hello, Linux!"
echo "$MY_VAR"

echo "=== ALL TASKS COMPLETED ==="
