# Scribus News Articles Importer

This repository contains a Python script to import news article titles and descriptions from an XML file into separate text frames in a Scribus document.

## Prerequisites

- **Scribus**: Version 1.5.5 or later.
- **Python**: Installed with Scribus.
- **XML File**: An XML file containing the news articles.

## Files

- **import_news.py**: The Python script that imports articles into Scribus.
- **news_articles.xml**: Sample XML file containing news articles.

## XML File Format

Ensure your XML file (`news_articles.xml`) has the following structure:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<articles>
    <article>
        <title>Breaking News: Market Hits Record High</title>
        <description>The stock market reached a new all-time high today as investors reacted positively to the latest economic data...</description>
    </article>
    <article>
        <title>Sports Update: Local Team Wins Championship</title>
        <description>In an exciting final match, the local team clinched the championship title after a dramatic comeback...</description>
    </article>
    <article>
        <title>Technology: New Smartphone Released</title>
        <description>The latest smartphone model features a range of new functionalities and improvements, including...</description>
    </article>
    <article>
        <title>Health: New Study on Exercise Benefits</title>
        <description>A recent study highlights the significant benefits of regular exercise on overall health and well-being...</description>
    </article>
    <article>
        <title>Entertainment: Upcoming Movie Premiere</title>
        <description>The much-anticipated movie is set to premiere next month, featuring an all-star cast and...</description>
    </article>
</articles>
