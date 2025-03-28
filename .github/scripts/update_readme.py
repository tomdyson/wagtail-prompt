# .github/scripts/update_readme.py
import os
import re
import sys

def update_readme(version, token_count, filename):
    """Updates the README.md with the latest version info."""
    readme_path = 'README.md'
    token_count_str = f'{token_count:,}' # Add commas for readability

    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()

        # Define the new section content
        latest_section_header = "## Latest Version"
        new_section_content = f"{latest_section_header}\n\n"
        new_section_content += f"The latest version processed is [{version}](./{filename})\n\n"
        new_section_content += f"**Token Count:** {token_count_str}"

        # Use regex to find and replace the section or append if not found
        pattern = re.compile(r"^## Latest Version.*?(?=^##|\Z)", re.MULTILINE | re.DOTALL)

        if pattern.search(readme_content):
            new_readme = pattern.sub(new_section_content, readme_content)
            print("Updated existing 'Latest Version' section in README.md.")
        else:
            # Append if the section doesn't exist (ensure proper spacing)
            new_readme = readme_content.strip() + "\n\n" + new_section_content
            print("Added new 'Latest Version' section to README.md.")

        # Write the updated content back to README.md
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_readme)

        print("README.md updated successfully.")

    except FileNotFoundError:
        print(f"Error: {readme_path} not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error updating README.md: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    wagtail_version = os.environ.get('WAGTAIL_VERSION')
    ttok_count = os.environ.get('TTOK_COUNT')
    output_filename = os.environ.get('OUTPUT_FILENAME')

    if not all([wagtail_version, ttok_count, output_filename]):
        print("Error: Missing required environment variables (WAGTAIL_VERSION, TTOK_COUNT, OUTPUT_FILENAME).", file=sys.stderr)
        sys.exit(1)

    try:
        # Convert token count string to int for validation/formatting if needed
        token_count_int = int(ttok_count)
    except ValueError:
        print(f"Error: Invalid TTOK_COUNT value: {ttok_count}", file=sys.stderr)
        sys.exit(1)

    update_readme(wagtail_version, token_count_int, output_filename)
