import os
import re
import shutil

# Define paths
posts_dir = r"C:\Users\Owner\Documents\igetime\content\posts"
attachments_dir = r"C:\Obsidian Vault\Thoughts\Thoughts\images"
static_images_dir = r"C:\Users\Owner\Documents\igetime\static\images"

# Process each Markdown file
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Find image links
        images = re.findall(r'!\[\[([^\]]+\.(?:png|jpg|jpeg|gif))\]\]', content)
        
        # Process each image
        for image in images:
            # Create Markdown-compatible link
            markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            content = content.replace(f"![[{image}]]", markdown_image)
            
            # Copy image to static/images
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # Write updated content back to the Markdown file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")
