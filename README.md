# GIMP Batch Invitation Generator

**GIMP Batch Invitation Generator** is a GIMP plugin that automates the creation of multiple invitation cards with different names, applying specified text styles, and exporting each invitation as a separate JPG file.

## Features

- Batch generate invitations with custom names.
- Optionally customize text font, size, and color, or use the existing style of the text layer.
- Automatically saves each generated invitation as a JPG file.
- Opens the output folder after processing for easy access.

## Installation

### Prerequisites

- **GIMP 2.10** or later installed on your system.

### Steps

1. **Download the Plugin:**
   - Download the `gimp_batch_invitation_generator.py` file from this repository.

2. **Locate GIMP's Plugin Directory:**
   - For **Windows**:
     ```
     C:\Users\[Your Username]\AppData\Roaming\GIMP\2.10\plug-ins\
     ```
   - For **Linux**:
     ```
     ~/.config/GIMP/2.10/plug-ins/
     ```

3. **Move the Plugin:**
   - Copy the `gimp_batch_invitation_generator.py` file to the `plug-ins` directory you located in the previous step.

4. **Set Permissions (Linux Only):**
   - Ensure the script is executable by running the following command in your terminal:
     ```bash
     chmod +x ~/.config/GIMP/2.10/plug-ins/gimp_batch_invitation_generator.py
     ```

5. **Restart GIMP:**
   - Close and reopen GIMP to load the new plugin.

## Usage

1. **Open Your Invitation Template:**
   - Create or open the invitation template in GIMP.

2. **Prepare the Text Layer:**
   - Ensure the text layer you want to update with names is named `NAME_LAYER` by default, or use a custom layer name.

3. **Run the Plugin:**
   - Go to `Filters > Python-Fu > Batch Invitation Generator...`.
   - Configure the settings:
     - **Layer Name**: Specify the text layer name (default is `NAME_LAYER`).
     - **Names**: Enter a comma-separated list of names (e.g., `John,Doe,Jane`).
     - **Output Folder**: Choose the folder where you want the JPG files saved.
     - **Font Name, Size, Color**: Optionally override the layer's current text style.

4. **Generate Invitations:**
   - Click `OK` to run the plugin. The invitations will be generated and saved to the specified folder, which will automatically open when the process is complete.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request if you'd like to improve the plugin.

---

*Created by Damian Winnicki*

If you like me work, please donate:
https://www.buymeacoffee.com/nerexis