# Dataset Tag Editor for Stable Diffusion Forge

**An extension for [Stable Diffusion Forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) to efficiently manage and edit tags (`.txt`, `.caption`) for your image datasets.**

This is a fork of [toshiaki1729's Dataset Tag Editor](https://github.com/toshiaki1729/stable-diffusion-webui-dataset-tag-editor), adapted and maintained for compatibility with the Stable Diffusion Forge UI.

Stop juggling separate text files and image viewers! This extension integrates tag editing directly into your Forge workflow, saving you time and effort when preparing datasets for Dreambooth, LoRA training, or general organization.

---

## ✨ Key Features

*(These features are inherited from the original extension and function within Forge)*

* **🖼️ Integrated Image & Tag Viewing:** Browse images from your dataset directory alongside their corresponding tag files (`.txt` or `.caption`) directly within the Forge UI.
* **✏️ Intuitive Tag Editing:** Easily add, remove, and reorder tags for individual images.
* **🔄 Powerful Batch Editing:**
    * **Search and Replace:** Modify tags across your entire dataset or filtered selection.
    * **Append/Prepend:** Add tags to the beginning or end of existing tag lists for selected images.
    * **Remove:** Delete specific tags or tag blocks from selected images.
* **🔍 Advanced Filtering & Searching:**
    * Quickly find images based on included or excluded tags.
    * Filter by file path/name (supports regular expressions).
    * Isolate images with or without existing tag files.
    * Combine multiple filter criteria.
* **⌨️ Keyboard Shortcuts:** Speed up your workflow with keyboard navigation and editing commands.
* **⚙️ Customizable UI:** Adjust thumbnail sizes, tag display, and other interface elements.
* **🏷️ Flexible Tag Separators:** Configure the separator character used in your tag files (e.g., comma, space).
* **💾 Load/Save Settings:** Persist your preferred filter, search, and UI settings between sessions.

---

## 🚀 Installation (for Stable Diffusion Forge)

You can install this extension using either the Forge UI or by cloning the repository manually.

**Method 1: Using the Forge UI (Recommended)**

1.  Launch Stable Diffusion Forge.
2.  Navigate to the **Extensions** tab.
3.  Click on the **Install from URL** sub-tab.
4.  Paste the following URL into the "URL for extension's git repository" field:
    ```
    [https://github.com/Squibeel/sd-forge-dataset-tag-editor.git](https://github.com/Squibeel/sd-forge-dataset-tag-editor.git)
    ```
5.  Click **Install**.
6.  Wait for the installation to complete.
7.  **Important:** Restart the Stable Diffusion Forge UI completely (reloading the UI via settings might not be sufficient for Forge).

**Method 2: Manual Installation (Git Clone)**

1.  Open a terminal or command prompt.
2.  Navigate to the `extensions` directory within your Stable Diffusion Forge installation folder (e.g., `stable-diffusion-webui-forge/extensions/`).
3.  Clone the repository using the following command:
    ```bash
    git clone [https://github.com/Squibeel/sd-forge-dataset-tag-editor.git](https://github.com/Squibeel/sd-forge-dataset-tag-editor.git)
    ```
4.  **Important:** Restart the Stable Diffusion Forge UI completely.

---

## 💡 Getting Started

1.  After installation and restarting Forge, you will find a new tab named **Dataset Tag Editor**.
2.  **Load Your Dataset:**
    * Enter the path to your image dataset directory in the "Dataset Directory" field.
    * *(Optional)* Enter the path to your tag file directory if it's different from the image directory.
    * Click **Load**.
3.  **Browse and Edit:**
    * Images and their tags (if found) will be displayed.
    * Click on an image or its tags to select it for editing.
    * Use the text box below the tags to modify them. Changes are saved automatically when you move to another image or explicitly save.
    * Use the filter and search bars at the top to narrow down your view.
    * Explore the "Batch Edit Tags" and "Settings" sections for advanced operations and customization.

---

## 🛠️ Detailed Functionality

*(Refer to the Key Features section. Functionality remains largely the same as the original extension.)*

### Batch Edit Tags
Select multiple images (using Shift+Click, Ctrl+Click, or filter results) and use the options in the "Batch Edit Tags" section (Replace, Remove, Append, Prepend).

### Filtering and Searching
Use the top bar to filter by included/excluded tags, filename, or tag file status. Combine filters for precise selections.

### Keyboard Shortcuts
Use these keys for faster editing (when the tag editing area is focused):
* `Ctrl + Enter` / `Cmd + Enter`: Save changes for the current image.
* `Ctrl + ArrowUp` / `Cmd + ArrowUp`: Move to the previous image.
* `Ctrl + ArrowDown` / `Cmd + ArrowDown`: Move to the next image.
* *(Verify and add other essential shortcuts)*

### Settings
Customize tag separators, thumbnail sizes, and load/save UI preferences.

---

## 🙏 Acknowledgements

This extension is a fork based on the excellent work done by **toshiaki1729** on the original [Dataset Tag Editor](https://github.com/toshiaki1729/stable-diffusion-webui-dataset-tag-editor). This version focuses specifically on compatibility and integration with Stable Diffusion Forge.

---

## 🤝 Contributing

Contributions, issues, and feature requests specifically for the **Forge version** are welcome!

1.  **Issues:** Please report any bugs or suggest features related to Forge compatibility via the [GitHub Issues page for this fork](https://github.com/Squibeel/sd-forge-dataset-tag-editor/issues).
2.  **Pull Requests:** If you'd like to contribute code improvements for Forge:
    * Fork this repository (`Squibeel/sd-forge-dataset-tag-editor`).
    * Create a new branch for your feature or bug fix.
    * Make your changes.
    * Submit a pull request to this repository with a clear description of your changes.
