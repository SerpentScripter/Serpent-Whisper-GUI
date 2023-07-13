# Serpent Whisper GUI

Serpent Whisper GUI is a user-friendly graphical interface (GUI) for [OpenAI's Whisper](https://github.com/openai/whisper), a powerful tool for multilingual speech recognition, translation, and identification. By simplifying complex tasks and harnessing the power of AI, Serpent Whisper GUI offers an efficient and streamlined platform for all your audio processing needs.

## Getting Started

Before you can use Serpent Whisper GUI, you must have Whisper installed and properly configured in your PATH environment variables. Without this step, the Whisper executable file won't be found.

### Whisper Installation and Configuration

If you haven't already done so, you can follow these steps to add the PATH to your Whisper files:

1. Download and install Whisper from the [OpenAI's Whisper GitHub page](https://github.com/openai/whisper).
2. Locate the directory where Whisper is installed.

On Windows, you can add the directory to your PATH environment variable by:

1. Right-clicking on 'Computer' and choosing 'Properties'.
2. Click on 'Advanced system settings'.
3. In the System Properties window that appears, click on 'Environment Variables'.
4. In the Environment Variables window, scroll down to 'Path' under the 'System variables' section, select it, and click 'Edit'.
5. In the 'Variable value' field, add a semicolon (;) to the end of the current value, then add the full path to the directory where Whisper is installed. Do not add a space between the semicolon and the path.
6. Click 'OK' in all windows to save the changes.

In addition to Whisper, you will also need to have `ffmpeg` installed as a prerequisite.

## Using a Virtual Environment

We recommend using a virtual environment, such as one provided by Anaconda or Miniconda, to run Serpent Whisper GUI. A virtual environment is a separate space where you can install the specific Python version and packages needed for a particular project, without affecting your system's Python installation or other Python projects.

To create a new Conda environment, you can use the following command:

\```bash
conda create -n myenv python=3.8
\```

Replace `myenv` with the name you want to give your environment, and `3.8` with the Python version you want to use.

Then, to activate the environment, use:

\```bash
conda activate myenv
\```

Now you can install the necessary packages in this environment without affecting other projects.

## Running Serpent Whisper GUI

Once you have Whisper and `ffmpeg` installed and your PATH environment variable set up correctly, and you're in your virtual environment, you can run Serpent Whisper GUI by executing the Python script:

\```bash
python serpent_whisper_gui.py
\```

Enjoy using Serpent Whisper GUI for your audio processing tasks!
