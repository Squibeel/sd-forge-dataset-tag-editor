# Dataset Tag Editor
[**Standalone version is here**](https://github.com/toshiaki1729/dataset-tag-editor-standalone): This may be better to avoid some known bugs.

This is an extension to edit captions in training dataset for [Stable Diffusion Web UI Forge by lllyasviel](https://github.com/lllyasviel/stable-diffusion-webui-forge).

**Please note that this version is only somewhat in working order as I've got no idea what I'm doing.** 

## What Works:
Tag Generation:
- BLIP
- BLIP2 (blip2-opt-2.7b-coco)
- WD (wd-swinv2-tagger-v3, wd-vit-large-tagger-v3, wd-eva02-large-tagger-v3)
Filter by Tags
Batch Edit Captions
Edit Caption of Selected Image:
- Read Caption from Selected Image (Copy and Overwrite, Prepend and Append)

## What Doesn't Work:
Edit Caption of Selected Image:
- Interrogate Selected Image

... Testing in Progress

## Installation
### Extensions tab on WebUI
Copy `https://github.com/Squibeel/sd-forge-dataset-tag-editor.git` into "Install from URL" tab.

Also, if you see this extension listed, you can install from "Available" tab with a single click.

**Please note that if you update this extension from "Extensions" tab, you will need to restart web UI to reload completely.**  

### Install Manually
To install, clone the repository into the `extensions` directory and restart the web UI.

On the web UI directory, run the following command to install:
```commandline
git clone https://github.com/Squibeel/sd-forge-dataset-tag-editor.git extensions/dataset-tag-editor
```

## Features
Note. "tag" means each blocks of caption separated by commas.
- Edit and save captions in text file (webUI style) or json file ([kohya-ss sd-scripts metadata](https://github.com/kohya-ss/sd-scripts))
- Edit captions while viewing related images
- Search tags
- Filter images to edit their caption by tags
  - AND/OR logic can be used in each Positive/Negative filters
- Batch replace/remove/append tags
- Batch sort tags
- Batch search and replace
  - [regular expression](https://docs.python.org/3/library/re.html#regular-expression-syntax) can be used
- Use interrogators
  - BLIP, BLIP2, GIT, DeepDanbooru, [Z3D-E621-Convnext](https://huggingface.co/toynya/Z3D-E621-Convnext), SmilingWolf's [WDv1.4 Tagger](https://huggingface.co/SmilingWolf) (v1, v2, v3 and some variants of them)
- You can add Custom Tagger in `userscripts/taggers` (they have to be wrapped by a class derived from `scripts.tagger.Tagger`)
  - Some Aesthetic Score Predictors are implemented in there
- Batch remove image and/or caption files


## Usage
1. Make dataset using web UI
    - better to use already cropped images
1. Load them
    - use interrogator if needed
1. Edit their captions
    - filter images you want to edit by tags in "Filter by Tags" tab
    - filter images manually in "Filter by Selection" tab
    - replace/remove tags or append new tags in "Batch Edit Captions" tab
    - edit captions individually in "Edit Caption of Selected Image" tab
      - you also can use interrogator here
    - move/delete files in "Move or Delete Files" tab if needed
1. Click "Save all changes" button


## By the way, how can I edit tags quickly?

Basic workflow is as follows:

1. Filter images
1. Batch edit

Please note that all batch editing will be applyed **only to displayed images (=filtered images)**.

### 1. Which filter is appropriate?
- **I want to edit all at once**  
  No filter is required.
- **Some images require editing**  
  1. **They should / shouldn't already have same tag(s)**  
    Go to "Filter by Tags" so that the only images to be edited are displayed.
  1. **They have nothing in common**  
    Go to "Filter by Selection" and apply.  
    Images can also be added to the filter by pushing [Enter] key.

### 2. How can I edit as I want?
- **I want to add some new tags**
  1. Go to "Batch Edit Captions" tab
  1. Append tags to "Edit tags" textbox
  1. Push "Apply changes to filtered images" button  
  "foo" and "bar" will be added to all images displayed.

- **I want to replace the tags which are common to displayed images**
  1. Go to "Batch Edit Captions" tab
  1. Replace tags in "Edit tags" textbox
  1. Push "Apply changes to filtered images" button  
  "male focus" and "solo" will be replaced with "foo" and "bar".

- **I want to remove some tags**  
  The same as replacing. Just replace the tags with "blank".  
  Also you can use "Remove" tab in "Batch Edit Captions".

- **I want to add/replace/remove tags more flexibly**
  1. Go to "Batch Edit Captions" tab
  2. Use "Search and Replace" with "Use regex" checked  
  "1boy", "2boys", … will be replaced with "1girl", "2girls", … in each tags of images displayed.  
  A comma will be regarded as the sepalator of two tags.  
  By using regex, you can add/replace/remove tags according to more complex conditions.


## Trouble shooting
### Cannot see any image in dataset and saying "All files must contained within the Gradio python app working directory…"
Set folder to store temporaly image in the "Settings" tab.
Input path in "Directory to save temporary files" and check "Force using temporary file…"

### So laggy when opening many images or extremely large image
Check "Force image gallery to use temporary files" and input number in "Maximum resolution of ..." in the "Settings" tab.  
It may not work with dataset with millions of images.  
If it doesn't work, please consider using [**stand alone version**](https://github.com/toshiaki1729/dataset-tag-editor-standalone).  
