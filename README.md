# Wagtail Prompt

This repository automatically fetches the documentation from the latest Wagtail release and converts it into a single text file suitable for prompting LLMs with large context windows. At the time of writing, only Gemini models have context windows large enough to support the Wagtail documentation (around 270k tokens).

## How It Works

- A GitHub Action runs daily at midnight UTC
- The action fetches the latest Wagtail release (not the `main` branch)
- It extracts the documentation from the `docs` directory
- Using `files-to-prompt`, it converts all `.md` and `.rst` files into a single consolidated text file
- The resulting file is named `wagtail-docs-[version number].txt`
- Using `ttok`, it counts the tokens for the consolidated text file and updates the README

## Files

This repository contains:

- A series of documentation files for different Wagtail versions (`wagtail-docs-[version number].txt`)
- This README.md file
- The Github action for generating the documentation files and updating this README.md

## Using the Documentation

The generated text files are formatted specifically for use with Large Language Models. They contain the consolidated documentation with proper context and formatting to maximize the LLM's ability to understand and utilize the Wagtail documentation. We're using [Anthropic's recommended XML structure](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/long-context-tips) for the combined documentation. The uploaded documentation should precede the question or request in your prompt.

## Excluded Content

The content of the 'releases' and 'contributing' directories is excluded from the combined documentation.

## Latest Version

The latest version is [v7.0](./wagtail-docs-v7.0.txt)

**Token Count:** 269606