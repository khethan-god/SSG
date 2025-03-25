# Static Site Generator (SSG)

## Overview

This project is a Static Site Generator (SSG) designed to convert Markdown files into fully-functional HTML pages. The generated HTML files are structured using a pre-defined template, ensuring a consistent layout and style for all pages. The final HTML content is written within the `docs` folder which helps build static sites in github pages.

## How It Works

The SSG performs the following steps each time it is run:

1. **Clean the `/docs` Directory**  
   - All existing files in the `/docs` directory are deleted to ensure the output is fresh and conflict-free.

2. **Copy Static Assets**  
   - Assets such as HTML templates, images, CSS files, and other static resources are copied into the `/docs` directory.

3. **Convert Markdown to HTML**  
   - For every Markdown file located in the `/content` directory, the SSG executes the following steps:
     - Open and read the contents of the file.
     - Parse the Markdown into blocks (e.g., headings, paragraphs, lists).
     - Convert each block into a tree of HTMLNode objects:
       - Inline elements (e.g., bold text, links) follow this process:  
         **Raw Markdown → TextNode → HTMLNode**
     - Combine all HTMLNode blocks under a single parent HTMLNode for the page.
     - Use a recursive `to_html()` method to transform the nested HTMLNode tree into a complete HTML string.
     - Inject the HTML string into the pre-defined HTML template.
     - Save the final HTML file in the `/public` directory.

## Directory Structure

```
/content     - Contains Markdown files to be converted.
/docs        - Output directory for generated HTML files and assets.
/src         - Main working directory for code development.
```

## Features

- Automatically organizes content from Markdown into structured HTML.
- Supports inline formatting, such as bold, italic, code and hyperlinks.
- Utilizes reusable HTML templates for consistent styling.
- Cleans and prepares the output directory on every run.

## Usage

To get started, place your Markdown files in the `/content` directory and run the SSG script. The HTML output will be available in the `/docs` directory, ready to be deployed.