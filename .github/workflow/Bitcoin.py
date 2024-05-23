name: Bitcoin

on:
  schedule:
  - cron: "*/5 * * * *"

jobs:
  write-prices:
    runs-on: ubuntu-latest

steps:
- name: checkout repository
  uses: actions/checkout@v2
  With:
    token: ${{ secrets.GITHUB_TOKEN }}

- name: Set up Python
  uses: actions/setup-python@v2
  With:
    python-version: '3.x'

- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install requests

- name: Run Python script
  run: |
    python Bitcoin.py 

- name: Commit changes
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}  # Ensure the token is available
  run: |
    git config --global user.name 'cavwaweru'
    git config --global user.email 'josephwaweru23@user.noreply.github.com'
    git add bitcoin_prices.csv
    git commit -m 'Update bitcoin_prices.csv with new prices'
    git push https://x-access-token:${GITHUB_TOKEN}@github.com/${{ github.repository }}.git HEAD:${{ github.ref }}



