# GIMP Batch Invitation Generator
# Author: Damian Winnicki
# GitHub: https://github.com/Nerexis/gimp_batch_invitation_generator.py
# Email: nerexis@gmail.com

from gimpfu import *
import os
import platform
import subprocess

def gimp_batch_invitation_generator(image, drawable, layer_name, names, output_folder, font_name, font_size, font_color):
    if not output_folder:
        if platform.system() == 'Windows':
            output_folder = "C:\\"
        else:
            output_folder = "/tmp/"
    
    if not layer_name:
        layer_name = "NAME_LAYER"

    layer = None
    for lyr in image.layers:
        if lyr.name == layer_name:
            layer = lyr
            break
    
    if layer is None:
        pdb.gimp_message("Layer with the specified name not found.")
        return

    names_list = names.split(",")
    for name in names_list:
        name = name.strip()
        
        duplicated_image = pdb.gimp_image_duplicate(image)
        
        duplicated_layer = None
        for lyr in duplicated_image.layers:
            if lyr.name == layer_name:
                duplicated_layer = lyr
                break

        if duplicated_layer is None:
            pdb.gimp_message("Duplicated layer with the specified name not found.")
            pdb.gimp_image_delete(duplicated_image)
            continue

        if font_name:
            pdb.gimp_text_layer_set_font(duplicated_layer, font_name)
        if font_size > 0:
            pdb.gimp_text_layer_set_font_size(duplicated_layer, font_size, PIXELS)
        if font_color:
            color = gimpcolor.RGB(float(font_color[0])/255, float(font_color[1])/255, float(font_color[2])/255)
            pdb.gimp_text_layer_set_color(duplicated_layer, color)
        
        pdb.gimp_text_layer_set_text(duplicated_layer, name)
        
        output_path = os.path.join(output_folder, "{}.jpg".format(name))
        
        merged_layer = pdb.gimp_image_merge_visible_layers(duplicated_image, CLIP_TO_IMAGE)
        
        pdb.file_jpeg_save(duplicated_image, merged_layer, output_path, output_path, 0.9, 0, 0, 0, "", 0, 1, 0, 0)

        pdb.gimp_image_delete(duplicated_image)
    
    if platform.system() == 'Windows':
        subprocess.Popen(['explorer', output_folder])
    else:
        subprocess.Popen(['xdg-open', output_folder])

register(
    "python_fu_gimp_batch_invitation_generator",
    "Batch Export Invitation Cards with Names (by Damian Winnicki nerexis@gmail.com)",
    "Automates the process of creating multiple invitation cards with different names and saving them as separate JPG files.\n"
    "Text Style Information:\n"
    "If no font, size, or color is specified, the script will use the current style of the text layer named 'NAME_LAYER' by default.\n"
    "Specify a custom font, size, or color to override the layer's current settings.",
    "Your Name",
    "Your Name",
    "2024",
    "<Image>/Filters/Python-Fu/Batch Invitation Generator...",
    "RGB*, GRAY*",
    [
        (PF_STRING, "layer_name", "Layer Name (Default: NAME_LAYER)", "NAME_LAYER"),
        (PF_STRING, "names", "Comma-separated names", "John,Doe,Jane"),
        (PF_DIRNAME, "output_folder", "Output Folder", ""),
        (PF_FONT, "font_name", "Font (Optional, uses layer's font if not specified)", ""),
        (PF_SPINNER, "font_size", "Font Size (Optional, uses layer's size if not specified, in Pixels)", 0, (0, 1000, 1)),
        (PF_COLOR, "font_color", "Font Color (Optional, uses layer's color if not specified)", (0, 0, 0)),
    ],
    [],
    gimp_batch_invitation_generator)

main()
