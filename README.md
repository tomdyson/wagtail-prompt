# Wagtail Prompt

This repository automatically fetches the documentation from the latest Wagtail release and converts it into a single text file suitable for prompting LLMs.

## How It Works

- A GitHub Action runs daily at midnight UTC
- The action fetches the latest Wagtail release (not the `main` branch)
- It extracts the documentation from the `docs` directory
- Using the `files-to-prompt` tool, it converts all `.md` and `.rst` files into a single consolidated text file
- The resulting file is named `wagtail-docs-[version number].txt`

## Files

This repository contains:

- A series of documentation files for different Wagtail versions (`wagtail-docs-[version number].txt`)
- This README.md file

## Manual Triggering

You can manually trigger the workflow by going to the "Actions" tab in the GitHub repository and selecting "Fetch Wagtail Docs" workflow, then clicking "Run workflow".

## Using the Documentation

The generated text files are formatted specifically for use with Large Language Models. They contain the consolidated documentation with proper context and formatting to maximize the LLM's ability to understand and utilize the Wagtail documentation.

## Claude's Recommended XML Structure

We are using Claude's recommended XML structure for the combined documentation. This structure helps in organizing the content in a way that is optimized for processing by Large Language Models. For more details on the XML structure, please refer to [Claude's Long Context Tips](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/long-context-tips).

## Excluded Content

The content of the 'releases' directory is excluded from the combined documentation.


## Latest Version

The latest version is [v6.4.1](./wagtail-docs-v6.4.1.txt)

**Token Count:** 296632